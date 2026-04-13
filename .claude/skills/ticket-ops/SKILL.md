---
name: ticket-ops
description: "工单操作领域知识：回复、内部备注、状态变更、转派、优先级修改、Topic 变更、表单字段更新、工单详情查看。"
user-invocable: false
---

# 工单操作

当需要执行工单相关操作时，参考本领域知识确定操作类型和对应的 API。

执行流程：通过 @findapiagent 查找 API → @api-validator 校验参数 → /api-executor 执行请求。

## 操作清单

### 1. 回复工单

- **用户意图关键词**：回复、答复、回消息、回复客户
- **需要的信息**：工单 ID + 回复内容
- **API**：POST /v1/staff/tickets/{id}/reply [staff]
- **说明**：回复内容会发送给客户。如果用户没有指定工单 ID，从实体上下文栈获取。
- **执行**：通过 @findapiagent 查找回复工单 API，填充 ticketId 和 content 参数后执行

### 2. 添加内部备注

- **用户意图关键词**：备注、内部备注、笔记、内部留言
- **需要的信息**：工单 ID + 消息 ID + 备注内容
- **API**：PUT /v1/staff/tickets/{ticketId}/messages/{messageId}/internal-note [staff]
- **说明**：内部备注仅对 Staff 可见，不发送给客户。需要先获取工单的消息列表来确定 messageId。
- **注意**：如果用户只说"加个备注"，需要先通过工单时间线获取最新消息 ID。

### 3. 修改工单状态

- **用户意图关键词**：改状态、设为、标记为、Open/Pending/Resolved/Closed
- **需要的信息**：工单 ID + 目标状态
- **API**：PUT /v1/staff/tickets/bulk/status [staff]
- **可用状态值**：
  - Open（处理中）
  - Pending（等待中）
  - Resolved（已解决）
  - Closed（已关闭）
- **⚠️ 不可逆操作**：关闭工单（设为 Closed）前必须请求用户确认
- **执行**：通过 @findapiagent 查找批量更新工单状态 API，填充 ticketId 和 status 参数后执行

### 4. 转派工单给人员

- **用户意图关键词**：转给、分配给、指派给、交给
- **需要的信息**：工单 ID + 目标人员（姓名或 ID）
- **API**：PUT /v1/staff/tickets/bulk/staff [staff]
- **名称解析**：如果用户提供的是姓名，需要先通过 POST /v1/staff/staff/page [staff] 搜索解析为员工 ID
- **执行**：通过 @findapiagent 查找批量转派工单 API，填充 ticketId 和 staffId 参数后执行

### 5. 转派工单到部门

- **用户意图关键词**：转到部门、移交部门、转给XX部
- **需要的信息**：工单 ID + 目标部门（名称或 ID）
- **API**：PUT /v1/staff/tickets/{ticketId}/department [staff]
- **批量版本**：PUT /v1/staff/tickets/bulk/department [staff]
- **名称解析**：如果用户提供的是部门名称，需要先通过 POST /v1/staff/departments/page [staff] 搜索解析为部门 ID

### 6. 工单转接（Handover）

- **用户意图关键词**：转接、handover
- **需要的信息**：工单 ID
- **API**：POST /v1/staff/tickets/{ticketId}/handover [staff]

### 7. 修改优先级

- **用户意图关键词**：优先级、紧急、加急、改优先级
- **需要的信息**：工单 ID + 目标优先级
- **API**：PUT /v1/staff/tickets/{id} [staff]（更新 priority 相关字段）
- **获取可用优先级列表**：POST /v1/staff/ticket/priorities/options/batch [staff] 或 POST /v1/open/ticket/priorities/page [open]
- **说明**：先查询可用的优先级选项，让用户从中选择或自动匹配

### 8. 修改工单 Topic

- **用户意图关键词**：改主题、换 Topic、修改分类
- **需要的信息**：工单 ID + 目标 Topic（名称或 ID）
- **API**：PUT /v1/staff/tickets/{id} [staff]（更新 topic 相关字段）
- **获取可用 Topic 列表**：POST /v1/staff/topics/page [staff]
- **名称解析**：如果用户提供的是 Topic 名称，需要先搜索解析为 Topic ID

### 9. 更新表单字段

- **用户意图关键词**：表单、字段、填写、更新订单号、更新备注字段
- **需要的信息**：工单 ID + Topic ID + 字段值
- **查询当前表单**：GET /v1/staff/tickets/{ticketId}/form-entries/{topicId} [staff]
- **更新表单**：PUT /v1/staff/tickets/{ticketId}/form-entries [staff]
- **说明**：先查询当前表单结构和已有值，再更新指定字段

### 10. 查看工单详情

- **用户意图关键词**：查看工单信息
- **需要的信息**：工单 ID 或工单编号
- **按 ID 查询**：GET /v1/staff/tickets/{id} [staff]
- **按编号查询**：GET /v1/staff/tickets/number/{code} [staff]
- **简要信息**：GET /v1/staff/tickets/brief/{id} [staff]
- **结果展示**：用自然语言描述工单的关键信息（编号、主题、状态、优先级、处理人、客户、创建时间）

### 11. 查看工单时间线

- **用户意图关键词**：时间线、历史记录、操作记录、聊天记录
- **需要的信息**：工单 ID 或工单编号
- **按 ID**：POST /v1/staff/tickets/{ticketId}/timeline [staff]
- **按编号**：POST /v1/staff/tickets/number/{ticketNumber}/timeline [staff]

### 12. 查询工单列表

- **用户意图关键词**：我的工单、工单列表、查找工单
- **API**：POST /v1/staff/tickets/page [staff]
- **说明**：支持按状态、优先级、处理人等条件筛选

## 复合操作模式

常见的一句话多操作场景：

| 用户说 | 分解步骤 |
|--------|---------|
| "回复并设为处理中" | 1. 回复工单 → 2. 修改状态为 Open |
| "回复并改为 Pending" | 1. 回复工单 → 2. 修改状态为 Pending |
| "转给张三并加备注说已转交" | 1. 解析张三 → 2. 转派给张三 → 3. 添加内部备注 |
| "改优先级为紧急并回复客户" | 1. 修改优先级 → 2. 回复工单 |
| "关闭工单并备注原因" | 1. 确认关闭 → 2. 添加备注 → 3. 修改状态为 Closed |
| "转到技术部并改为处理中" | 1. 解析技术部 → 2. 转派到部门 → 3. 修改状态为 Open |
