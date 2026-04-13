---
name: auto-assign
description: "自动分配规则管理领域知识（暂未在引导助手中开放）。"
user-invocable: false
---

# 自动分配规则管理（暂未开放）

此功能的 API 已就绪，但尚未在引导助手中开放。

## 已确认可用的 API

| 操作 | API | 来源 |
|------|-----|------|
| 创建规则 | POST /v1/staff/auto-assign/rule | staff |
| 更新规则 | PUT /v1/staff/auto-assign/rule | staff |
| 删除规则 | DELETE /v1/staff/auto-assign/rule/{id} | staff |
| 查询规则列表 | POST /v1/staff/auto-assign/rule/page | staff |
| 更新规则状态 | PUT /v1/staff/auto-assign/rule/status | staff |
| 查询员工工作量 | POST /v1/staff/auto-assign/workload/page | staff |
| 查询分配历史 | POST /v1/staff/auto-assign/history/page | staff |

## 支持的分配策略

- Round Robin（轮询分配）
- Workload（按工作量分配）
- 每人最大工单数量限制（limitNumber，0 表示不限制）

## 当用户请求此功能时

回复用户："自动分配规则功能正在开发中，预计后续版本开放。目前你可以手动转移工单给指定人员。"

## 权限要求

- TeamLeader：可管理自己部门的分配规则
- Admin：可管理所有部门的分配规则
