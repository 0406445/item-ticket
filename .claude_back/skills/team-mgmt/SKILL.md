---
name: team-mgmt
description: "团队管理领域知识：添加/移除部门成员、创建员工账号并入组、查询成员列表。TeamLeader/DeptManager/Admin 可用。"
user-invocable: false
---

# 团队成员管理

当需要管理部门成员（添加、移除、查询）或创建员工账号时，参考本领域知识。

执行流程：通过 @findapiagent 查找 API → @api-validator 校验参数 → /api-executor 执行请求。

## 权限边界

- **TeamLeader**：只能管理自己所在部门的成员
- **DeptManager**：只能管理自己所在部门的成员
- **Admin**：可管理所有部门的成员
- **CSR**：无权执行任何团队管理操作

跨部门操作时，如果当前用户不是 Admin，必须拒绝并提示："跨部门成员管理需要管理员权限。"

## 操作清单

### 1. 添加已有员工到部门

- **用户意图关键词**：把XX加到部门、添加成员、加入团队
- **需要的信息**：员工（姓名或 ID）+ 部门（名称或 ID，默认为用户所在部门）
- **API**：POST /v1/staff/departments/{departmentId}/members [staff]
- **名称解析**：
  - 员工姓名 → 通过 POST /v1/staff/staff/page [staff] 搜索解析为员工 ID
  - 部门名称 → 通过 POST /v1/staff/departments/page [staff] 搜索解析为部门 ID
  - "我的团队"/"我的部门" → 使用当前用户所在部门 ID
- **执行**：通过 @findapiagent 查找添加部门成员 API，填充 staffId 和 departmentId 参数后执行

### 2. 创建新员工并加入部门

- **用户意图关键词**：创建新员工并加入、新人入职、把新员工XX加到团队
- **需要的信息**：员工姓名 + 邮箱 + 部门（名称或 ID）
- **分两步执行**：
  1. 创建员工：POST /v1/staff/staff [staff]（需要姓名和邮箱）
  2. 添加到部门：POST /v1/staff/departments/{departmentId}/members [staff]（用第一步返回的员工 ID）
- **说明**：这是一个复合操作，需要按顺序执行。第一步创建员工后，自动将返回的员工 ID 传递给第二步。
- **缺少信息时**：
  - 没有邮箱 → 问用户："请提供这位新员工的邮箱地址"
  - 没有部门 → 默认使用用户所在部门，或问用户："要加到哪个部门？默认是你的部门。"

### 3. 从部门移除成员

- **用户意图关键词**：移除、从团队删除、把XX从部门去掉
- **需要的信息**：员工（姓名或 ID）+ 部门（名称或 ID）
- **API**：DELETE /v1/staff/departments/{departmentId}/members [staff]
- **⚠️ 不可逆操作**：执行前必须请求用户确认
  - 确认格式："即将把 [员工姓名] 从 [部门名称] 移除，确认吗？"
- **名称解析**：同添加成员

### 4. 查询部门成员列表

- **用户意图关键词**：团队成员、部门有谁、成员列表、我的团队都有谁
- **API**：POST /v1/staff/staff/page [staff]（按部门 ID 筛选）
- **参数**：部门 ID（默认为用户所在部门）
- **结果展示**：
  ```
  你的团队目前有 X 位成员：
  1. 张三 — zhangsan@company.com
  2. 李四 — lisi@company.com
  3. 王五 — wangwu@company.com
  ```

### 5. 查询员工信息

- **用户意图关键词**：查一下XX的信息、XX是谁、员工详情
- **按 ID 查询**：GET /v1/staff/staff/{id} [staff]
- **搜索查询**：POST /v1/staff/staff/page [staff]（按姓名搜索）
- **批量获取选项**：POST /v1/staff/staff/options/batch [staff]

### 6. 更新员工信息

- **用户意图关键词**：修改员工信息、更新XX的邮箱
- **API**：PUT /v1/staff/staff/{id} [staff]
- **名称解析**：如果用户提供姓名，先搜索解析为员工 ID

## 常见复合操作

| 用户说 | 分解步骤 |
|--------|---------|
| "把新员工 Lisa 加到我的团队，邮箱 lisa@company.com" | 1. 创建员工（姓名 Lisa，邮箱 lisa@company.com）→ 2. 添加到用户所在部门 |
| "把张三从技术部移到运营部" | 1. 解析张三 → 2. 解析技术部 → 3. 从技术部移除 → 4. 解析运营部 → 5. 添加到运营部 |
| "看看我的团队，然后把最后一个人移除" | 1. 查询成员列表 → 2. 确认要移除的人 → 3. 执行移除 |
