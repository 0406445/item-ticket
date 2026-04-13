---
name: work-status
description: "工作状态查询领域知识：个人/团队/部门工单统计、仪表盘数据、工作量排名。"
user-invocable: false
---

# 工作状态查询

当需要查询工作状态、工单统计、仪表盘数据时，参考本领域知识确定查询类型和对应的 API。

所有查询通过 @findapiagent 查找 API → /api-executor 执行。

## 查询类型

### 1. 个人工作状态（所有角色可用）

- **用户意图关键词**：我的工作状态、我今天的情况、我的工单统计
- **API**：POST /v1/staff/report/staff/work-status [staff]
- **参数**：需要传入当前用户的员工 ID 和日期范围（默认今天）
- **结果展示模板**：
  ```
  你今天的工作状态：
  - 新工单：X 张
  - 处理中：X 张
  - 等待中：X 张
  - 已解决：X 张
  - 已关闭：X 张
  - 共处理：X 张
  ```

### 2. 按状态查看工单列表（所有角色可用）

- **用户意图关键词**：列出我的 Open 工单、看看我的待处理工单、我有哪些未解决的
- **API**：POST /v1/staff/tickets/page [staff]
- **参数**：按状态筛选 + 当前用户作为处理人
- **结果展示**：每条工单显示编号、主题、客户名称
  ```
  你有 X 张处理中的工单：
  1. #12345 — 物流查询问题 — 客户：张先生
  2. #12346 — 退款申请 — 客户：李女士
  ...
  ```

### 3. 团队工作状态（TeamLeader 及以上）

- **用户意图关键词**：团队情况、团队工作状态、我们部门今天怎么样
- **API**：POST /v1/staff/report/staff/work-status [staff]
- **参数**：传入部门 ID，查询该部门所有成员的工作状态
- **结果展示模板**：
  ```
  你的团队今天的情况：
  - 张三：处理了 15 张，还有 3 张待处理
  - 李四：处理了 12 张，还有 5 张待处理
  - 王五：处理了 8 张，还有 8 张待处理
  团队总计：处理 35 张，待处理 16 张
  ```

### 4. 按未处理数量排序（TeamLeader 及以上）

- **用户意图关键词**：谁手上积压最多、谁最忙、工作量排名
- **API**：POST /v1/staff/auto-assign/workload/page [staff] 或 POST /v1/staff/report/staff/work-status [staff]
- **说明**：查询团队成员的工作量，按未处理工单数量降序排列
- **结果展示**：
  ```
  按未处理工单数量排序：
  1. 王五 — 8 张未处理
  2. 李四 — 5 张未处理
  3. 张三 — 3 张未处理
  ```

### 5. 工单数量统计（综合仪表盘）

- **用户意图关键词**：工单统计、今天的数据、仪表盘
- **API**：POST /v1/staff/dashboard/ticket/count-stats [staff]
- **说明**：返回综合的工单数量统计，包括各状态分布

### 6. 按部门统计工单数量

- **用户意图关键词**：各部门工单量、部门对比、哪个部门最多
- **API**：POST /v1/staff/dashboard/ticket/department-count [staff]
- **权限**：DeptManager 及以上

### 7. 按 Topic 统计工单数量

- **用户意图关键词**：各主题工单量、哪类问题最多
- **API**：POST /v1/staff/dashboard/ticket/topic-count [staff]

### 8. 工单趋势

- **用户意图关键词**：工单趋势、最近几天的变化、工单量走势
- **API**：POST /v1/staff/dashboard/ticket/trend [staff]
- **参数**：日期范围（默认最近 7 天）

### 9. 工单活动统计

- **用户意图关键词**：工单活动、回复量统计
- **API**：POST /v1/staff/dashboard/ticket/activity-stats [staff]

### 10. 平均解决时间

- **用户意图关键词**：平均解决时间、处理效率
- **API**：POST /v1/staff/dashboard/ticket/average-resolution-time [staff]

### 11. SLA 达成率

- **用户意图关键词**：SLA 达成、SLA 完成率
- **API**：POST /v1/staff/dashboard/ticket/sla-achieved [staff]

## 查询范围与角色关系

| 角色 | 可查询范围 |
|------|-----------|
| CSR | 仅自己的工单和个人工作状态 |
| TeamLeader | 个人 + 自己部门所有成员 |
| DeptManager | 个人 + 自己部门 + 部门级统计 |
| Admin | 全部数据，跨部门统计 |

当用户查询超出权限范围时，自动缩小到其权限范围内的数据。例如 CSR 说"团队情况"，回复："你目前是客服角色，我可以帮你查看你个人的工作状态，需要吗？"
