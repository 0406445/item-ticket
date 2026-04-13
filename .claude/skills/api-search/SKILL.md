---
name: api-search
description: "Search and browse the item-tickets API index (702 endpoints). Use when the user asks about APIs, endpoints, request/response schemas, or needs to find a specific API. Examples: \"find ticket API\", \"what APIs are available for customer\", \"show me the staff dashboard endpoints\", \"API for creating ticket\""
---

# API Search（API 索引查询）

当用户需要**查找、浏览、了解** item-tickets 后端 API 时使用本技能。

## 文件结构

```
.claude/skills/api-search/
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

INDEX.txt 每行格式：`METHOD PATH | summary | [source] tag`

## 工作流

### 1. 关键词搜索（最常用）

用 grep 搜索 `apis/INDEX.txt`（路径相对于本 skill 目录）：

```bash
grep -i "ticket" .claude/skills/api-search/apis/INDEX.txt
```

可组合过滤：
```bash
# 只看某个 source
grep "\[staff\]" .claude/skills/api-search/apis/INDEX.txt

# 只看 POST 接口
grep "^POST" .claude/skills/api-search/apis/INDEX.txt

# 组合：staff 下的 ticket 相关 POST 接口
grep -i "ticket" .claude/skills/api-search/apis/INDEX.txt | grep "\[staff\]" | grep "^POST"
```

### 2. 浏览目录（了解有哪些模块）

读取 `apis/INDEX.md` 的 Table of Contents 部分（前 100 行左右），展示所有 source 和 tag 分组。

### 3. 查看完整 API 详情（请求参数、响应 schema）

1. 先从 `apis/INDEX.txt` 找到目标 API 及其 `[source]`
2. 读取对应的 `apis/api-docs-{source}.json`
3. 在 `paths` 对象中定位具体路径和方法
4. 展开 `$ref` 引用（从 `components/schemas`）获取完整 schema
5. 清晰展示：路径参数、查询参数、请求体、响应体

### 4. 用 jq 做结构化查询（高级）

```bash
# 搜索路径包含 ticket 的所有 API
cat .claude/skills/api-search/apis/INDEX.jsonl | jq -r 'select(.path | contains("ticket")) | "\(.method) \(.path) — \(.summary)"'

# 搜索某个 tag 下的所有 API
cat .claude/skills/api-search/apis/INDEX.jsonl | jq -r 'select(.tag == "Ticket API") | "\(.method) \(.path) — \(.summary)"'
```

## Checklist

```
- [ ] 用 grep 在 apis/INDEX.txt 中搜索关键词
- [ ] 确认目标 API 的 source 和 path
- [ ] 如需详情，读取 apis/api-docs-{source}.json 中对应的 path 定义
- [ ] 展开 $ref 引用，展示完整的请求/响应 schema
```

## 注意事项

- `api-docs-all.json` 是全量合并文件（1.7MB），一般不需要读取，优先用分 source 的文件
- `staff` 最大（577 endpoints），搜索时建议加关键词缩小范围
- 索引基于 2026-04-09 的 OpenAPI 导出，如 API 有更新需重新生成索引
