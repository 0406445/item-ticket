# Open API 文档

## 概述

Open API 允许外部系统通过 API Key 与 Agent 进行交互。支持以下功能：

- 获取 Agent 列表和详情
- 发送对话消息（支持流式 SSE 和非流式 JSON）
- 结构化输出（通过 JSON Schema 约束 Agent 响应格式）
- 动态外部工具调用（让 Agent 调用客户端提供的自定义工具）
- 通过 WebSocket 进行实时双向对话
- 查询会话消息历史
- 上传文件附件（base64 编码）

**Base URL**

```
https://agentforce.item.pub
```

**通用响应格式**

所有 REST API 返回统一的 JSON 信封格式：

```json
{
  "success": true,
  "data": { ... }
}
```

错误时：

```json
{
  "success": false,
  "error": "错误描述"
}
```

---

## 认证方式

所有 Open API 端点通过 **API Key** 认证。在请求头中携带：

```
Authorization: Bearer laf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

API Key 格式为 `laf_` 前缀 + 32 位十六进制字符串（共 36 字符）。

可在系统的 **API Keys** 页面创建和管理 Key。

**认证失败响应**

| 状态码 | 场景 | 响应 |
|--------|------|------|
| 401 | 缺少 Authorization 头 | `{"success": false, "error": "Missing API key"}` |
| 401 | Key 无效或已过期 | `{"success": false, "error": "Invalid or expired API key"}` |

---

## 获取 Agent 列表

获取当前组织下所有可用的 Agent。

```
GET /api/v1/open/agents
```

**请求头**

| 名称 | 必填 | 说明 |
|------|------|------|
| Authorization | 是 | `Bearer laf_xxx` |

**响应示例**

```json
{
  "success": true,
  "data": [
    {
      "id": "83e9af68-e385-4f50-8574-06aa61c11566",
      "name": "客服助手",
      "description": "智能客服 Agent，支持多轮对话",
      "avatar": null,
      "model": "claude-sonnet-4-20250514"
    }
  ]
}
```

**响应字段**

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | Agent 唯一标识（UUID） |
| name | string | Agent 名称 |
| description | string \| null | Agent 描述 |
| avatar | string \| null | Agent 头像（base64 图片数据） |
| model | string \| null | 使用的模型标识 |

**curl 示例**

```bash
curl https://agentforce.item.pub/api/v1/open/agents \
  -H "Authorization: Bearer laf_your_api_key_here"
```

---

## 获取 Agent 详情

获取指定 Agent 的详细信息，包含系统提示词。

```
GET /api/v1/open/agents/:id
```

**路径参数**

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | 是 | Agent ID（UUID） |

**响应示例**

```json
{
  "success": true,
  "data": {
    "id": "83e9af68-e385-4f50-8574-06aa61c11566",
    "name": "客服助手",
    "description": "智能客服 Agent，支持多轮对话",
    "avatar": null,
    "model": "claude-sonnet-4-20250514",
    "systemPrompt": "你是一个专业的客服助手..."
  }
}
```

**响应字段**

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | Agent 唯一标识 |
| name | string | Agent 名称 |
| description | string \| null | Agent 描述 |
| avatar | string \| null | Agent 头像 |
| model | string \| null | 模型标识 |
| systemPrompt | string | 系统提示词 |

**错误响应**

| 状态码 | 说明 |
|--------|------|
| 404 | Agent 不存在或不属于当前组织 |

**curl 示例**

```bash
curl https://agentforce.item.pub/api/v1/open/agents/AGENT_ID \
  -H "Authorization: Bearer laf_your_api_key_here"
