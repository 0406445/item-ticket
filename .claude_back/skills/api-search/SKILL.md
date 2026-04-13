---
name: api-search
description: "内部 API 检索技能，用于查找 item-tickets 接口及请求响应 schema。"
user-invocable: false
disable-model-invocation: true
---

# API Search

这是给子 agent 用的底层技能，不直接承担用户对话。

## 文件位置

```
${CLAUDE_SKILL_DIR}/
├── SKILL.md                        ← 本文件
└── apis/
    ├── INDEX.txt                   ← 扁平文本索引（grep 搜索用）
    ├── INDEX.md                    ← Markdown 结构化索引（浏览用）
    ├── INDEX.jsonl                 ← JSON Lines 索引（程序化查询用）
    ├── api-docs-customer.json      ← OpenAPI 规范（完整 schema）
    ├── api-docs-iam.json
    ├── api-docs-open.json
    ├── api-docs-staff.json
    ├── api-docs-tenant.json
    └── api-docs-all.json           ← 全量合并（1.7MB，一般不需要）
```

Sources（5 个来源）：`customer`, `iam`, `open`, `staff`, `tenant`

`INDEX.txt` 每行格式：
`METHOD PATH | summary | cn_summary | [source] tag_cn`

- `cn_summary` 是中文操作摘要
- `tag_cn` 是中文分类标签

## 使用规则

1. 先用索引召回候选，再按 source 打开对应 `api-docs-{source}.json`
2. 优先读取最小必要片段，不要动辄读取 `api-docs-all.json`
3. path 使用索引里的原始 path，例如 `/v1/staff/tickets/page`
4. 只展开当前判断需要的 `$ref`
5. 结果必须可供别的 agent 继续处理，不要输出大段无结构说明

## 推荐检索方式

### 1. 文本召回

```bash
rg -n "ticket|工单" "${CLAUDE_SKILL_DIR}/apis/INDEX.txt"
```

常见组合方式：
```bash
rg -n "^POST .*departments" "${CLAUDE_SKILL_DIR}/apis/INDEX.txt"
rg -n "\[staff\].*部门管理" "${CLAUDE_SKILL_DIR}/apis/INDEX.txt"
```

### 2. 结构化过滤

```bash
jq -c 'select(.source == "staff" and (.summary | test("department"; "i")))' \
  "${CLAUDE_SKILL_DIR}/apis/INDEX.jsonl"
```

### 3. 查看 OpenAPI 详情

1. 从索引确定 `source`
2. 读取 `${CLAUDE_SKILL_DIR}/apis/api-docs-{source}.json`
3. 在 `paths` 中定位 path + method
4. 必要时从 `components.schemas` 展开 `$ref`

## 检索启发式

- 动作词优先映射到 method，例如创建/新增更偏向 `POST`
- 实体词优先匹配 summary、tag、path 段
- 如果是“名字转 ID”“查选项”“分页查询”这类辅助意图，优先查 `page`、`options`、`list`
- 对多个候选，比较必填参数、返回结构和 source 是否贴近当前场景

## 注意事项

- `staff` 是最大 source，优先多给几个关键词缩小范围
- `api-docs-all.json` 只在跨 source 对比时使用
- 本技能只提供检索方法，不负责输出格式，最终返回结构由调用它的子 agent 决定
