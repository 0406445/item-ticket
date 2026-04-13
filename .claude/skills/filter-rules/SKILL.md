---
name: filter-rules
description: "工单筛选规则管理领域知识（暂未在引导助手中开放）。"
user-invocable: false
---

# 工单筛选规则管理（暂未开放）

此功能的 API 已就绪，但尚未在引导助手中开放。

## 已确认可用的 API

| 操作 | API | 来源 |
|------|-----|------|
| 创建筛选规则组 | POST /v1/staff/ticket/filter-group | staff |
| 更新筛选规则组 | PUT /v1/staff/ticket/filter-group | staff |
| 删除筛选规则组 | DELETE /v1/staff/ticket/filter-group/{id} | staff |
| 查询筛选规则组列表 | POST /v1/staff/ticket/filter-group/page | staff |
| 查询筛选规则组详情 | GET /v1/staff/ticket/filter-group/{id} | staff |
| 查询可用筛选字段 | GET /v1/staff/ticket/filter/fields | staff |

## 支持的筛选条件

- 工单状态（status）
- 优先级（priority）
- 部门（department）
- 日期范围（date range）
- 工单主题（topic）

## 当用户请求此功能时

回复用户："筛选规则功能正在开发中，预计后续版本开放。目前你可以通过描述条件让我帮你查询工单。"

## 权限要求

- DeptManager：可管理自己部门的筛选规则
- Admin：可管理所有部门的筛选规则