```

---

## 发送对话

向指定 Agent 发送消息，支持流式（SSE）和非流式两种模式。支持多轮对话和文件附件。

```
POST /api/v1/open/agents/:id/chat
```

**路径参数**

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | 是 | Agent ID（UUID） |

**请求体**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| message | string | 是 | 用户消息内容（最少 1 个字符） |
| session_id | string | 否 | 会话 ID（UUID）。传入以继续多轮对话，省略则自动创建新会话 |
| stream | boolean | 否 | 是否流式返回，默认 `true` |
| attachments | array | 否 | 文件附件列表，最多 10 个文件 |
| env | object | 否 | Session 级环境变量覆盖（仅在不带 session_id 创建新会话时生效）。key 必须为合法变量名（`[A-Za-z_][A-Za-z0-9_]*`），最多 50 个，单个 value 最大 8KB。安全敏感变量（如 `ANTHROPIC_*`、`PATH`、`HOME` 等）会被自动过滤 |
| tools | array | 否 | 外部工具定义列表（最多 50 个），仅流式模式可用。不可与 `response_format` 同时使用。详见「外部工具调用」章节 |

**附件格式（attachments 数组元素）**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| filename | string | 是 | 文件名（含扩展名），如 `report.pdf` |
| data | string | 是 | 文件内容的 base64 编码 |
| content_type | string | 否 | MIME 类型，默认 `application/octet-stream` |

支持的文件类型包括但不限于：图片（png/jpg/gif）、PDF、Office 文档、文本文件、CSV、JSON 等。单个文件最大 50MB。

### 非流式响应（stream=false）

**响应示例**

```json
{
  "success": true,
  "data": {
    "session_id": "96de3d24-c6eb-40aa-9ec7-1d760b5ce532",
    "content": "你好！有什么可以帮你的？",
    "thinking": "用户在打招呼，我应该友好回应...",
    "tool_calls": [
      {
        "id": "tooluse_abc123",
        "name": "search",
        "input": { "query": "相关信息" },
        "result": "搜索结果...",
        "is_error": false
      }
    ],
    "usage": {
      "input_tokens": 150,
      "output_tokens": 80
    }
  }
}
```

**响应字段**

| 字段 | 类型 | 说明 |
|------|------|------|
| session_id | string | 会话 ID，后续多轮对话需传回 |
| content | string | Agent 回复的文本内容 |
| thinking | string（可选） | Agent 的思考过程（如果模型支持） |
| tool_calls | array（可选） | 工具调用记录 |
| tool_calls[].id | string | 工具调用 ID |
| tool_calls[].name | string | 工具名称 |
| tool_calls[].input | object | 工具输入参数 |
| tool_calls[].result | string（可选） | 工具执行结果 |
| tool_calls[].is_error | boolean（可选） | 工具执行是否出错 |
| usage | object | Token 使用统计 |
| usage.input_tokens | number | 输入 Token 数量 |
| usage.output_tokens | number | 输出 Token 数量 |

**curl 示例**

```bash
curl -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "你好",
    "stream": false
  }'
```

### 流式响应（stream=true，默认）

返回 Server-Sent Events (SSE) 流。

**响应头**

```
Content-Type: text/event-stream
Cache-Control: no-cache
Connection: keep-alive
```

**事件类型**

每个事件以 `data: ` 前缀发送，格式为 JSON 对象。

#### 1. session — 会话信息（首个事件）

```
data: {"type":"session","session_id":"96de3d24-c6eb-40aa-9ec7-1d760b5ce532"}
```

#### 2. thinking — Agent 思考过程

```
data: {"type":"thinking","content":"让我想想这个问题..."}
```

#### 3. text — 文本内容（逐段推送）

```
data: {"type":"text","content":"你好"}
data: {"type":"text","content":"！有什么"}
data: {"type":"text","content":"可以帮你的？"}
```

#### 4. tool_use — 工具调用

```
data: {"type":"tool_use","id":"tooluse_abc123","name":"search","input":{"query":"相关信息"}}
```

#### 5. tool_result — 工具执行结果

```
data: {"type":"tool_result","tool_use_id":"tooluse_abc123","content":"搜索结果...","is_error":false}
```

#### 6. external_tool_call — 外部工具调用（需客户端执行并返回结果）

当 Agent 需要调用客户端注册的外部工具时，会发送此事件。客户端收到后需执行对应工具，并通过 `POST /sessions/:id/tool-result` 返回结果。

```
data: {"type":"external_tool_call","request_id":"req-abc123","tool_name":"get_weather","tool_input":{"location":"NYC"},"timeout":30000}
```

| 字段 | 类型 | 说明 |
|------|------|------|
| request_id | string | 唯一请求 ID，提交结果时需回传 |
| tool_name | string | 工具名称（匹配注册时的 name） |
| tool_input | object | 工具输入参数 |
| timeout | number | 超时时间（毫秒），默认 30000。超时未返回结果则 Agent 收到超时错误 |

#### 7. done — 完成（最后一个事件）

```
data: {"type":"done","usage":{"input_tokens":150,"output_tokens":80}}
```

#### 8. error — 错误（如果发生）

```
data: {"type":"error","message":"处理请求时出错"}
```

#### 结束标记

```
data: [DONE]
```

**SSE 事件顺序**

```
session → [thinking] → [text]* → [tool_use → tool_result]* → [external_tool_call → (客户端回调)]* → [text]* → done → [DONE]
```

**curl 示例**

```bash
curl -N -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "你好",
    "stream": true
  }'
