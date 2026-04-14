---
name: ticket-ops
description: "工单处理知识，用于回复、备注、状态流转、分派和工单查询。"
user-invocable: false
---

# 工单处理

提供工单处理相关的业务知识和 API playbook。
适用于回复、备注、状态流转、分派和工单查询，不负责编排或执行。

## 访问边界

- `CSR`：仅自己的工单
- `TeamLeader`：团队范围
- `DeptManager`：部门范围
- `Admin`：可跨范围

## 常见意图

### 1. 回复与备注

- 意图关键词：回复、回复客户、内部备注、加备注
- 主 API：
  - `POST /v1/staff/tickets/{id}/reply`
  - `PUT /v1/staff/tickets/{ticketId}/messages/{messageId}/internal-note`
  - `POST /v1/staff/tickets/{ticketId}/timeline`
- 关键输入：工单、消息内容、必要时消息节点
- 备注前常需要先查时间线拿最新消息节点

### 2. 状态与分派

- 意图关键词：改状态、设为处理中、关闭工单、转给某人、转到部门、handover
- 主 API：
  - `PUT /v1/staff/tickets/bulk/status`
  - `PUT /v1/staff/tickets/bulk/staff`
  - `PUT /v1/staff/tickets/bulk/team`
  - `PUT /v1/staff/tickets/bulk/department`
  - `PUT /v1/staff/tickets/{ticketId}/department`
  - `POST /v1/staff/tickets/{ticketId}/handover`
- 关键输入：工单、目标状态、目标人员或部门
- 高风险：关闭工单、转派、批量操作都应确认

### 3. 优先级、Topic、表单

- 意图关键词：改优先级、换主题、更新表单字段
- 主 API：
  - `PUT /v1/staff/tickets/{id}`
  - `PUT /v1/staff/tickets/{ticketId}/form-entries`
  - `GET /v1/staff/tickets/{ticketId}/form-entries/{topicId}`
- 常见辅助查询：
  - `POST /v1/staff/ticket/priorities/page`
  - `POST /v1/staff/ticket/priorities/options/batch`
  - `POST /v1/staff/topics/page`

### 4. 查询与定位

- 意图关键词：查看工单、工单详情、时间线、我的工单、查找工单
- 主 API：
  - `GET /v1/staff/tickets/{id}`
  - `GET /v1/staff/tickets/brief/{id}`
  - `GET /v1/staff/tickets/number/{code}`
  - `POST /v1/staff/tickets/page`
  - `POST /v1/staff/tickets/search`
  - `POST /v1/staff/tickets/{ticketId}/timeline`
  - `POST /v1/staff/tickets/number/{ticketNumber}/timeline`
- 工单可由 ID、编号或最近上下文定位

## 名称解析偏好

- 人员名称 -> 员工搜索
- 部门名称 -> 部门搜索
- Topic 名称 -> Topic 搜索
- “这个工单” -> 最近工单上下文

## 复合动作提示

- “回复并设为处理中” -> 先回复，再改状态
- “转给张三并备注已转交” -> 先解析张三，再转派，再加备注
- “关闭工单并说明原因” -> 先确认关闭，再补备注或说明，再执行关闭

## 兜底规则

- 回复、备注、状态流转、分派、详情、时间线优先使用这里列出的主 API
- 如果只是缺人员、部门、Topic、优先级 ID，优先用这里列出的 page / options 接口解析
- 只有遇到宏、升级、提醒、打印、平行工单等低频能力时，再调用 `findapiagent`
