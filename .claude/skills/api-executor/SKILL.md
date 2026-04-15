---
name: api-executor
description: "内部 API 执行技能，用于读取认证配置并执行已确认的 item-tickets 请求。"
user-invocable: false
disable-model-invocation: true
---

# API Executor

用于根据已确认的 `request_plan` 执行 item-tickets 请求。
这是内部技能，只供执行型子 agent 使用，不直接面向用户。

## 前置条件

调用前应当已经拿到结构化的 `request_plan`，至少包含：
- `method`
- `path`
- `path_params`
- `query_params`
- `body`

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

- 必须存在 `request_plan`
- 必须存在 `runtime_api_context`
- `request_plan` 缺失时，直接返回 `invalid_request_plan`
- `runtime_api_context` 缺失时，直接返回 `missing_runtime_api_context`
- 不要从自然语言自行猜测请求计划
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

通过 shell 执行构造好的 curl 命令。

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

### 6. 返回结果

优先返回结构化 JSON：

```json
{
  "status": "success",
  "http_status": 201,
  "business_success": true,
  "data": { ... },
  "summary": "请求执行成功",
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
  "debug_env": {
    "runtime_api_context": {
      "baseUrl": "https://...",
      "x-tickets-token": "token-from-env",
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

## 注意事项

- 写操作应由主 agent 先确认；如果调用方没确认，执行子 agent 应拒绝继续
- curl 输出可能很长，只返回关键字段
- 敏感信息不要原样回传，用 `***` 遮蔽
- 不要读取 `.claude/api-config.json`，即使它存在
- 如果本地调试需要认证信息，也必须由调用方显式传入 `runtime_api_context`，不要自行读文件
- 收到自然语言直输但缺少结构化 `request_plan` 时，直接失败，不要先读文件再判断
- 失败时必须把当前收到的 env 上下文放进 `debug_env`
- 这个 skill 负责执行约定，不负责业务解释或用户话术
