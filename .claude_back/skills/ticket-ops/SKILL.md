---
name: ticket-ops
description: "工单处理知识，用于回复、备注、状态流转、分派和工单查询。"
user-invocable: false
---

# 工单处理领域知识

这个 skill 只提供业务知识，不负责编排。

## 访问边界

- `CSR`：仅自己的工单
- `TeamLeader`：团队范围
- `DeptManager`：部门范围
- `Admin`：可跨范围

## 常见意图

### 1. 回复与备注

- 意图关键词：回复、回复客户、内部备注、加备注
- API 查找种子：`reply ticket`、`internal note`、`timeline`
- 关键输入：工单、消息内容、必要时消息节点
- 备注前常需要先查时间线拿最新消息节点

### 2. 状态与分派

- 意图关键词：改状态、设为处理中、关闭工单、转给某人、转到部门、handover
- API 查找种子：`bulk status`、`bulk staff`、`department transfer`、`handover`
- 关键输入：工单、目标状态、目标人员或部门
- 高风险：关闭工单、转派、批量操作都应确认

### 3. 优先级、Topic、表单

- 意图关键词：改优先级、换主题、更新表单字段
- API 查找种子：`ticket priorities options`、`topics page`、`form entries`
- 常见辅助查询：优先级选项、Topic 列表、当前表单结构

### 4. 查询与定位

- 意图关键词：查看工单、工单详情、时间线、我的工单、查找工单
- API 查找种子：`ticket detail`、`ticket brief`、`ticket timeline`、`tickets page`
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
