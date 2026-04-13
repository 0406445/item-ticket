---
name: auto-assign
description: "自动分配规则知识，用于规则、工作量和分配历史相关操作。"
user-invocable: false
---

# 自动分配规则领域知识

此域暂不默认开放给用户，主 agent 只有在用户明确提到时才进入解释或评估。

## 访问边界

- `TeamLeader`：自己部门
- `Admin`：全局
- 其他角色：无权

## API 查找种子

- `auto assign rule`
- `auto assign rule page`
- `auto assign workload`
- `auto assign history`

## 业务语义

- 常见动作：创建规则、更新规则、删除规则、开关规则、看工作量、看分配历史
- 常见策略：轮询、按工作量、每人上限
- 关键输入：部门、策略、状态、限制人数

## 默认回复策略

- 如果产品策略仍未开放，主 agent 优先回复“功能暂未开放”，并建议手动分配
- 如果后续开放，这个 skill 可以直接被主 agent 用作领域知识，不需要再改子 agent
