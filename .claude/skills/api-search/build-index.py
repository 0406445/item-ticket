#!/usr/bin/env python3
"""
从现有 INDEX.jsonl 生成带中文业务标识的增强索引。
输出: INDEX.txt (grep 搜索用) 和 INDEX.jsonl (程序化查询用)
"""

import json
import re
import sys
from pathlib import Path

APIS_DIR = Path(__file__).parent / "apis"

# ── Tag → 中文名映射 ──
TAG_CN = {
    # customer
    "Customer Options": "客户选项",
    "Customer Profile Management": "客户资料管理",
    "Customer Ticket Management": "客户工单管理",
    "Customer WebSocket": "客户WebSocket",
    "customer-auth-controller": "客户认证",
    # iam
    "Chat API": "在线聊天",
    "Customer Organization API": "客户组织",
    "Facility API": "设施管理",
    "IAM Staff Dashboard": "IAM员工仪表盘",
    "Staff Ticket Report": "工单报表",
    "Ticket API": "工单",
    "iam-extend-roster-controller": "排班扩展",
    # open
    "Attachment API": "附件",
    "Department API": "部门(开放)",
    "Enum Management": "枚举管理",
    "File API": "文件",
    "Form API": "表单(开放)",
    "HRM Test": "HRM测试",
    "Open Customer APIs": "客户(开放)",
    "Open Customer Organization APIs": "客户组织(开放)",
    "Open Tenant API": "租户(开放)",
    "Survey API": "满意度调查(开放)",
    "Ticket API": "工单(开放)",
    "Ticket Display Status API": "工单显示状态(开放)",
    "Ticket Priority API": "工单优先级(开放)",
    "Topic API": "工单主题(开放)",
    "open-config-controller": "开放配置",
    "test-controller": "测试",
    # staff
    "AI Agent Management": "AI智能体管理",
    "AI Assistant Agent Department Binding": "AI助手部门绑定",
    "AI Assistant Agent Registry": "AI助手注册",
    "AI Dashboard": "AI仪表盘",
    "API Key Management": "API密钥管理",
    "Attachment Index and Document Management Center": "附件索引与文档管理",
    "Attendance Admin": "考勤管理",
    "Audit Logs": "审计日志",
    "Auto Assign Rule": "自动分配规则",
    "CSV测试": "CSV测试",
    "Chat Session Management": "聊天会话管理",
    "Configuration Management": "系统配置",
    "Department Management": "部门管理",
    "Email Banlist Management": "邮件黑名单",
    "Email Configuration": "邮件配置",
    "Form Entry Management": "表单条目管理",
    "Form Entry Value Management": "表单条目值管理",
    "Form Management": "表单管理",
    "HR Organization Managers": "HR组织管理者",
    "HR Organization Unit Management": "HR组织单元管理",
    "HRM Batch Sync": "HRM批量同步",
    "HRM Kafka Control": "HRM Kafka控制",
    "Kafka Admin": "Kafka管理",
    "Leave Balance Management": "假期余额管理",
    "Leave Data Fix": "假期数据修复",
    "Leave Migration Management": "假期迁移管理",
    "Leave Request Management": "请假申请管理",
    "Leave Revoke Request Management": "销假申请管理",
    "Leave Type Management": "假期类型管理",
    "Notification Channel Management": "通知渠道管理",
    "Notification Instance Management": "通知实例管理",
    "Notification Setting Management": "通知设置管理",
    "Notification Template Group Management": "通知模板组管理",
    "Notification Template Management": "通知模板管理",
    "Overtime Request Management": "加班申请管理",
    "Permission Management": "权限管理",
    "Push Setting": "推送设置",
    "Push Token": "推送令牌",
    "Role Management": "角色管理",
    "SLA Management": "SLA管理",
    "Schedule Entry Management": "排班条目管理",
    "Schedule Management": "排班管理",
    "Shift Auto Publish Management": "班次自动发布",
    "Shift Bidding": "班次竞标",
    "Shift Instance Management": "班次实例管理",
    "Staff Attendance Confirmations": "员工考勤确认",
    "Staff Attendance Records": "员工考勤记录",
    "Staff Attendance Summary": "员工考勤汇总",
    "Staff Authentication": "员工认证",
    "Staff Dashboard": "员工仪表盘",
    "Staff Face Management": "员工人脸管理",
    "Staff HRM Attendance": "员工HRM考勤",
    "Staff Hierarchy": "员工层级",
    "Staff Management": "员工管理",
    "Staff Period Work Status": "员工周期工作状态",
    "Staff Ticket Report": "员工工单报表",
    "Staff WebSocket": "员工WebSocket",
    "Storage API": "存储",
    "Survey Config": "满意度调查配置",
    "Survey Dashboard": "满意度调查仪表盘",
    "Survey Ratings": "满意度评分",
    "Survey Send Logs": "满意度调查发送日志",
    "Tag Management": "标签管理",
    "Team Management": "团队管理",
    "Ticket Collaborators": "工单协作者",
    "Ticket Create Template Management": "工单创建模板",
    "Ticket Display Status": "工单显示状态",
    "Ticket Filter Group Management": "工单筛选组",
    "Ticket Filter Job": "工单筛选任务",
    "Ticket Filter Management": "工单筛选管理",
    "Ticket Macro Management": "工单宏管理",
    "Ticket Management": "工单管理",
    "Ticket Priority": "工单优先级",
    "Ticket Search": "工单搜索",
    "Ticket View Management": "工单视图管理",
    "Topic Management": "工单主题管理",
    "UF Dashboard": "UF仪表盘",
    "Wfm Dashboard": "劳动力管理仪表盘",
    "Workflow Definition Management": "工作流定义管理",
    "Workflow Diagram Management": "工作流图管理",
    "Workflow Instance Management": "工作流实例管理",
    "anomaly-analysis-controller": "异常分析",
    "customer-controller": "客户",
    "customer-organization-controller": "客户组织",
    "facility-controller": "设施",
    "roster-controller": "排班",
    "roster-primary-contact-review-controller": "排班主要联系人审核",
    "teams-channel-controller": "Teams频道",
    "ticket-escalation-controller": "工单升级",
    "ticket-side-conversation-controller": "工单侧边对话",
    "user-info-controller": "用户信息",
    # tenant
    "Tenant Management": "租户管理",
}

