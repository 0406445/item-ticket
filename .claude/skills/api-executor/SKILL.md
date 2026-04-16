---
name: api-executor
description: "内部 API 执行技能，用于接收主 agent 透传的运行时 API 上下文并执行已确认的 item-tickets 请求。"
user-invocable: false
disable-model-invocation: true
---

# API Executor

用于根据已确认的 `execution_plan` 或单步 `request_plan` 执行 item-tickets 请求。
这是内部技能，只供执行型子 agent 使用，不直接面向用户。

## 前置条件

调用前应当已经拿到结构化的执行输入，优先使用：

- `execution_plan`
  - `goal`
  - `confirmed`
  - `expectation`
  - `steps[]`

每个 `step` 至少包含：

- `step_id`
- `purpose`
- `request_plan`
  - `method`
  - `path`
  - `path_params`
  - `query_params`
  - `body`
- `extract`
- `checks`

兼容旧链路时，也允许直接收到单步 `request_plan`。这时你应先把它规范化成仅含一个 step 的 `execution_plan` 再执行。

## 认证配置

执行时只允许使用输入里提供的 `runtime_api_context`。
`runtime_api_context` 应由调用方根据运行时环境变量构造后传入。
禁止把 `.claude/api-config.json` 或其他本地文件当作认证兜底。

`runtime_api_context` 通常由以下环境变量映射而来，结构至少包含：

```json
{
  "baseUrl": "<from TICKETS_BASE_URL>",
  "x-tickets-token": "<from TICKETS_TOKEN>",
  "x-tickets-timezone": "<from TICKETS_TIMEZONE>",
  "x-tenant-id": "<from TENANT_ID>"
}
```

也可能额外收到：

```json
{
  "runtime_system_language": "en-US"
}
```

如果缺少 `runtime_api_context`，或缺少任一必填字段，必须立即停止执行并把错误交回主 agent。
不要为了“补齐认证”去读取 `.claude/api-config.json`。

## 执行流程

### 1. 前置校验

先校验输入是否完整：

- 必须存在 `execution_plan.steps` 或 `request_plan`
- 必须存在 `runtime_api_context`
- 两者都缺失时，直接返回 `invalid_request_plan`
- `runtime_api_context` 缺失时，直接返回 `missing_runtime_api_context`
- 不要从自然语言自行猜测请求计划
- 如果只收到自然语言描述但没有结构化计划，直接失败
- 如果收到 `execution_plan`，逐 step 执行；不要自己改写或合并步骤语义
- 不要读取 `.claude/api-config.json`
- 不要调用 `Read` 打开 `.claude/api-config.json`
- 不要使用 `cat .claude/api-config.json`、`less .claude/api-config.json` 或任何等价方式读取本地认证文件

### 2. 读取认证配置

只允许读取并使用：

- `runtime_api_context.baseUrl`
- `runtime_api_context.x-tickets-token`
- `runtime_api_context.x-tickets-timezone`
- `runtime_api_context.x-tenant-id`

验证四个必填字段都存在且非空：`baseUrl`、`x-tickets-token`、`x-tickets-timezone`、`x-tenant-id`。
`x-tickets-token` 只能从 `runtime_api_context` 读取；它本质上来自运行时环境变量 `TICKETS_TOKEN`。

### 3. 构造 curl 命令

**【强制】baseUrl 必须从 `runtime_api_context` 读取。**

- 禁止使用 localhost、127.0.0.1 或任何非 `runtime_api_context` 中的地址
- 索引中的 path 不带前缀，执行时必须拼接成 `{runtime_api_context.baseUrl} + path`
- 如果 `runtime_api_context` 中没有 `baseUrl` 字段，停止执行并报错

必须包含的固定请求头：
- `accept: application/json, text/plain, */*`
- `accept-language: {runtime_system_language；若未提供则默认 en-US}`
- `content-type: application/json`（POST/PUT/PATCH 请求时）
- `origin: https://unisticket-staging.item.com`
- `referer: https://unisticket-staging.item.com/`
- `user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36`

认证头从当前生效配置填充：
- `x-tickets-token: {从 runtime_api_context 读取}`
- `x-tickets-timezone: {从 runtime_api_context 读取}`
- `x-tenant-id: {从 runtime_api_context 读取}`

curl 规则：
- 加 `-s` 静默模式
- 加 `-w '\n%{http_code}'` 获取 HTTP 状态码
- query 参数拼接在 URL
- path 参数替换到路径中
- JSON body 用 `--data-raw`

### 4. 执行请求

按 `execution_plan.steps` 的顺序逐步执行 shell 请求。

- 每个 step 都要单独记录请求与响应
- 如果某一步失败，保留已执行步骤的 trace，再决定返回 `failed` 或 `partial`
- 不要跳步，也不要因为“看起来像常识”而省略 lookup / 当前用户 / 统计步骤

