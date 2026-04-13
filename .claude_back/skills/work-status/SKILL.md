---
name: work-status
description: "工作状态知识，用于个人、团队和部门的工单统计与趋势查询。"
user-invocable: false
---

# 工作状态领域知识

这个 skill 只提供查询类业务知识。

## 查询范围

- `CSR`：个人
- `TeamLeader`：个人 + 团队
- `DeptManager`：个人 + 部门
- `Admin`：全局

## 常见意图

### 1. 个人状态

- 意图关键词：我的工作状态、我今天的情况、我的工单统计
- API 查找种子：`staff work status`
- 默认时间：今天

### 2. 按状态列出工单

- 意图关键词：我的待处理工单、我的 Open 工单、有哪些未解决的
- API 查找种子：`tickets page`
- 常见过滤：状态、处理人、日期范围

### 3. 团队或部门情况

- 意图关键词：团队情况、我们部门今天怎么样、团队工作状态
- API 查找种子：`staff work status`、`department count`
- 关键输入：部门范围、日期范围

### 4. 工作量排名

- 意图关键词：谁最忙、谁积压最多、工作量排名
- API 查找种子：`workload page`、`work status`
- 常见排序：未处理数量降序

### 5. 仪表盘统计

- 意图关键词：工单统计、仪表盘、趋势、活动统计、平均解决时间、SLA 达成率
- API 查找种子：`dashboard ticket count`、`trend`、`activity stats`、`average resolution time`、`sla achieved`

## 默认行为

- 用户没给时间范围时，个人状态默认今天，趋势默认最近 7 天
- 用户范围超权时，主 agent 应收缩到其可见范围，而不是直接失败