# ── HTTP Method → 中文动词 ──
METHOD_CN = {
    "GET": "查询",
    "POST": "创建",
    "PUT": "更新",
    "PATCH": "部分更新",
    "DELETE": "删除",
}

# ── 路径模式 → 更精确的中文动词 ──
# POST 不一定是创建，很多 POST 用于查询（分页、批量获取）
PATH_ACTION_PATTERNS = [
    # 查询类 POST（这些 POST 实际上是查询，不是创建）
    (r"/page$", "POST", "分页查询"),
    (r"/options/batch$", "POST", "批量获取选项"),
    (r"/best-match$", "POST", "匹配查询"),
    (r"/timeline$", "POST", "查询时间线"),
    (r"/count$", "POST", "统计数量"),
    (r"-count$", "POST", "统计数量"),
    (r"-stats$", "POST", "查询统计"),
    (r"-time$", "POST", "查询统计"),
    (r"/trend$", "POST", "查询趋势"),
    (r"/achieved$", "POST", "查询统计"),
    (r"/filter/", "POST", "筛选"),
    (r"/reply$", "POST", "回复"),
    (r"/guessing$", "POST", "智能推荐"),
    (r"/rating$", "POST", "提交评分"),
    (r"/reset$", "POST", "重置"),
    # 报表类（POST 但实际是查询/导出）
    (r"/report/", "POST", "查询报表"),
    (r"/dashboard/", "POST", "查询仪表盘"),
    (r"/statistics$", "GET", "查询统计"),
    (r"/stats$", "GET", "查询统计"),
    # 认证类
    (r"/login", "POST", "登录"),
    (r"/logout$", "POST", "登出"),
    (r"/switch-tenant$", "POST", "切换租户"),
    (r"/password$", "PUT", "修改密码"),
    (r"/language$", "PUT", "切换语言"),
    (r"/validate$", "GET", "验证"),
    (r"/current$", "GET", "获取当前信息"),
    (r"/tenants$", "GET", "获取租户列表"),
    # 批量/同步
    (r"/batch$", "POST", "批量操作"),
    (r"/sync$", "POST", "同步"),
    (r"/export$", "POST", "导出"),
    (r"/import$", "POST", "导入"),
    (r"/search$", "POST", "搜索"),
    (r"/upload$", "POST", "上传"),
    (r"/download$", "GET", "下载"),
    # 成员操作
    (r"/members$", "POST", "添加成员"),
    (r"/members$", "DELETE", "移除成员"),
    # 状态变更
    (r"/assign$", "POST", "分配"),
    (r"/transfer$", "POST", "转移"),
    (r"/close$", "POST", "关闭"),
    (r"/reopen$", "POST", "重新打开"),
    (r"/resolve$", "POST", "解决"),
    (r"/merge$", "POST", "合并"),
    (r"/clone$", "POST", "克隆"),
    (r"/enable$", "POST", "启用"),
    (r"/disable$", "POST", "禁用"),
    (r"/activate$", "POST", "激活"),
    (r"/deactivate$", "POST", "停用"),
    (r"/publish$", "POST", "发布"),
    (r"/unpublish$", "POST", "取消发布"),
    (r"/approve$", "POST", "审批通过"),
    (r"/reject$", "POST", "审批拒绝"),
    (r"/cancel$", "POST", "取消"),
]

