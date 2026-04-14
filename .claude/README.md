# .claude_back 架构说明

这套配置按三层拆分，避免 agent 和 skill 职责混杂。

## 1. 主控层

- 入口：`agents/onboarding-agent.md`
- 责任：用户交互、角色识别、权限判断、上下文维护、步骤编排、确认写操作
- 约束：不直接解析 OpenAPI，不直接执行 HTTP，不把内部技术细节直接暴露给用户

## 2. 执行层

- `agents/findapiagent.md`
  通用 API 检索子 agent，只负责从索引和 OpenAPI 中找候选接口
- `agents/api-validator.md`
  通用请求规划子 agent，只负责校验参数、补齐缺项、输出最小执行计划
- `agents/api-executor-agent.md`
  通用请求执行子 agent，只负责读取认证配置并执行已确认的请求

这一层全部返回结构化结果，不直接承担用户对话。

## 3. 知识层

- 业务 skills：`setup-onboarding`、`ticket-ops`、`work-status`、`team-mgmt`、`dept-config`、`admin-ops`、`auto-assign`、`filter-rules`
  只保存领域知识、权限边界、意图映射、常见分解方式
- 通用 skills：`api-search`、`api-executor`
  只给子 agent 提供底层检索和执行方法

## 设计原则

- 主 agent 只有一个，避免重复入口
- 子 agent 通用化，不绑定具体业务域
- skill 只承载知识和操作约束，不再编排完整流程
- 用户看到的是业务语言，子 agent 之间传递的是结构化技术结果

## 参考来源

本次拆分遵循：
- [docs/sub_agent.md](/Users/nests/Desktop/nests/item-ticket/docs/sub_agent.md)
- [docs/build_skill.md](/Users/nests/Desktop/nests/item-ticket/docs/build_skill.md)
