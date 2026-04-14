---
name: team-mgmt
description: "团队管理知识，用于成员增删、员工入组和员工信息相关操作。"
user-invocable: false
---

# 团队管理

提供团队成员管理相关的业务知识和 API playbook。
适用于成员增删、员工入组和员工信息类请求，不负责编排或执行。

## 访问边界

- `TeamLeader` / `DeptManager`：只处理自己部门
- `Admin`：可跨部门
- `CSR`：不进入本域

## 常见意图

### 1. 添加或移除成员

- 意图关键词：添加成员、加入团队、移除成员、从团队删除
- 主 API：
  - `POST /v1/staff/departments/{departmentId}/members`
  - `DELETE /v1/staff/departments/{departmentId}/members`
  - `POST /v1/staff/teams/{teamId}/members`
  - `DELETE /v1/staff/teams/{teamId}/members`
- 关键输入：目标员工、目标部门或团队
- 常见辅助查询：
  - `POST /v1/staff/staff/page`
  - `POST /v1/staff/departments/page`
  - `POST /v1/staff/teams/page`
- 风险：移除成员是不可逆写操作

### 2. 创建员工并入组

- 意图关键词：新人入职、创建新员工并加入、把新员工加到团队
- 主 API：
  - `POST /v1/staff/staff`
- 优先策略：
  - 如果目标是加入部门，优先在创建员工时直接带 `departmentIds`
  - 只有用户明确说“加入团队”或创建接口不支持目标字段时，才追加团队成员接口
- 常见辅助查询：
  - `POST /v1/staff/departments/page`
  - `POST /v1/staff/roles/page`
  - `POST /v1/staff/teams/page`
- 关键输入：姓名、邮箱、目标部门或团队
- 默认策略：
  - 用户说“其他默认”时，优先使用系统默认认证类型和基础角色
  - 用户没给用户名时，可按姓名或邮箱前缀生成待确认草案

### 3. 查询团队与员工信息

- 意图关键词：团队成员、成员列表、员工详情、查一下某人信息
- 主 API：
  - `POST /v1/staff/staff/page`
  - `GET /v1/staff/staff/{id}`
  - `POST /v1/staff/teams/page`
  - `GET /v1/staff/teams/{id}`
- 常见输出：姓名、邮箱、部门、状态

### 4. 更新员工信息

- 意图关键词：修改员工邮箱、更新员工信息
- 主 API：
  - `PUT /v1/staff/staff/{id}`
- 常见辅助查询：
  - `POST /v1/staff/staff/page`
- 关键输入：目标员工、修改内容

## 名称解析偏好

- 人员名称优先走员工分页查询
- 部门名称优先走部门分页查询
- 团队名称优先走团队分页查询
- 角色名称优先走角色分页查询
- “我的团队”“我的部门”默认落到当前用户部门
- “我”“当前登录员工”由主 agent 通过固定接口 `GET /v1/staff/auth/current` 解析，不走 `findapiagent`

## 复合操作提示

- “把张三从技术部移到运营部”应拆为：解析人 -> 从原部门移除 -> 加入新部门
- “先建人再入组”若目标是部门，优先尝试一次 `create staff` 完成；只有不支持时再拆分
- 对删除/移除类动作，主 agent 必须确认

## 兜底规则

- 如果 skill 中的主 API 已能覆盖动作，不调用 `findapiagent`
- 如果只是缺部门/团队/角色 ID，优先用这里列出的 page 接口解析
- 只有以下情况才调用 `findapiagent`：
  - 需要查字段枚举或默认值
  - 创建接口是否支持某字段不明确
  - 新业务不在本 playbook 内
