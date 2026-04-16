---
name: ticket-ops
description: "工单处理知识，用于回复、备注、状态流转、分派和工单查询。"
user-invocable: false
---

# 工单处理

提供工单处理相关的业务知识和 API playbook。
适用于回复、备注、状态流转、分派和工单查询，不负责编排或执行。

## 与主 agent / 执行 agent 的协作契约

- 本 skill 只负责提供 API playbook、拆步规则、名称解析偏好和风险提示，不直接产生最终用户结论
- 主 agent 读取本 skill 后，必须先形成结构化 `execution_plan`，再交给 `api-executor-agent`
- 禁止只把“先查 A，再查 B”“帮我查一下人数”这类自然语言步骤直接转发给执行 agent
- 如果一个意图需要多步请求，必须展开为 `execution_plan.steps[]`
- 每个 `step` 至少包含：
  - `step_id`
  - `purpose`
  - `request_plan.method`
  - `request_plan.path`
  - `request_plan.source`
  - `request_plan.path_params`
  - `request_plan.query_params`
  - `request_plan.body`
  - `extract`
  - `checks`
- 名称转 ID、当前登录员工、分页统计、范围过滤都要在结构化计划里显式写出，不要让执行 agent 自行猜字段或猜统计口径
- skill 决定“该用什么 API、拆几步、先后顺序和默认策略”；最终数字、ID 和事实结论只能来自执行 trace

## 读操作统计规则

- 用户问“多少个”“总数”“成员数”“数量”时，主 agent 必须在 `extract` 里明确写出优先读取的统计字段
- 如果 page 接口同时返回 `total` 与列表字段，主 agent 应要求执行 agent 一并带回，方便上游验收
- 如果过滤条件存在多个近义字段，主 agent 必须先根据 skill、已知 schema 或 `findapiagent` 明确字段后再执行，不能把字段选择留给执行 agent 临场判断
- 执行结果里如果缺少可追溯证据路径，主 agent 只能回复“暂时无法确认”，不能输出精确数字

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
- “我的 Open 工单 / 我的待处理工单 / 我的工单” -> 先由主 agent 获取当前员工，再走 `POST /v1/staff/tickets/page`
- “我”“当前登录员工” -> `GET /v1/staff/auth/current`

## 复合动作提示

- “回复并设为处理中” -> 先回复，再改状态
- “转给张三并备注已转交” -> 先解析张三，再转派，再加备注
- “关闭工单并说明原因” -> 先确认关闭，再补备注或说明，再执行关闭

## 兜底规则

- 回复、备注、状态流转、分派、详情、时间线优先使用这里列出的主 API
- 如果只是缺人员、部门、Topic、优先级 ID，优先用这里列出的 page / options 接口解析
- 只有遇到宏、升级、提醒、打印、平行工单等低频能力时，再调用 `findapiagent`