```

### 多轮对话示例

```bash
# 第一轮：创建新会话
RESPONSE=$(curl -s -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{"message": "记住数字 42", "stream": false}')

# 提取 session_id
SESSION_ID=$(echo $RESPONSE | jq -r '.data.session_id')

# 第二轮：继续对话
curl -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d "{
    \"message\": \"我刚才说的数字是什么？\",
    \"session_id\": \"$SESSION_ID\",
    \"stream\": false
  }"
```

### 带环境变量示例

```bash
# 创建新会话并注入自定义环境变量
curl -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "请读取 $DB_HOST 环境变量",
    "stream": false,
    "env": {
      "DB_HOST": "10.0.1.100",
      "DB_PORT": "5432",
      "TENANT_ID": "org_abc123"
    }
  }'
```

> **注意**：`env` 仅在创建新会话时生效（即不传 `session_id`）。后续带 `session_id` 继续对话时，`env` 字段会被忽略，会话始终使用首次创建时设置的环境变量。

### 带附件示例

```bash
# 将文件编码为 base64
FILE_BASE64=$(base64 < document.pdf)

curl -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d "{
    \"message\": \"请分析这份文档\",
    \"stream\": false,
    \"attachments\": [
      {
        \"filename\": \"document.pdf\",
        \"data\": \"$FILE_BASE64\",
        \"content_type\": \"application/pdf\"
      }
    ]
  }"
```

**错误响应**

| 状态码 | 说明 |
|--------|------|
| 400 | 请求体无效（缺少 message 或格式错误） |
| 404 | Agent 不存在或不属于当前组织 |
| 503 | Open API 服务不可用 |

---

## 结构化输出

通过 `response_format` 参数，可以强制 Agent 按照指定的 JSON Schema 返回结构化数据。适用于需要机器解析响应的场景，如数据提取、分类、实体识别等。

> **注意**：结构化输出仅支持 REST API（`POST /api/v1/open/agents/:id/chat`），不支持 WebSocket 协议。

### 请求参数

在发送对话的请求体中额外传入 `response_format` 字段：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| response_format | object | 否 | 结构化输出格式定义 |
| response_format.type | string | 是 | 固定值 `"json_schema"` |
| response_format.json_schema | object | 是 | JSON Schema 定义 |
| response_format.json_schema.name | string | 是 | Schema 名称标识（1-64 字符，仅字母数字下划线） |
| response_format.json_schema.schema | object | 是 | 符合 JSON Schema 规范的对象定义 |

### 非流式响应（stream=false）

```json
{
  "success": true,
  "data": {
    "session_id": "bdc1113b-8693-42f7-8e11-729917ac3233",
    "structured_output": {
      "intent": "询价",
      "sender": "zhangsan@example.com",
      "subject": "询问产品报价",
      "key_info": {
        "product": "服务器",
        "quantity": 100
      },
      "urgency": "medium"
    },
    "tool_calls": [...],
    "usage": {
      "input_tokens": 4,
      "output_tokens": 556
    }
  }
}
```

**响应字段**

| 字段 | 类型 | 说明 |
|------|------|------|
| session_id | string | 会话 ID |
| structured_output | object | 符合请求中 JSON Schema 定义的结构化数据 |
| content | string（可选） | Agent 的文本回复（结构化模式下通常为空） |
| tool_calls | array（可选） | 工具调用记录（包含内部 StructuredOutput 工具调用） |
| usage | object | Token 使用统计 |

### 流式响应（stream=true）

流式模式下，结构化输出通过 SSE 事件返回：

```
data: {"type":"session","session_id":"af90398c-a87b-43aa-9794-0ffa216cf0ef"}
data: {"type":"tool_use","id":"toolu_xxx","name":"StructuredOutput","input":{...}}
data: {"type":"structured_output","data":{"intent":"询价","sender":"zhangsan@example.com",...}}
data: {"type":"done","usage":{"input_tokens":4,"output_tokens":556}}
data: [DONE]
```

**新增事件类型**

| 事件类型 | 说明 |
|----------|------|
| structured_output | 包含完整的结构化输出对象，`data` 字段为符合 Schema 的 JSON |

### curl 示例

```bash
curl -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "分析这封邮件的意图：你好，我们想采购100台服务器，请提供报价。",
    "stream": false,
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "email_analysis",
        "schema": {
          "type": "object",
          "properties": {
            "intent": { "type": "string" },
            "key_info": {
              "type": "object",
              "properties": {
                "product": { "type": "string" },
                "quantity": { "type": "number" }
              },
              "required": ["product", "quantity"]
            },
            "urgency": {
              "type": "string",
              "enum": ["low", "medium", "high"]
            }
          },
          "required": ["intent", "key_info", "urgency"]
        }
      }
    }
  }'
