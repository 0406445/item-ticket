---
name: admin-ops
description: "管理员系统管理知识，用于部门、员工、Topic 和系统配置相关操作。"
user-invocable: false
---

# 管理员系统管理

提供管理员场景的业务知识和 API playbook。
适用于部门、员工、Topic 和系统配置相关请求，不负责编排或执行。

## 访问边界

- 仅 `Admin` 可用
- 非管理员进入本域时，主 agent 应直接拒绝，不再继续查找 API

## 常见意图

### 1. 部门与组织

- 意图关键词：创建部门、新建部门、添加部门、修改部门、系统配置
- 主 API：
  - `POST /v1/staff/departments`
  - `PUT /v1/staff/departments/{id}`
  - `GET /v1/staff/departments/{id}`
- 常见辅助查询：
  - `POST /v1/staff/departments/page`
  - `POST /v1/staff/slas/page`
  - `POST /v1/staff/staff/page`
- 关键输入：部门名称、部门编码、上级部门、负责人、SLA

### 2. 员工账号与凭证

- 意图关键词：创建员工、新建账号、注册员工、重置密码、初始化密码
- 主 API：
  - `POST /v1/staff/staff`
  - `PUT /v1/staff/staff/{id}`
  - `PUT /v1/staff/staff/{id}/password/reset`
- 常见辅助查询：
  - `POST /v1/staff/staff/page`
  - `GET /v1/staff/staff/{id}`
  - `POST /v1/staff/roles/page`
  - `POST /v1/staff/departments/page`
- 关键输入：姓名、邮箱、目标员工
- 默认策略：
  - 创建员工时优先先补齐 `roleIds`、`departmentIds`，能一次完成就不拆第二个写操作

### 3. Topic 与系统对象

- 意图关键词：创建主题、更新主题、主题列表、系统配置
- 主 API：
  - `POST /v1/staff/topics`
  - `PUT /v1/staff/topics/{id}`
  - `GET /v1/staff/topics/{id}`
  - `GET /v1/staff/configs/{namespace}/{key}`
  - `GET /v1/staff/configs/{namespace}`
  - `PUT /v1/staff/configs/{namespace}/{key}`
  - `PUT /v1/staff/configs/{namespace}/batch`
- 常见辅助查询：
  - `POST /v1/staff/topics/page`
  - `POST /v1/staff/departments/page`
- 关键输入：主题标题、归属部门、配置命名空间、配置项

### 4. 系统概览与统计

- 意图关键词：系统概览、系统状态、有多少部门、有多少用户
- 主 API：
  - `POST /v1/staff/departments/page`
  - `POST /v1/staff/staff/page`
- 关键输出：总量、主要状态、可继续 drill down 的方向

## 风险提示

- 重置密码、批量配置更新、删除类操作都属于高风险写操作
- 主 agent 应明确二次确认，不要直接执行
- 如果用户只给了名字没给唯一标识，优先先查再操作

## 常用固定 lookup

- 当前登录员工由主 agent 通过 `GET /v1/staff/auth/current` 获取，不需要额外检索
- 目标员工优先用 `POST /v1/staff/staff/page` 解析
- 目标部门优先用 `POST /v1/staff/departments/page` 解析
- 目标角色优先用 `POST /v1/staff/roles/page` 解析
- 目标 SLA 优先用 `POST /v1/staff/slas/page` 解析

## 后续建议

- 创建部门后，通常可以继续建议“是否添加成员”
- 创建员工后，通常可以继续建议“是否加入部门”
- 新建 Topic 后，通常可以继续建议“是否绑定到部门或表单”

## 兜底规则

- skill 已列出的部门、员工、Topic、配置主 API 优先直接使用
- 如果只是缺角色、部门、SLA、员工 ID，优先用这里列出的 page 接口解析
- 只有配置项、字段枚举或低频系统能力未列出时，才调用 `api-executor-agent`（schema_lookup 模式）