### 5. 响应校验

拿到响应后，按以下顺序校验：

#### ① HTTP 状态码校验
| 状态码 | 判定 |
|--------|------|
| 2xx | 成功，继续解析 body |
| 401 | 认证失败 → 提示用户检查 token |
| 403 | 权限不足 → 提示用户检查权限 |
| 404 | 资源不存在 → 提示检查路径或 ID |
| 422/400 | 参数错误 → 解析错误信息，给出修正建议 |
| 5xx | 服务端错误 → 提示稍后重试 |

#### ② 业务状态校验
很多 API 返回 HTTP 200 但 body 中有业务错误码，检查：
- `code` 字段是否为 0 或 200（成功）
- `success` 字段是否为 true
- `message` / `msg` 字段是否有错误信息

#### ③ 响应结构校验
如果有预期的 response schema，检查返回的 JSON 是否包含预期的关键字段。

#### ④ step 提取与校验
- 按 `extract` 规则从每个 step 的响应中提取字段
- 按 `checks` 逐项校验，并在结果里返回 `passed: true/false`
- 如果关键结论缺少证据路径或提取失败，不要自己补一个“合理值”

### 6. 返回结果

优先返回结构化 JSON：

```json
{
  "status": "success",
  "http_status": 201,
  "business_success": true,
  "request_echo": {
    "execution_mode": "single_step",
    "step_count": 1,
    "steps": [
      {
        "step_id": "count_staff",
        "method": "POST",
        "path": "/v1/staff/staff/page"
      }
    ]
  },
  "summary": "请求执行成功",
  "data": { ... },
  "evidence": {
    "staff_total": {
      "step_id": "count_staff",
      "path": "response.body.data.total",
      "value": 1
    }
  },
  "trace": [
    {
      "step_id": "count_staff",
      "purpose": "按部门统计成员数量",
      "status": "success",
      "request": {
        "method": "POST",
        "path": "/v1/staff/staff/page",
        "path_params": {},
        "query_params": {},
        "body": {},
        "headers": {
          "accept-language": "zh-CN",
          "x-tickets-token": "***",
          "x-tickets-timezone": "Asia/Shanghai",
          "x-tenant-id": "1"
        }
      },
      "response": {
        "http_status": 200,
        "body": {}
      },
      "extracted": {
        "staff_total": 1
      },
      "checks": [
        {
          "name": "staff_total_present",
          "passed": true
        }
      ]
    }
  ],
  "warnings": [],
  "debug_env": null
}
```

失败时：

```json
{
  "status": "failed",
  "http_status": 400,
  "business_success": false,
  "error_message": "参数错误: name 字段不能为空",
  "suggestion": "请提供部门名称后重试",
  "trace": [],
  "debug_env": {
    "runtime_api_context": {
      "baseUrl": "https://...",
      "x-tickets-token": "***",
      "x-tickets-timezone": "Asia/Shanghai",
      "x-tenant-id": "1"
    },
    "runtime_system_language": "en-US"
  }
}
```

失败结果里的 `debug_env` 规则：

- 必须返回这次实际收到的环境上下文
- 至少包含 `runtime_api_context` 和 `runtime_system_language`
- 没收到的字段显式返回 `null`
- 不要自己构造不存在的 env 值
- 这个字段就是给调试透传问题看的

新增字段要求：

- `trace`：必须按执行顺序保留每一步的完整请求 body 和原始响应 body；如果响应过大，可截断，但必须显式标记 `truncated: true`
- `evidence`：所有会被上游拿去直接说给用户的数字、ID、名称，必须有对应证据路径
- `summary`：只能复述 `trace` / `evidence` 已经证明的事实，不能新增任何未经证据支持的数字或判断
- 如果请求执行成功但关键结论证据不足，返回 `status: "needs_confirmation"`，不要假装成功

## 注意事项

- 写操作应由主 agent 先确认；如果调用方没确认，执行子 agent 应拒绝继续
- curl 输出可能很长，但 `trace.request.body` 与 `trace.response.body` 不能省略
- 敏感信息不要原样回传，用 `***` 遮蔽
- 不要读取 `.claude/api-config.json`，即使它存在
- 如果本地调试需要认证信息，也必须由调用方显式传入 `runtime_api_context`，不要自行读文件
- 收到自然语言直输但缺少结构化 `request_plan` 时，直接失败，不要先读文件再判断
- 失败时必须把当前收到的 env 上下文放进 `debug_env`
- 这个 skill 负责执行约定，不负责业务解释或用户话术
- 任何数字如果不能从响应里直接提取，就不要写进 `summary`、`data` 或 `evidence`