# ── 英文实体 → 中文实体 ──
ENTITY_CN = {
    "department": "部门",
    "ticket": "工单",
    "staff": "员工",
    "customer": "客户",
    "team": "团队",
    "role": "角色",
    "permission": "权限",
    "tag": "标签",
    "topic": "主题",
    "form": "表单",
    "sla": "SLA",
    "schedule": "排班",
    "shift": "班次",
    "leave": "请假",
    "attendance": "考勤",
    "notification": "通知",
    "survey": "满意度调查",
    "workflow": "工作流",
    "organization": "组织",
    "tenant": "租户",
    "email": "邮件",
    "chat": "聊天",
    "session": "会话",
    "attachment": "附件",
    "file": "文件",
    "report": "报表",
    "dashboard": "仪表盘",
    "filter": "筛选",
    "view": "视图",
    "macro": "宏",
    "template": "模板",
    "priority": "优先级",
    "status": "状态",
    "collaborator": "协作者",
    "member": "成员",
    "agent": "智能体",
    "assistant": "助手",
    "config": "配置",
    "configuration": "配置",
    "setting": "设置",
    "rule": "规则",
    "log": "日志",
    "audit": "审计",
    "overtime": "加班",
    "roster": "排班表",
    "facility": "设施",
    "face": "人脸",
    "hierarchy": "层级",
    "escalation": "升级",
    "conversation": "对话",
    "channel": "频道",
    "token": "令牌",
    "key": "密钥",
    "storage": "存储",
    "enum": "枚举",
    "diagram": "流程图",
    "instance": "实例",
    "definition": "定义",
    "entry": "条目",
    "value": "值",
    "balance": "余额",
    "bidding": "竞标",
    "profile": "资料",
    "password": "密码",
    "language": "语言",
    "timezone": "时区",
}


def infer_action(method: str, path: str, summary: str) -> str:
    """根据 method + path 模式推断中文操作动词"""
    for pattern, m, action in PATH_ACTION_PATTERNS:
        if method == m and re.search(pattern, path):
            return action

    # summary 里的关键词
    sl = summary.lower()
    if any(w in sl for w in ["page", "query", "list", "get all", "search"]):
        return "查询"
    if any(w in sl for w in ["create", "add", "new"]):
        return "创建"
    if any(w in sl for w in ["update", "modify", "edit", "change"]):
        return "更新"
    if any(w in sl for w in ["delete", "remove"]):
        return "删除"
    if any(w in sl for w in ["export"]):
        return "导出"
    if any(w in sl for w in ["import"]):
        return "导入"
    if any(w in sl for w in ["upload"]):
        return "上传"
    if any(w in sl for w in ["download"]):
        return "下载"
    if any(w in sl for w in ["count", "statistics", "stats"]):
        return "统计"

    # 兜底用 method
    return METHOD_CN.get(method, method)


def extract_entities(path: str, summary: str, source: str) -> list[str]:
    """从 path 和 summary 中提取中文业务实体，排除 source 前缀干扰"""
    entities = set()
    # 去掉路径中的 source 前缀，避免 /v1/staff/departments 把 staff 当实体
    clean_path = re.sub(r"^/v1/(staff|customer|iam|open|tenant)/", "/v1/", path)
    text = (clean_path + " " + summary).lower()
    for en, cn in ENTITY_CN.items():
        # 用词边界匹配，避免 "log" 匹配到 "login"、"dialog" 等
        if re.search(r'\b' + re.escape(en) + r'(?:s|es|ies)?\b', text):
            entities.add(cn)
    return sorted(entities)


def build_cn_summary(action: str, entities: list[str], tag_cn: str) -> str:
    """构建中文摘要"""
    if entities:
        return f"{action} {'/'.join(entities)}"
    return f"{action} - {tag_cn}"


def main():
    input_file = APIS_DIR / "INDEX.jsonl"
    out_txt = APIS_DIR / "INDEX.txt"
    out_jsonl = APIS_DIR / "INDEX.jsonl"

    records = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))

    enriched = []
    for rec in records:
        method = rec["method"]
        path = rec["path"]
        summary = rec.get("summary", "") or ""
        tag = rec.get("tag", "")
        source = rec.get("source", "")
        operation_id = rec.get("operationId", "")

        tag_cn = TAG_CN.get(tag, tag)
        action = infer_action(method, path, summary)
        entities = extract_entities(path, summary, source)
        cn_summary = build_cn_summary(action, entities, tag_cn)

        rec["tag_cn"] = tag_cn
        rec["action"] = action
        rec["entities"] = entities
        rec["cn_summary"] = cn_summary
        enriched.append(rec)

    # 写 INDEX.jsonl
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for rec in enriched:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # 写 INDEX.txt
    # 新格式: METHOD PATH | summary | cn_summary | [source] tag_cn
    with open(out_txt, "w", encoding="utf-8") as f:
        for rec in enriched:
            method = rec["method"].ljust(6)
            path = rec["path"]
            summary = rec.get("summary", "") or "-"
            cn = rec["cn_summary"]
            source = rec["source"]
            tag_cn = rec["tag_cn"]
            f.write(f"{method} {path}  |  {summary}  |  {cn}  |  [{source}] {tag_cn}\n")

    print(f"Done: {len(enriched)} APIs enriched")
    print(f"  → {out_jsonl}")
    print(f"  → {out_txt}")


if __name__ == "__main__":
    main()
