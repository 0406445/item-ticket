---
name: dept-config
description: "部门配置知识，用于负责人、邮箱、Atlas 绑定和部门设置相关操作。"
user-invocable: false
---

# 部门配置

提供部门设置相关的业务知识和 API playbook。
适用于负责人、邮箱、Atlas 绑定和部门基础配置，不负责编排或执行。

## 访问边界

- `DeptManager`：只处理自己部门
- `Admin`：可跨部门
- `CSR` 和 `TeamLeader`：不进入本域

## 常见意图

### 1. 查看部门配置

- 意图关键词：部门配置、部门信息、我的部门设置、部门详情
- 主 API：
  - `GET /v1/staff/departments/{id}`
- 默认范围：当前用户部门
- 期望输出：负责人、邮箱、AI 绑定、描述、基础配置

### 2. 更新负责人或基础信息

- 意图关键词：换负责人、改部门经理、修改部门名称、修改描述、修改编码
- 主 API：
  - `PUT /v1/staff/departments/{id}`
- 常见辅助查询：
  - `POST /v1/staff/staff/page`
  - `POST /v1/staff/departments/page`

### 3. 邮箱配置

- 意图关键词：换邮箱、修改部门邮箱、绑定新邮箱
- 主 API：
  - `POST /v1/staff/emails`
  - `PUT /v1/staff/emails/{id}`
- 常见辅助查询：
  - `POST /v1/staff/emails/page`
  - `GET /v1/staff/emails/{id}`
- 关键输入：目标部门、新邮箱
- 风险：可能覆盖已有绑定，主 agent 需要确认

### 4. Atlas / AI 绑定

- 意图关键词：开启 Atlas、关闭 Atlas、AI 绑定、Atlas AI
- 主 API：
  - `PUT /v1/staff/ai-assistant/departments/{departmentId}/assistant-agent`
  - `DELETE /v1/staff/ai-assistant/departments/{departmentId}/assistant-agent`
- 常见辅助查询：
  - `GET /v1/staff/ai-assistant/agents`
  - `POST /v1/staff/ai/agents/page`

### 5. 部门列表与排班

- 意图关键词：有哪些部门、部门列表、排班、工作时间
- 主 API：
  - `POST /v1/staff/departments/page`
- 用途：做跨部门选择或查看开放时间

## 额外约束

- 非 Admin 遇到跨部门配置请求时直接拦截
- 涉及负责人、邮箱、AI 绑定时，优先先查当前状态再改
- 变更类请求默认视为写操作，需要确认
- “我的部门”“当前登录员工所在部门”优先由主 agent 通过 `GET /v1/staff/auth/current` 解析当前部门 ID，再走部门详情或更新接口

## 兜底规则

- skill 已列出的部门、邮箱、AI 绑定接口优先直接使用
- 如果只是缺部门 ID、员工 ID、邮箱配置 ID、assistant agent 代码或 ID，优先用这里的 lookup API 解析
- 如果需要查更细的字段枚举、配置命名空间或未列出的部门周边能力，再调用 `api-executor-agent`（schema_lookup 模式）
