---
name: auto-assign
description: "自动分配规则知识，用于规则、工作量和分配历史相关操作。"
user-invocable: false
---

# 自动分配规则

提供自动分配规则相关的业务知识和 API playbook。
默认不作为常规用户入口，仅在用户明确提到相关能力时使用。

## 访问边界

- `TeamLeader`：自己部门
- `Admin`：全局
- 其他角色：无权

## 主 API

- `POST /v1/staff/auto-assign/rule`
- `PUT /v1/staff/auto-assign/rule`
- `PUT /v1/staff/auto-assign/rule/status`
- `DELETE /v1/staff/auto-assign/rule/{id}`
- `POST /v1/staff/auto-assign/rule/page`
- `POST /v1/staff/auto-assign/history/page`
- `POST /v1/staff/auto-assign/workload/page`

## 业务语义

- 常见动作：创建规则、更新规则、删除规则、开关规则、看工作量、看分配历史
- 常见策略：轮询、按工作量、每人上限
- 关键输入：部门、策略、状态、限制人数

## 默认回复策略

- 如果产品策略仍未开放，主 agent 优先回复“功能暂未开放”，并建议手动分配
- 如果后续开放，这个 skill 可以直接被主 agent 用作领域知识，不需要再改子 agent

## 兜底规则

- 规则、状态、工作量、历史优先使用这里列出的固定 API
- 如果请求涉及未列出的细粒度字段枚举或新策略类型，再调用 `findapiagent`
