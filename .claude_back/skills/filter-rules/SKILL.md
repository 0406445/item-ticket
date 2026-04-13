---
name: filter-rules
description: "工单筛选规则领域知识。当前默认不对终端用户开放，但保留 API 线索和权限边界。"
user-invocable: false
---

# 工单筛选规则领域知识

此域暂不默认开放给用户，主 agent 仅在用户明确提到时使用本知识。

## 访问边界

- `DeptManager`：自己部门
- `Admin`：全局
- 其他角色：无权

## API 查找种子

- `ticket filter group`
- `ticket filter fields`
- `filter group page`

## 业务语义

- 常见动作：创建规则组、更新规则组、删除规则组、查看详情
- 常见条件：状态、优先级、部门、时间范围、Topic
- 辅助查询：先查可用筛选字段，再让用户配置规则

## 默认回复策略

- 如果产品策略仍未开放，主 agent 优先回复“功能暂未开放”，并引导用户直接描述筛选条件
- 如果后续开放，此 skill 继续提供业务语义，无需把执行逻辑塞进 skill