```

### JSON Schema 编写指南

- **必填字段**：使用 `required` 数组声明必须返回的字段
- **枚举值**：使用 `enum` 限制字段取值范围
- **嵌套对象**：支持多层嵌套的 `object` 类型
- **数组**：使用 `array` + `items` 定义列表字段
- **类型**：支持 `string`、`number`、`boolean`、`object`、`array`
- **描述**：使用 `description` 字段帮助 Agent 理解每个字段的含义

---

## 外部工具调用

外部工具允许客户端在对话过程中为 Agent 动态注册自定义工具。当 Agent 决定调用这些工具时，会通过 `external_tool_call` 事件通知客户端执行，客户端完成执行后将结果回传给 Agent 继续处理。

> **适用场景**：Agent 需要访问客户端本地资源（数据库查询、内部 API 调用、设备操作等），而这些能力无法在服务端预配置。

### 工作流程

```
1. 客户端发送 chat 请求时通过 tools 参数注册外部工具
2. Agent 在对话中决定调用外部工具 → 发送 external_tool_call 事件
3. 客户端执行工具逻辑 → 通过 POST /sessions/:id/tool-result 回传结果
4. Agent 收到结果后继续生成回复
```

### 工具定义格式

通过 `tools` 参数传入的每个工具定义：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| name | string | 是 | 工具名称（1-64 字符） |
| description | string | 是 | 工具描述，帮助 Agent 理解何时使用（1-2048 字符） |
| inputSchema | object | 否 | JSON Schema properties 对象，定义工具的输入参数 |

**工具定义示例**

```json
{
  "tools": [
    {
      "name": "query_database",
      "description": "查询业务数据库中的客户信息",
      "inputSchema": {
        "customer_id": { "type": "string", "description": "客户 ID" },
        "fields": { "type": "array", "items": { "type": "string" }, "description": "需要查询的字段列表" }
      }
    },
    {
      "name": "send_notification",
      "description": "向指定用户发送通知消息",
      "inputSchema": {
        "user_id": { "type": "string" },
        "message": { "type": "string" },
        "channel": { "type": "string", "enum": ["email", "sms", "push"] }
      }
    }
  ]
}
```

### 提交工具执行结果

```
POST /api/v1/open/sessions/:id/tool-result
```

**路径参数**

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | 是 | 会话 ID（UUID） |

**请求体**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| request_id | string | 是 | `external_tool_call` 事件中的 `request_id` |
| result | string | 是 | 工具执行结果（文本） |
| is_error | boolean | 否 | 执行是否出错，默认 `false` |

**响应**

```json
{ "success": true }
```

重复提交同一 `request_id` 返回 `{ "success": false, "error": "External tool call not found or already responded" }`。

### 动态更新工具列表

在会话进行中动态添加、替换或移除外部工具。

```
PUT /api/v1/open/sessions/:id/tools
```

**请求体**

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| tools | array | 是 | 新的工具定义列表（最多 50 个）。传空数组 `[]` 移除所有外部工具 |

**响应**

```json
{ "success": true }
```

> 更新在 Agent 下一轮对话时生效。

### 查询待处理的工具调用

SSE 客户端断线重连后，可通过此端点恢复尚未完成的工具调用。

```
GET /api/v1/open/sessions/:id/pending-tool-calls
```

**响应**

```json
{
  "success": true,
  "data": [
    {
      "request_id": "req-abc123",
      "tool_name": "query_database",
      "tool_input": { "customer_id": "C001" },
      "remaining_timeout": 25000
    }
  ]
}
```

### 完整交互示例

```bash
# 1. 发起带外部工具的流式对话
curl -N -X POST https://agentforce.item.pub/api/v1/open/agents/AGENT_ID/chat \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "帮我查一下客户 C001 的信息",
    "stream": true,
    "tools": [
      {
        "name": "query_database",
        "description": "查询业务数据库中的客户信息",
        "inputSchema": {
          "customer_id": { "type": "string" }
        }
      }
    ]
  }'

