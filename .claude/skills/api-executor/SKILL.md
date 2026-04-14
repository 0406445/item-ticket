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

所有配置从 `.claude/api-config.json` 读取：

```json
{
  "baseUrl": "https://unisticket-staging.item.com/api/item-tickets",
  "x-tickets-token": "your-token-here",
  "x-tickets-timezone": "Asia/Shanghai",
  "x-tenant-id": "your-tenant-id"
}
```

如果配置文件不存在或缺少任何字段，必须停止执行并把错误交回主 agent。

## 执行流程

### 1. 读取认证配置

```bash
cat .claude/api-config.json
```

验证四个必填字段都存在且非空：`baseUrl`、`x-tickets-token`、`x-tickets-timezone`、`x-tenant-id`。

### 2. 构造 curl 命令

**【强制】baseUrl 必须从 `.claude/api-config.json` 的 `baseUrl` 字段读取，禁止硬编码、猜测或使用任何其他地址。**

- 禁止使用 localhost、127.0.0.1 或任何非配置文件中的地址
- 索引中的 path 不带前缀，执行时必须拼接成 `{配置中的 baseUrl} + path`
- 如果配置文件中没有 `baseUrl` 字段，停止执行并报错

必须包含的固定请求头：
- `accept: application/json, text/plain, */*`
- `accept-language: en-US`
- `content-type: application/json`（POST/PUT/PATCH 请求时）
- `origin: https://unisticket-staging.item.com`
- `referer: https://unisticket-staging.item.com/`
- `user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36`

认证头从配置文件填充：
- `x-tickets-token: {从配置读取}`
- `x-tickets-timezone: {从配置读取}`
- `x-tenant-id: {从配置读取}`

curl 规则：
- 加 `-s` 静默模式
- 加 `-w '\n%{http_code}'` 获取 HTTP 状态码
- query 参数拼接在 URL
- path 参数替换到路径中
- JSON body 用 `--data-raw`

### 3. 执行请求

通过 shell 执行构造好的 curl 命令。

### 4. 响应校验

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

### 5. 返回结果

优先返回结构化 JSON：

```json
{
  "status": "success",
  "http_status": 201,
  "business_success": true,
  "data": { ... },
  "summary": "请求执行成功"
}
```

失败时：

```json
{
  "status": "failed",
  "http_status": 400,
  "business_success": false,
  "error_message": "参数错误: name 字段不能为空",
  "suggestion": "请提供部门名称后重试"
}
```

## 注意事项

- 写操作应由主 agent 先确认；如果调用方没确认，执行子 agent 应拒绝继续
- curl 输出可能很长，只返回关键字段
- 敏感信息不要原样回传，用 `***` 遮蔽
- 这个 skill 负责执行约定，不负责业务解释或用户话术
