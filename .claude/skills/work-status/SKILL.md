---
name: work-status
description: "工作状态知识，用于个人、团队和部门的工单统计与趋势查询。"
user-invocable: false
---

# 工作状态

提供工作状态和统计查询相关的业务知识与 API playbook。
适用于个人、团队和部门的统计、排行与趋势类请求。

## 查询范围

- `CSR`：个人
- `TeamLeader`：个人 + 团队
- `DeptManager`：个人 + 部门
- `Admin`：全局

## 常见意图

### 1. 个人状态

- 意图关键词：我的工作状态、我今天的情况、我的工单统计
- 主 API：
  - `POST /v1/staff/report/staff/work-status`
- 默认时间：今天

### 2. 按状态列出工单

- 意图关键词：我的待处理工单、我的 Open 工单、有哪些未解决的
- 主 API：
  - `POST /v1/staff/tickets/page`
- 常见过滤：状态、处理人、日期范围

### 3. 团队或部门情况

- 意图关键词：团队情况、我们部门今天怎么样、团队工作状态
- 主 API：
  - `POST /v1/staff/report/staff/work-status`
  - `POST /v1/staff/dashboard/ticket/department-count`
  - `POST /v1/staff/dashboard/staff/department-count`
- 关键输入：部门范围、日期范围

### 4. 工作量排名

- 意图关键词：谁最忙、谁积压最多、工作量排名
- 主 API：
  - `POST /v1/staff/auto-assign/workload/page`
  - `POST /v1/staff/report/staff/work-status`
- 常见排序：未处理数量降序

### 5. 仪表盘统计

- 意图关键词：工单统计、仪表盘、趋势、活动统计、平均解决时间、SLA 达成率
- 主 API：
  - `POST /v1/staff/dashboard/ticket/count-stats`
  - `POST /v1/staff/dashboard/ticket/trend`
  - `POST /v1/staff/dashboard/ticket/activity-stats`
  - `POST /v1/staff/dashboard/ticket/average-resolution-time`
  - `POST /v1/staff/dashboard/ticket/sla-achieved`

## 默认行为

- 用户没给时间范围时，个人状态默认今天，趋势默认最近 7 天
- 用户范围超权时，主 agent 应收缩到其可见范围，而不是直接失败
- “我的””我自己””当前登录员工”的范围优先由主 agent 通过 `GET /v1/staff/auth/current` 固化，不需要额外检索

## 兜底规则

- 个人状态、团队状态、工作量、仪表盘统计优先使用这里列出的报表 API
- 如果只是缺某个筛选条件枚举或更细的统计维度，再调用 `api-executor-agent`（schema_lookup 模式）
