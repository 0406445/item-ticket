---
name: agentforce-ops
description: "AgentForce Agent 管理知识，用于创建、更新、删除、查询和配置 Agent。"
user-invocable: false
---

# AgentForce Agent 管理

提供 AgentForce 平台 Agent 管理相关的业务知识和 API 操作指引。
适用于创建 Agent、更新 Agent 配置、删除 Agent、查询 Agent 列表/详情、管理 Agent 会话等操作。

## 认证配置

所有配置从 `.claude/agentforce-config.json` 读取：

```json
{
  "baseUrl": "https://agentforce.item.pub/api/v1",
  "authBaseUrl": "https://agentforce.item.pub/api/auth",
  "authorization": "Bearer your-session-token-here",
  "x-organization-id": "your-organization-id-here",
  "agents": {
    "onboarding-agent": "agent-uuid-here",
    "findapiagent": "agent-uuid-here",
    "api-validator": "agent-uuid-here",
    "api-executor-agent": "agent-uuid-here"
  },
  "skills": {
    "skill-name": "registry-{registryId}-{skillName}"
  }
}
```

- `baseUrl`：业务 API 前缀（/users/agents 等）
- `authBaseUrl`：认证相关 API 前缀（/organization/list 等）
- `authorization`：Bearer token，来自 `better-auth.session_token`
- `x-organization-id`：组织 ID
- `agents`：已创建的 Agent 名称到 ID 的映射，操作特定 Agent 时从此处读取 ID
- `skills`：Skill 名称到 Skill Registry ID 的映射，格式为 `registry-{registryId}-{skillName}`

如果配置文件不存在或缺少任何字段，必须停止执行并提示用户补充配置。

### Agent ID 读取规则

当需要操作某个 Agent（更新、删除、查详情等）时：
1. 先从 `.claude/agentforce-config.json` 的 `agents` 字段按名称查找 ID
2. 如果配置中没有该名称，再调用 `GET /users/agents` 列表接口按名称匹配
3. 创建新 Agent 后，必须将返回的 `id` 写回配置文件的 `agents` 字段
4. 删除 Agent 后，必须从配置文件的 `agents` 字段移除对应条目

## 请求规范

### 基础请求头

所有请求必须包含：
- `Accept: */*`
- `Authorization: {从配置读取，含 Bearer 前缀}`
- `Content-Type: application/json`（POST/PATCH/DELETE 请求时）
- `x-organization-id: {从配置读取}`（业务 API 需要，auth API 不需要）

### curl 规则

- 加 `-s` 静默模式
- 加 `-w '\n%{http_code}'` 获取 HTTP 状态码
- JSON body 用 `--data-raw`
- baseUrl 必须从配置文件读取，禁止硬编码

## API 接口

### 0. 查询组织列表

- 方法：`GET`
- 基础路径：`{authBaseUrl}/organization/list`（注意用 authBaseUrl，不是 baseUrl）
- 请求头：只需 `Authorization`，不需要 `x-organization-id`
- 响应：组织数组

### 1. 创建 Agent

- 方法：`POST`
- 路径：`/users/agents`
- 最小必填 body：

```json
{
  "name": "Agent 名称",
  "description": "Agent 描述"
}
```

- 响应：返回完整 Agent 对象，包含系统分配的 `id`

### 2. 更新 Agent

- 方法：`PATCH`
- 路径：`/users/agents/{agentId}`
- body 为完整配置（全量更新），可配置字段：

```json
{
  "name": "Agent 名称",
  "description": "Agent 描述",
  "systemPrompt": "系统提示词",
  "modelProviderId": "模型提供商 ID",
  "modelId": "模型 ID",
  "fastModelProviderId": null,
  "fastModelId": null,
  "effort": "medium",
  "permissionMode": "bypassPermissions",
  "maxTurns": 50,
  "networkEnabled": true,
  "sandboxEnabled": false,
  "imageGenEnabled": true,
  "fileShareEnabled": true,
  "taskToolEnabled": true,
  "teamEnabled": false,
  "scheduledTaskEnabled": true,
  "skillManagementEnabled": true,
  "containerSandboxEnabled": false,
  "browserProfileId": null,
  "gitRepo": null,
  "skillIds": null,
  "pluginIds": null,
  "knowledgeBaseIds": null,
  "mcpServers": null,
  "envVars": null,
  "subagents": null,
  "sessionPolicy": null
}
```

- 更新前建议先 GET 当前配置，在现有基础上修改，避免覆盖丢失

### 3. 删除 Agent

- 方法：`DELETE`
- 路径：`/users/agents/{agentId}`
- 无 body
- 高风险操作，执行前必须确认
- 响应：成功返回 `{ "success": true }`

### 4. 查询 Agent 列表

- 方法：`GET`
- 路径：`/users/agents`
- 响应：Agent 数组，每个包含 `_count.sessions`、`sessionCount`、`channels` 等额外字段

### 5. 查询 Agent 详情

- 方法：`GET`
- 路径：`/users/agents/{agentId}`
- 响应：完整 Agent 对象，含 `channels` 字段

### 6. 查询 Agent 会话列表

- 方法：`GET`
- 路径：`/users/agents/{agentId}/sessions`
- 响应：会话数组

### 7. 查询可用模型