# SSE 流中会收到:
# data: {"type":"session","session_id":"SESSION_ID"}
# data: {"type":"text","content":"好的，我来查询客户信息..."}
# data: {"type":"external_tool_call","request_id":"req-001","tool_name":"query_database","tool_input":{"customer_id":"C001"},"timeout":30000}

# 2. 客户端执行工具后回传结果（需在 30 秒内）
curl -X POST https://agentforce.item.pub/api/v1/open/sessions/SESSION_ID/tool-result \
  -H "Authorization: Bearer laf_your_api_key_here" \
  -H "Content-Type: application/json" \
  -d '{
    "request_id": "req-001",
    "result": "客户 C001: 张三, VIP 等级, 注册于 2024-01-15"
  }'

# SSE 流继续:
# data: {"type":"text","content":"查询到客户 C001 的信息：张三，VIP 等级..."}
# data: {"type":"done","usage":{"input_tokens":200,"output_tokens":60}}
# data: [DONE]
```

### 注意事项

- **仅流式模式**：外部工具仅在 `stream: true` 时可用，非流式模式不支持
- **互斥**：`tools` 和 `response_format` 不可同时使用
- **超时**：工具调用默认 30 秒超时，超时后 Agent 收到超时错误并继续处理
- **幂等**：同一 `request_id` 重复提交结果会返回 `success: false`，不会重复执行
- **数量限制**：单次最多注册 50 个外部工具

---

## WebSocket 对话

通过 WebSocket 进行实时双向对话，适用于需要持续交互的场景。

```
WebSocket: wss://agentforce.item.pub/ws/open/chat?api_key=laf_xxx
```

**连接参数**

| 参数 | 位置 | 必填 | 说明 |
|------|------|------|------|
| api_key | Query | 是 | API Key（`laf_xxx` 格式） |

连接时通过 query 参数传递 API Key 进行认证。认证失败返回 HTTP 401。

### 客户端消息（Client → Server）

所有消息为 JSON 对象，通过 `type` 字段区分。

#### init — 初始化会话（连接后必须首先发送）

```json
{
  "type": "init",
  "agent_id": "83e9af68-e385-4f50-8574-06aa61c11566",
  "session_id": "可选，传入以继续已有会话",
  "env": { "MY_VAR": "value" },
  "tools": [{ "name": "my_tool", "description": "工具描述", "inputSchema": { "param": { "type": "string" } } }]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 固定值 `"init"` |
| agent_id | string | 是 | Agent ID（UUID） |
| session_id | string | 否 | 已有会话 ID，省略则创建新会话 |
| env | object | 否 | Session 级环境变量覆盖（仅创建新会话时生效），规则同 REST API |
| tools | array | 否 | 外部工具定义列表（最多 50 个），格式同 REST API 的 `tools` 参数 |

#### message — 发送消息

```json
{
  "type": "message",
  "content": "你好",
  "attachments": [
    {
      "filename": "image.png",
      "data": "base64编码数据...",
      "content_type": "image/png"
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 固定值 `"message"` |
| content | string | 是 | 消息内容（最少 1 字符） |
| attachments | array | 否 | 文件附件，最多 10 个，格式同 REST API |

#### update_tools — 动态更新外部工具列表

```json
{
  "type": "update_tools",
  "tools": [
    {
      "name": "search_docs",
      "description": "搜索内部文档",
      "inputSchema": { "query": { "type": "string" } }
    }
  ]
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 固定值 `"update_tools"` |
| tools | array | 是 | 新的工具定义列表（最多 50 个）。传空数组移除所有工具 |

服务端确认后返回 `tools_updated` 消息。

#### external_tool_result — 提交外部工具执行结果

```json
{
  "type": "external_tool_result",
  "request_id": "req-abc123",
  "result": "查询结果...",
  "is_error": false
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| type | string | 是 | 固定值 `"external_tool_result"` |
| request_id | string | 是 | `external_tool_call` 中的 `request_id` |
| result | string | 是 | 工具执行结果 |
| is_error | boolean | 否 | 是否执行出错，默认 `false` |

#### stop — 中断当前回复

```json
{ "type": "stop" }
```

#### ping — 心跳

```json
{ "type": "ping" }
```

### 服务端消息（Server → Client）

#### connected — 会话已建立（响应 init）

```json
{ "type": "connected", "session_id": "96de3d24-c6eb-40aa-9ec7-1d760b5ce532" }
```

#### text — 文本内容

```json
{ "type": "text", "content": "你好！" }
```

#### thinking — 思考过程

```json
{ "type": "thinking", "content": "让我想想..." }
```

#### tool_use — 工具调用

```json
{
  "type": "tool_use",
  "id": "tooluse_abc123",
  "name": "search",
  "input": { "query": "相关信息" }
}
```

#### tool_result — 工具执行结果

```json
{
  "type": "tool_result",
  "tool_use_id": "tooluse_abc123",
  "content": "搜索结果...",
  "is_error": false
}
```

#### external_tool_call — 外部工具调用（需客户端执行并返回结果）

```json
{
  "type": "external_tool_call",
  "request_id": "req-abc123",
  "tool_name": "query_database",
  "tool_input": { "customer_id": "C001" },
  "timeout": 30000
}
```

客户端收到后需执行对应工具，并通过 `external_tool_result` 消息回传结果。超时（默认 30 秒）未响应则 Agent 收到超时错误。

#### tools_updated — 工具更新确认（响应 update_tools）

```json
{
  "type": "tools_updated",
  "success": true,
  "message": "Tools updated successfully"
}
```

#### done — 回复完成

```json
{
  "type": "done",
  "usage": {
    "input_tokens": 150,
    "output_tokens": 80
  }
}
```

#### error — 错误

```json
{ "type": "error", "message": "处理请求时出错" }
```

#### pong — 心跳响应

```json
{ "type": "pong" }
```

### 心跳机制

服务端每 30 秒发送 ping，客户端需回复 pong。未响应的连接将被自动断开。

### WebSocket 使用示例（JavaScript）

```javascript
const ws = new WebSocket('wss://agentforce.item.pub/ws/open/chat?api_key=laf_your_api_key_here');

ws.onopen = () => {
  // 1. 初始化会话
  ws.send(JSON.stringify({
    type: 'init',
    agent_id: 'AGENT_ID'
  }));
};

ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);

  switch (msg.type) {
    case 'connected':
      console.log('会话已建立:', msg.session_id);
      // 2. 发送消息
      ws.send(JSON.stringify({
        type: 'message',
        content: '你好'
      }));
      break;

    case 'text':
      process.stdout.write(msg.content);
      break;

    case 'thinking':
      console.log('[思考]', msg.content);
      break;

    case 'tool_use':
      console.log('[工具调用]', msg.name, msg.input);
      break;

    case 'tool_result':
      console.log('[工具结果]', msg.content);
      break;

    case 'external_tool_call':
      console.log('[外部工具调用]', msg.tool_name, msg.tool_input);
      // 执行工具逻辑后回传结果
      const result = await executeMyTool(msg.tool_name, msg.tool_input);
      ws.send(JSON.stringify({
        type: 'external_tool_result',
        request_id: msg.request_id,
        result: JSON.stringify(result),
        is_error: false
      }));
      break;

    case 'tools_updated':
      console.log('[工具更新]', msg.success, msg.message);
      break;

    case 'done':
      console.log('\n[完成]', msg.usage);
      break;

    case 'error':
      console.error('[错误]', msg.message);
      break;

    case 'pong':
      break; // 心跳响应
  }
};

