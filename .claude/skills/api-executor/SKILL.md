---
name: api-executor
description: "Execute API requests against item-tickets backend. Takes validated API info (method, path, body), constructs curl with auth headers, executes, and returns structured results with response validation."
---

# API Executor（API 请求执行）

当需要**实际发送 HTTP 请求**到 item-tickets 后端时使用本技能。

## 前置条件

调用本 skill 前，必须已经完成：
1. API 查找（通过 findapiagent）
2. 参数校验和用户确认（通过 api-validator）

## 认证配置

认证信息从 `.claude/api-config.json` 读取：

```json
{
  "x-tickets-token": "your-token-here",
  "x-tickets-timezone": "Asia/Shanghai",
  "x-tenant-id": "your-tenant-id"
}
```

如果配置文件不存在或缺少字段，**必须停止执行**并提示用户创建配置文件。

## 执行流程

### 1. 读取认证配置

```bash
cat .claude/api-config.json
```

验证三个必填字段都存在且非空：`x-tickets-token`、`x-tickets-timezone`、`x-tenant-id`。

### 2. 构造 curl 命令

baseUrl 固定为: `https://unisticket-staging.item.com/api/item-tickets`

**重要**：INDEX 中的 API path（如 `/v1/staff/staff`）不包含 `/api/item-tickets` 前缀，构造 URL 时必须拼接为 `baseUrl + path`，即 `https://unisticket-staging.item.com/api/item-tickets/v1/staff/staff`。如果缺少 `/api/item-tickets` 前缀，nginx 会返回 405 Not Allowed。

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

curl 参数规则：
- 加 `-s` 静默模式
- 加 `-w '\n%{http_code}'` 获取 HTTP 状态码
- query 参数拼接在 URL
- path 参数替换到路径中
- JSON body 用 `--data-raw`

### 3. 执行请求

通过 bash 执行构造好的 curl 命令。

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

输出格式：

```json
{
  "success": true,
  "http_status": 201,
  "data": { ... },
  "summary": "部门「技术部」创建成功，ID: 42"
}
```

失败时：

```json
{
  "success": false,
  "http_status": 400,
  "error": "参数错误: name 字段不能为空",
  "suggestion": "请提供部门名称后重试"
}
```

## Checklist

```
- [ ] 读取 .claude/api-config.json 获取认证信息
- [ ] 验证认证字段完整
- [ ] 构造完整 curl 命令
- [ ] 执行请求
- [ ] 校验 HTTP 状态码
- [ ] 校验业务状态
- [ ] 返回结构化结果
```

## 注意事项

- **绝对不要**在没有用户确认的情况下执行写操作（POST/PUT/DELETE）
- 如果认证配置缺失，停止执行并引导用户创建配置
- curl 输出可能很长，只提取关键信息返回
- 敏感信息（token）不要在输出中完整展示，用 `***` 遮蔽