- 方法：`GET`
- 路径：`/users/models`
- 响应：按 provider 分组的模型列表，每个模型含 `id`、`name`、`contextLength`

### 8. 查询可用 Skills

- 方法：`GET`
- 路径：`/users/skills`
- 响应：Skill 数组，每个含 `id`、`name`、`type`、`description`

### 9. 查询可用 Plugins

- 方法：`GET`
- 路径：`/users/plugins`
- 响应：Plugin 数组，每个含 `marketplaceId`、`name`、`description`

### 10. 查询 Skill Registries

- 方法：`GET`
- 路径：`/users/skill-registries`
- 响应：Registry 数组，含 `id`、`name`、`url`、`branch`

### 11. 查询 Knowledge Bases

- 方法：`GET`
- 路径：`/users/knowledge-bases`
- 响应：Knowledge Base 数组

### 12. 查询 Browser Profiles

- 方法：`GET`
- 路径：`/users/browser-profiles`
- 响应：Browser Profile 数组

### 13. 同步 Skill Registry

- 方法：`POST`
- 路径：`/users/skill-registries/{registryId}/sync`
- 无 body
- 用途：触发 Skill Registry 从 Git 仓库拉取最新 skill 定义并同步到平台
- 响应：同步结果对象
- 常见场景：推送 skill 文件修改到 Git 后，调用此接口刷新平台侧的 skill 内容

## Agent 数据结构

完整 Agent 对象字段说明：

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string(uuid) | Agent 唯一标识 |
| name | string | Agent 名称 |
| description | string | Agent 描述 |
| systemPrompt | string/null | 系统提示词 |
| modelProviderId | string(uuid) | 模型提供商 ID |
| modelId | string | 模型 ID |
| fastModelProviderId | string/null | 快速模型提供商 ID |
| fastModelId | string/null | 快速模型 ID |
| effort | string | 推理力度：low/medium/high |
| permissionMode | string | 权限模式 |
| maxTurns | number | 最大对话轮次 |
| networkEnabled | boolean | 是否启用网络 |
| sandboxEnabled | boolean | 是否启用沙箱 |
| imageGenEnabled | boolean | 是否启用图片生成 |
| fileShareEnabled | boolean | 是否启用文件共享 |
| taskToolEnabled | boolean | 是否启用任务工具 |
| teamEnabled | boolean | 是否启用团队 |
| scheduledTaskEnabled | boolean | 是否启用定时任务 |
| skillManagementEnabled | boolean | 是否启用技能管理 |
| containerSandboxEnabled | boolean | 是否启用容器沙箱 |
| gitRepo | string/null | Git 仓库地址 |
| mcpServers | object/null | MCP 服务器配置 |
| subagents | object/null | 子 Agent 配置 |
| envVars | object/null | 环境变量 |
| sessionPolicy | object/null | 会话策略 |
| skillIds | array/null | 关联的 Skill ID 列表 |
| pluginIds | array/null | 关联的 Plugin ID 列表 |
| knowledgeBaseIds | array/null | 关联的 Knowledge Base ID 列表 |
| browserProfileId | string/null | 浏览器配置 ID |
| configVersion | string | 配置版本号 |
| avatar | string/null | 头像（base64 编码图片） |

## 常见意图

### 创建 Agent
- 意图关键词：创建 agent、新建 agent、添加 agent
- 最少需要：name、description
- 创建后系统会分配默认模型和配置

### 更新 Agent 配置
- 意图关键词：修改 agent、更新配置、改名、改提示词、换模型
- 更新前先 GET 当前配置
- 修改目标字段后 PATCH 回去

### 删除 Agent
- 意图关键词：删除 agent、移除 agent
- 高风险操作，必须确认后执行
- 需要 agentId

### 查询 Agent
- 意图关键词：查看 agent、agent 列表、agent 详情
- 列表查询返回所有 agent
- 详情查询需要 agentId

### 配置模型
- 意图关键词：换模型、用什么模型、可用模型
- 先 GET /users/models 获取可用模型列表
- 更新时需同时设置 modelProviderId 和 modelId

### 同步 Skill Registry
- 意图关键词：同步 skill、刷新 skill、sync registry、推送 skill
- 从配置文件的 `skills` 字段提取 registryId（格式 `registry-{registryId}-{skillName}`，取中间部分）
- 调用 `POST /users/skill-registries/{registryId}/sync`
- 常用于 skill 文件修改提交到 Git 后刷新平台

## 执行流程

### 1. 读取认证配置

```bash
cat .claude/agentforce-config.json
```

验证 `baseUrl`、`authBaseUrl`、`authorization` 和 `x-organization-id` 都存在且非空。

### 2. 构造请求

- 业务 API：`{baseUrl}` 拼接路径，加 `Authorization` + `x-organization-id` 头
- 认证 API：`{authBaseUrl}` 拼接路径，只加 `Authorization` 头

### 3. 执行并校验

- HTTP 状态码校验（2xx 成功，401 认证失败，403 权限不足等）
- 业务状态校验（检查 `success` 字段）
- 返回结构化结果

## 注意事项

- 创建、更新、删除操作应先确认再执行
- Agent ID 为 UUID 格式
- 更新是全量更新，务必先查再改，避免丢失已有配置
- 敏感信息（token、密钥）不要原样回传