// 心跳：响应服务端 ping
ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  if (msg.type === 'ping') {
    ws.send(JSON.stringify({ type: 'pong' }));
  }
  // ... 其他消息处理
};
```

### WebSocket 使用示例（Python）

```python
import json
import websocket

def on_message(ws, message):
    msg = json.loads(message)

    if msg['type'] == 'connected':
        print(f"会话已建立: {msg['session_id']}")
        ws.send(json.dumps({
            'type': 'message',
            'content': '你好'
        }))

    elif msg['type'] == 'text':
        print(msg['content'], end='', flush=True)

    elif msg['type'] == 'thinking':
        print(f"[思考] {msg['content']}")

    elif msg['type'] == 'external_tool_call':
        print(f"[外部工具调用] {msg['tool_name']}")
        # 执行工具逻辑后回传结果
        result = execute_my_tool(msg['tool_name'], msg['tool_input'])
        ws.send(json.dumps({
            'type': 'external_tool_result',
            'request_id': msg['request_id'],
            'result': json.dumps(result),
            'is_error': False
        }))

    elif msg['type'] == 'tools_updated':
        print(f"[工具更新] {msg['success']}")

    elif msg['type'] == 'done':
        print(f"\n[完成] {msg['usage']}")

    elif msg['type'] == 'error':
        print(f"[错误] {msg['message']}")

