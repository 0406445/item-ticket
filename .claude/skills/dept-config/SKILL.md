---
name: dept-config
description: "部门配置领域知识：部门设置、负责人管理、邮箱配置、Atlas AI 绑定。DeptManager/Admin 可用。"
user-invocable: false
---

# 部门配置管理

当需要查看或修改部门配置（负责人、邮箱、Atlas AI 绑定等）时，参考本领域知识。

执行流程：通过 @findapiagent 查找 API → @api-validator 校验参数 → /api-executor 执行请求。

## 权限边界

- **DeptManager**：只能查看和修改自己所在部门的配置
- **Admin**：可查看和修改所有部门的配置
- **CSR / TeamLeader**：无权执行部门配置操作

跨部门操作时，如果当前用户不是 Admin，必须拒绝并提示："跨部门配置修改需要管理员权限。"

## 操作清单

### 1. 查询部门当前配置

- **用户意图关键词**：部门配置、部门信息、部门详情、我的部门设置
- **API**：GET /v1/staff/departments/{id} [staff]
- **参数**：部门 ID（默认为用户所在部门）
- **结果展示**：用自然语言描述部门的关键配置信息
  ```
  你的部门「技术部」当前配置：
  - 负责人：张三
  - 绑定邮箱：tech@company.com
  - Atlas AI：已开启
  - 部门描述：负责技术支持和系统维护
  ```

### 2. 更新部门负责人

- **用户意图关键词**：换负责人、改部门经理、设置负责人
- **需要的信息**：目标负责人（姓名或 ID）+ 部门（默认为用户所在部门）
- **API**：PUT /v1/staff/departments/{id} [staff]（更新 managerId 字段）
- **名称解析**：如果用户提供姓名，先通过 POST /v1/staff/staff/page [staff] 搜索解析为员工 ID
- **执行**：通过 @findapiagent 查找更新部门 API，填充 departmentId 和 managerId 参数后执行
- **HR 组织管理者关联**：
  - 查询当前管理者关系：POST /v1/staff/hr-org-managers/list [staff]
  - 创建管理者关系：POST /v1/staff/hr-org-managers [staff]
  - 更新管理者关系：PUT /v1/staff/hr-org-managers/{id} [staff]

### 3. 更换部门绑定邮箱

- **用户意图关键词**：换邮箱、修改部门邮箱、绑定新邮箱
- **需要的信息**：新邮箱地址 + 部门（默认为用户所在部门）
- **⚠️ 不可逆操作**：执行前必须请求用户确认
  - 确认格式："即将把部门绑定邮箱从 [旧邮箱] 更换为 [新邮箱]，确认吗？"
- **查询当前邮箱配置**：POST /v1/staff/emails/page [staff]（按部门筛选）
- **创建邮箱配置**：POST /v1/staff/emails [staff]
- **更新邮箱配置**：PUT /v1/staff/emails/{id} [staff]
- **说明**：先查询当前部门的邮箱配置，如果已有则更新，如果没有则创建

### 4. 开启/关闭 Atlas AI 绑定

- **用户意图关键词**：开启 Atlas、关闭 Atlas、AI 绑定、Atlas AI
- **需要的信息**：开启或关闭 + 部门（默认为用户所在部门）
- **API**：PUT /v1/staff/departments/{id} [staff]（更新 aiAgentId 字段）
- **开启 Atlas**：
  1. 先查询可用的 AI Agent 列表：POST /v1/staff/ai/agents/page [staff]
  2. 获取 Atlas 的 agent ID
  3. 更新部门的 aiAgentId 为该 ID
- **关闭 Atlas**：将部门的 aiAgentId 设为 null
- **执行**：
  - 开启：通过 @findapiagent 查找更新部门 API，将 aiAgentId 设为对应 agent ID
  - 关闭：通过 @findapiagent 查找更新部门 API，将 aiAgentId 设为空

### 5. 查询部门列表

- **用户意图关键词**：有哪些部门、部门列表、所有部门
- **API**：POST /v1/staff/departments/page [staff]
- **结果展示**：
  ```
  当前系统有以下部门：
  1. 技术部 — 负责人：张三 — 成员 12 人
  2. 运营部 — 负责人：李四 — 成员 8 人
  3. 财务部 — 负责人：王五 — 成员 5 人
  ```

### 6. 更新部门基本信息

- **用户意图关键词**：改部门名称、更新部门描述、修改部门编码
- **API**：PUT /v1/staff/departments/{id} [staff]
- **可更新的信息**：部门名称、部门描述、部门编码、上级部门、关联 SLA

### 7. 查询部门排班

- **用户意图关键词**：排班、工作时间、部门排班表
- **查询排班**：GET /v1/open/departments/{id}/schedule [open]
- **查询排班条目**：GET /v1/staff/schedules/{scheduleId}/entries [staff]

## 常见复合操作

| 用户说 | 分解步骤 |
|--------|---------|
| "把负责人改成 Ethan，顺便开启 Atlas" | 1. 解析 Ethan → 2. 更新负责人 → 3. 查询 AI Agent → 4. 绑定 Atlas |
| "看看部门配置，然后换个邮箱" | 1. 查询部门配置 → 2. 用户提供新邮箱 → 3. 确认后更新 |