ws = websocket.WebSocketApp(
    'wss://agentforce.item.pub/ws/open/chat?api_key=laf_your_api_key_here',
    on_open=lambda ws: ws.send(json.dumps({
        'type': 'init',
        'agent_id': 'AGENT_ID'
    })),
    on_message=on_message,
)

ws.run_forever()
```

---

## 会话消息历史

查询指定会话的消息记录。

```
GET /api/v1/open/sessions/:id/messages
```

**路径参数**

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| id | string | 是 | 会话 ID（UUID），从对话响应中获取 |

**响应示例**

```json
{
  "success": true,
  "data": [
    {
      "id": "msg-001",
      "role": "user",
      "content": "你好",
      "timestamp": "2026-03-29T10:00:00.000Z"
    },
    {
      "id": "msg-002",
      "role": "assistant",
      "content": "你好！有什么可以帮你的？",
      "timestamp": "2026-03-29T10:00:01.500Z"
    }
  ]
}
```

**响应字段**

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | 消息 ID |
| role | string | 消息角色：`user` 或 `assistant` |
| content | string | 消息内容 |
| timestamp | string | ISO 8601 时间戳 |

消息按时间升序排列。

**错误响应**

| 状态码 | 说明 |
|--------|------|
| 404 | 会话不存在或不属于当前组织 |

**curl 示例**

```bash
curl https://agentforce.item.pub/api/v1/open/sessions/SESSION_ID/messages \
  -H "Authorization: Bearer laf_your_api_key_here"
```

---

## 错误处理

### HTTP 状态码

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 资源创建成功 |
| 400 | 请求参数错误 |
| 401 | 认证失败（API Key 缺失、无效或已过期） |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
| 503 | 服务不可用 |

### 错误响应格式

```json
{
  "success": false,
  "error": "错误描述信息"
}
```

### SSE 流中的错误

如果在 SSE 流式传输过程中发生错误，会通过 SSE 事件发送：

```
data: {"type":"error","message":"处理请求时出错"}

data: [DONE]
```

### WebSocket 错误

WebSocket 连接中的错误通过 `error` 类型消息发送：

```json
{ "type": "error", "message": "错误描述" }
```

### 常见错误场景

| 场景 | 状态码 | 错误信息 |
|------|--------|---------|
| 未提供 API Key | 401 | Missing API key |
| API Key 无效 | 401 | Invalid or expired API key |
| API Key 已吊销 | 401 | Invalid or expired API key |
| Agent 不存在 | 404 | Agent not found |
| 会话不存在 | 404 | Session not found |
| 请求体缺少 message | 400 | message is required and must be a string |
| 缺少组织上下文 | 400 | Organization context required |
