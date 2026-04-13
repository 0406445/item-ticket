# API Index

> Auto-generated from OpenAPI specs. Total: **702** endpoints across **5** sources.
>
> Sources: customer, iam, open, staff, tenant

## Table of Contents

- [CUSTOMER](#source-customer) (28 endpoints, 5 tags)
  - [Customer Options](#customer--customer-options) (7)
  - [Customer Profile Management](#customer--customer-profile-management) (1)
  - [Customer Ticket Management](#customer--customer-ticket-management) (9)
  - [Customer WebSocket](#customer--customer-websocket) (1)
  - [customer-auth-controller](#customer--customer-auth-controller) (10)
- [IAM](#source-iam) (42 endpoints, 7 tags)
  - [Chat API](#iam--chat-api) (2)
  - [Customer Organization API](#iam--customer-organization-api) (2)
  - [Facility API](#iam--facility-api) (2)
  - [IAM Staff Dashboard](#iam--iam-staff-dashboard) (9)
  - [Staff Ticket Report](#iam--staff-ticket-report) (12)
  - [Ticket API](#iam--ticket-api) (12)
  - [iam-extend-roster-controller](#iam--iam-extend-roster-controller) (3)
- [OPEN](#source-open) (46 endpoints, 16 tags)
  - [Attachment API](#open--attachment-api) (2)
  - [Department API](#open--department-api) (3)
  - [Enum Management](#open--enum-management) (1)
  - [File API](#open--file-api) (1)
  - [Form API](#open--form-api) (1)
  - [HRM Test](#open--hrm-test) (2)
  - [Open Customer APIs](#open--open-customer-apis) (1)
  - [Open Customer Organization APIs](#open--open-customer-organization-apis) (2)
  - [Open Tenant API](#open--open-tenant-api) (1)
  - [Survey API](#open--survey-api) (2)
  - [Ticket API](#open--ticket-api) (4)
  - [Ticket Display Status API](#open--ticket-display-status-api) (2)
  - [Ticket Priority API](#open--ticket-priority-api) (2)
  - [Topic API](#open--topic-api) (2)
  - [open-config-controller](#open--open-config-controller) (1)
  - [test-controller](#open--test-controller) (19)
- [STAFF](#source-staff) (577 endpoints, 91 tags)
  - [AI Agent Management](#staff--ai-agent-management) (7)
  - [AI Assistant Agent Department Binding](#staff--ai-assistant-agent-department-binding) (2)
  - [AI Assistant Agent Registry](#staff--ai-assistant-agent-registry) (5)
  - [AI Dashboard](#staff--ai-dashboard) (10)
  - [API Key Management](#staff--api-key-management) (5)
  - [Attachment Index and Document Management Center](#staff--attachment-index-and-document-management-center) (5)
  - [Attendance Admin](#staff--attendance-admin) (1)
  - [Audit Logs](#staff--audit-logs) (2)
  - [Auto Assign Rule](#staff--auto-assign-rule) (7)
  - [CSV测试](#staff--csv测试) (3)
  - [Chat Session Management](#staff--chat-session-management) (9)
  - [Configuration Management](#staff--configuration-management) (6)
  - [Department Management](#staff--department-management) (7)
  - [Email Banlist Management](#staff--email-banlist-management) (5)
  - [Email Configuration](#staff--email-configuration) (6)
  - [Form Entry Management](#staff--form-entry-management) (1)
  - [Form Entry Value Management](#staff--form-entry-value-management) (1)
  - [Form Management](#staff--form-management) (7)
  - [HR Organization Managers](#staff--hr-organization-managers) (15)
  - [HR Organization Unit Management](#staff--hr-organization-unit-management) (24)
  - [HRM Batch Sync](#staff--hrm-batch-sync) (5)
  - [HRM Kafka Control](#staff--hrm-kafka-control) (4)
  - [Kafka Admin](#staff--kafka-admin) (6)
  - [Leave Balance Management](#staff--leave-balance-management) (21)
  - [Leave Data Fix](#staff--leave-data-fix) (4)
  - [Leave Migration Management](#staff--leave-migration-management) (2)
  - [Leave Request Management](#staff--leave-request-management) (8)
  - [Leave Revoke Request Management](#staff--leave-revoke-request-management) (5)
  - [Leave Type Management](#staff--leave-type-management) (11)
  - [Notification Channel Management](#staff--notification-channel-management) (6)
  - [Notification Instance Management](#staff--notification-instance-management) (9)
  - [Notification Setting Management](#staff--notification-setting-management) (6)
  - [Notification Template Group Management](#staff--notification-template-group-management) (5)
  - [Notification Template Management](#staff--notification-template-management) (3)
  - [Overtime Request Management](#staff--overtime-request-management) (9)
  - [Permission Management](#staff--permission-management) (3)
  - [Push Setting](#staff--push-setting) (2)
  - [Push Token](#staff--push-token) (2)
  - [Role Management](#staff--role-management) (5)
  - [SLA Management](#staff--sla-management) (5)
  - [Schedule Entry Management](#staff--schedule-entry-management) (4)
  - [Schedule Management](#staff--schedule-management) (8)
  - [Shift Auto Publish Management](#staff--shift-auto-publish-management) (1)
  - [Shift Bidding](#staff--shift-bidding) (3)
  - [Shift Instance Management](#staff--shift-instance-management) (12)
  - [Staff Attendance Confirmations](#staff--staff-attendance-confirmations) (13)
  - [Staff Attendance Records](#staff--staff-attendance-records) (6)
  - [Staff Attendance Summary](#staff--staff-attendance-summary) (9)
  - [Staff Authentication](#staff--staff-authentication) (15)
  - [Staff Dashboard](#staff--staff-dashboard) (8)
  - [Staff Face Management](#staff--staff-face-management) (6)
  - [Staff HRM Attendance](#staff--staff-hrm-attendance) (1)
  - [Staff Hierarchy](#staff--staff-hierarchy) (3)
  - [Staff Management](#staff--staff-management) (10)
  - [Staff Period Work Status](#staff--staff-period-work-status) (5)
  - [Staff Ticket Report](#staff--staff-ticket-report) (12)
  - [Staff WebSocket](#staff--staff-websocket) (1)
  - [Storage API](#staff--storage-api) (5)
  - [Survey Config](#staff--survey-config) (4)
  - [Survey Dashboard](#staff--survey-dashboard) (1)
  - [Survey Ratings](#staff--survey-ratings) (1)
  - [Survey Send Logs](#staff--survey-send-logs) (2)
  - [Tag Management](#staff--tag-management) (6)
  - [Team Management](#staff--team-management) (9)
  - [Ticket Collaborators](#staff--ticket-collaborators) (2)
  - [Ticket Create Template Management](#staff--ticket-create-template-management) (6)
  - [Ticket Display Status](#staff--ticket-display-status) (6)
  - [Ticket Filter Group Management](#staff--ticket-filter-group-management) (5)
  - [Ticket Filter Job](#staff--ticket-filter-job) (2)
  - [Ticket Filter Management](#staff--ticket-filter-management) (6)
  - [Ticket Macro Management](#staff--ticket-macro-management) (6)
  - [Ticket Management](#staff--ticket-management) (38)
  - [Ticket Priority](#staff--ticket-priority) (6)
  - [Ticket Search](#staff--ticket-search) (1)
  - [Ticket View Management](#staff--ticket-view-management) (10)
  - [Topic Management](#staff--topic-management) (5)
  - [UF Dashboard](#staff--uf-dashboard) (6)
  - [Wfm Dashboard](#staff--wfm-dashboard) (7)
  - [Workflow Definition Management](#staff--workflow-definition-management) (6)
  - [Workflow Diagram Management](#staff--workflow-diagram-management) (1)
  - [Workflow Instance Management](#staff--workflow-instance-management) (9)
  - [anomaly-analysis-controller](#staff--anomaly-analysis-controller) (1)
  - [customer-controller](#staff--customer-controller) (9)
  - [customer-organization-controller](#staff--customer-organization-controller) (5)
  - [facility-controller](#staff--facility-controller) (5)
  - [roster-controller](#staff--roster-controller) (8)
  - [roster-primary-contact-review-controller](#staff--roster-primary-contact-review-controller) (7)
  - [teams-channel-controller](#staff--teams-channel-controller) (12)
  - [ticket-escalation-controller](#staff--ticket-escalation-controller) (7)
  - [ticket-side-conversation-controller](#staff--ticket-side-conversation-controller) (5)
  - [user-info-controller](#staff--user-info-controller) (2)
- [TENANT](#source-tenant) (9 endpoints, 1 tags)
  - [Tenant Management](#tenant--tenant-management) (9)

---
## <a id="source-customer"></a>CUSTOMER

### <a id="customer--customer-options"></a>Customer Options

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/customer/customer-organizations/options/batch` | Get customer organization options by IDs |
| `POST` | `/v1/customer/customers/options/batch` | Get customer options by IDs |
| `POST` | `/v1/customer/departments/options/batch` | Get department options by IDs |
| `POST` | `/v1/customer/staff/options/batch` | Get staff options by IDs |
| `POST` | `/v1/customer/teams/options/batch` | Get team options by IDs |
| `POST` | `/v1/customer/ticket/priorities/options/batch` | Get ticket priority options by IDs |
| `POST` | `/v1/customer/topics/options/batch` | Get topic options by IDs |

### <a id="customer--customer-profile-management"></a>Customer Profile Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/customer/profile` | Get customer profile |

### <a id="customer--customer-ticket-management"></a>Customer Ticket Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/customer/tickets/brief/{id}` | Get ticket brief information |
| `GET` | `/v1/customer/tickets/number/{code}` | Get ticket detail by number |
| `POST` | `/v1/customer/tickets/number/{ticketNumber}/timeline` | Get ticket timeline by number |
| `POST` | `/v1/customer/tickets/page` | Query customer tickets with pagination |
| `GET` | `/v1/customer/tickets/statistics` | Get ticket statistics |
| `POST` | `/v1/customer/tickets/statistics/ai-summary` | Generate AI summary from statistics |
| `GET` | `/v1/customer/tickets/{id}` | Get ticket detail by ID |
| `GET` | `/v1/customer/tickets/{ticketId}/form-entries/{topicId}` | Get ticket form entries |
| `POST` | `/v1/customer/tickets/{ticketId}/timeline` | Get ticket timeline by ID |

### <a id="customer--customer-websocket"></a>Customer WebSocket

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/customer/websocket/stats` | Get basic WebSocket stats |

### <a id="customer--customer-auth-controller"></a>customer-auth-controller

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/customer/auth/current` | - |
| `PUT` | `/v1/customer/auth/language` | - |
| `POST` | `/v1/customer/auth/login` | - |
| `POST` | `/v1/customer/auth/login/iam` | Customer IAM login |
| `POST` | `/v1/customer/auth/logout` | - |
| `PUT` | `/v1/customer/auth/password` | - |
| `POST` | `/v1/customer/auth/switch-tenant` | - |
| `GET` | `/v1/customer/auth/tenant` | - |
| `GET` | `/v1/customer/auth/tenants` | - |
| `GET` | `/v1/customer/auth/validate` | - |

---
## <a id="source-iam"></a>IAM

### <a id="iam--chat-api"></a>Chat API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/iam/chat/agent/business-hours` | Get Business Hours |
| `POST` | `/v1/iam/chat/session/sync` | Sync Staff Session Status |

### <a id="iam--customer-organization-api"></a>Customer Organization API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/customer-organizations/best-match` | Get best matching organizations by name |
| `POST` | `/v1/iam/customer-organizations/page` | Page customer organizations |

### <a id="iam--facility-api"></a>Facility API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/extend/facility/page` | Page query facilities |
| `GET` | `/v1/iam/extend/facility/{id}` | Get facility by ID |

### <a id="iam--iam-staff-dashboard"></a>IAM Staff Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/dashboard/staff/department-count` | Get staff counts by department |
| `POST` | `/v1/iam/dashboard/ticket/activity-stats` | Get ticket activity statistics by department |
| `POST` | `/v1/iam/dashboard/ticket/average-resolution-time` | Get average resolution time statistics by department |
| `POST` | `/v1/iam/dashboard/ticket/count-stats` | Get comprehensive ticket count statistics |
| `POST` | `/v1/iam/dashboard/ticket/department-count` | Get ticket counts by department |
| `POST` | `/v1/iam/dashboard/ticket/organization/average-resolution-time` | Get average resolution time statistics by organization  |
| `POST` | `/v1/iam/dashboard/ticket/sla-achieved` | Get SLA achievement statistics by department |
| `POST` | `/v1/iam/dashboard/ticket/topic-count` | Get ticket counts by topic |
| `POST` | `/v1/iam/dashboard/ticket/trend` | Get ticket count trend over time |

### <a id="iam--staff-ticket-report"></a>Staff Ticket Report

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/report/extend/data-entry` | Get data entry report with configurable field aggregations |
| `POST` | `/v1/iam/report/extend/data-entry/export` | Export data entry report to Excel |
| `POST` | `/v1/iam/report/staff/work-status` | Get staff work status data |
| `POST` | `/v1/iam/report/staff/work-status/export` | Export staff work status data to Excel |
| `POST` | `/v1/iam/report/ticket/activity` | Get ticket activity statistics |
| `POST` | `/v1/iam/report/ticket/activity/export` | Export ticket activity statistics to Excel |
| `POST` | `/v1/iam/report/ticket/sla` | Get ticket SLA and AHT statistics |
| `POST` | `/v1/iam/report/ticket/sla/export` | Export ticket SLA and AHT statistics to Excel |
| `POST` | `/v1/iam/report/ticket/sla/new` | Get new ticket SLA and AHT statistics |
| `POST` | `/v1/iam/report/ticket/sla/new/export` | Export new ticket SLA and AHT statistics to Excel |
| `POST` | `/v1/iam/report/ticket/status` | Get ticket status statistics |
| `POST` | `/v1/iam/report/ticket/status/export` | Export ticket status statistics to Excel |

### <a id="iam--ticket-api"></a>Ticket API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/tickets` | Create a ticket |
| `GET` | `/v1/iam/tickets/brief/{id}` | Get ticket brief info |
| `POST` | `/v1/iam/tickets/filter/{ticketId}` | Handler Ticket Filter |
| `POST` | `/v1/iam/tickets/list-with-first-message` | List tickets with first message |
| `POST` | `/v1/iam/tickets/messages` | Page messages |
| `POST` | `/v1/iam/tickets/page` | Page tickets |
| `POST` | `/v1/iam/tickets/search` | Search tickets |
| `PUT` | `/v1/iam/tickets/{id}` | Partial update a ticket |
| `POST` | `/v1/iam/tickets/{id}/messages` | Page ticket messages |
| `POST` | `/v1/iam/tickets/{id}/reply` | Reply to a ticket |
| `GET` | `/v1/iam/tickets/{ticketId}/form-entries` | Get ticket form entries |
| `PUT` | `/v1/iam/tickets/{ticketId}/form-entries` | Update ticket form entries |

### <a id="iam--iam-extend-roster-controller"></a>iam-extend-roster-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/iam/extend/roster/guessing` | - |
| `POST` | `/v1/iam/extend/roster/page` | - |
| `GET` | `/v1/iam/extend/roster/{id}` | - |

---
## <a id="source-open"></a>OPEN

### <a id="open--attachment-api"></a>Attachment API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/attachments` | - |
| `POST` | `/v1/open/attachments/images` | Upload image attachment |

### <a id="open--department-api"></a>Department API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/departments/options/batch` | - |
| `POST` | `/v1/open/departments/page` | - |
| `GET` | `/v1/open/departments/{id}/schedule` | - |

### <a id="open--enum-management"></a>Enum Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/enums` | Get all enums |

### <a id="open--file-api"></a>File API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/files/{fileId}` | - |

### <a id="open--form-api"></a>Form API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/forms/topic/{topicId}` | - |

### <a id="open--hrm-test"></a>HRM Test

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/hrm-sync/test` | Test HRM employee sync (Local Only) |
| `POST` | `/v1/open/hrm-sync/test-create-teams` | Test Team creation workflow (Local Only) |

### <a id="open--open-customer-apis"></a>Open Customer APIs

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/customers/password/reset` | Request password reset |

### <a id="open--open-customer-organization-apis"></a>Open Customer Organization APIs

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/customer-organizations/page` | Query customer organizations with pagination |
| `GET` | `/v1/open/customer-organizations/{id}` | Get customer organization by ID |

### <a id="open--open-tenant-api"></a>Open Tenant API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/tenants/{id}` | Get tenant by ID |

### <a id="open--survey-api"></a>Survey API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/surveys/{token}` | - |
| `POST` | `/v1/open/surveys/{token}/rating` | - |

### <a id="open--ticket-api"></a>Ticket API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/tickets` | - |
| `POST` | `/v1/open/tickets/link` | - |
| `GET` | `/v1/open/tickets/number/{ticketNumber}` | - |
| `POST` | `/v1/open/tickets/number/{ticketNumber}/timeline` | - |

### <a id="open--ticket-display-status-api"></a>Ticket Display Status API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/ticket/display-statuses/options/batch` | Get display status options by IDs |
| `POST` | `/v1/open/ticket/display-statuses/page` | Query ticket display statuses with pagination |

### <a id="open--ticket-priority-api"></a>Ticket Priority API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/ticket/priorities/options/batch` | Get priority options by IDs |
| `POST` | `/v1/open/ticket/priorities/page` | Query ticket priorities with pagination |

### <a id="open--topic-api"></a>Topic API

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/open/topics/options/batch` | - |
| `POST` | `/v1/open/topics/page` | - |

### <a id="open--open-config-controller"></a>open-config-controller

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/configs/system` | - |

### <a id="open--test-controller"></a>test-controller

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/open/test` | - |
| `POST` | `/v1/open/test/activity` | - |
| `GET` | `/v1/open/test/agent/business-hours` | - |
| `POST` | `/v1/open/test/extend/data-entry` | - |
| `GET` | `/v1/open/test/form-entries` | - |
| `POST` | `/v1/open/test/notification/publish/in-app` | - |
| `POST` | `/v1/open/test/notification/publish/system` | - |
| `POST` | `/v1/open/test/search` | - |
| `POST` | `/v1/open/test/sla-aht` | - |
| `POST` | `/v1/open/test/staff-work-status` | - |
| `POST` | `/v1/open/test/staff/productive/report` | - |
| `POST` | `/v1/open/test/status` | - |
| `GET` | `/v1/open/test/survey/send` | Test survey email send |
| `GET` | `/v1/open/test/ticket/count` | - |
| `POST` | `/v1/open/test/ticket/number/{ticketNumber}/simulate-email` | - |
| `POST` | `/v1/open/test/ticket/{ticketId}/simulate-email` | - |
| `GET` | `/v1/open/test/websocket/stats` | Get WebSocket statistics |
| `POST` | `/v1/open/test/workflow/start` | - |
| `POST` | `/v1/open/test/{ticketId}/print` | - |

---
## <a id="source-staff"></a>STAFF

### <a id="staff--ai-agent-management"></a>AI Agent Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ai/agents` | Create AI agent |
| `GET` | `/v1/staff/ai/agents/built-in-tools` | Get built-in tools |
| `GET` | `/v1/staff/ai/agents/llm-info` | Get LLM information |
| `POST` | `/v1/staff/ai/agents/options/batch` | Get AI agent options by IDs |
| `POST` | `/v1/staff/ai/agents/page` | Page query AI agents |
| `GET` | `/v1/staff/ai/agents/{id}` | Get AI agent by ID |
| `PUT` | `/v1/staff/ai/agents/{id}` | Update AI agent |

### <a id="staff--ai-assistant-agent-department-binding"></a>AI Assistant Agent Department Binding

| Method | Path | Summary |
|--------|------|---------|
| `DELETE` | `/v1/staff/ai-assistant/departments/{departmentId}/assistant-agent` | Unbind assistant agent |
| `PUT` | `/v1/staff/ai-assistant/departments/{departmentId}/assistant-agent` | Bind assistant agent |

### <a id="staff--ai-assistant-agent-registry"></a>AI Assistant Agent Registry

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/ai-assistant/agents` | List assistant agents |
| `POST` | `/v1/staff/ai-assistant/agents` | Create assistant agent |
| `POST` | `/v1/staff/ai-assistant/agents/validate` | Validate assistant agent baseUrl |
| `DELETE` | `/v1/staff/ai-assistant/agents/{code}` | Delete assistant agent |
| `PUT` | `/v1/staff/ai-assistant/agents/{code}` | Update assistant agent |

### <a id="staff--ai-dashboard"></a>AI Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ai-dashboard/accuracy-trend` | Get AI accuracy trend over time |
| `POST` | `/v1/staff/ai-dashboard/agent-stats` | Get AI Agent statistics |
| `POST` | `/v1/staff/ai-dashboard/ai-coverage-trend` | Get AI coverage trend over time |
| `POST` | `/v1/staff/ai-dashboard/assistant-stats` | Get AI Assistant statistics |
| `POST` | `/v1/staff/ai-dashboard/involved-tickets-trend` | Get involved tickets trend over time |
| `POST` | `/v1/staff/ai-dashboard/message-processes/page` | - |
| `POST` | `/v1/staff/ai-dashboard/metrics/summary` | Query metrics summary |
| `POST` | `/v1/staff/ai-dashboard/metrics/time-series` | Query metrics time series |
| `POST` | `/v1/staff/ai-dashboard/overview` | Get AI Dashboard overview statistics |
| `POST` | `/v1/staff/ai-dashboard/stats` | Get AI Dashboard statistics |

### <a id="staff--api-key-management"></a>API Key Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/api-keys` | Create API key |
| `POST` | `/v1/staff/api-keys/page` | Page query API keys |
| `DELETE` | `/v1/staff/api-keys/{id}` | Delete API key |
| `GET` | `/v1/staff/api-keys/{id}` | Get API key by ID |
| `PUT` | `/v1/staff/api-keys/{id}` | Update API key |

### <a id="staff--attachment-index-and-document-management-center"></a>Attachment Index and Document Management Center

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/attachment-index/add-tag` | AI auto-tag attachments |
| `POST` | `/v1/staff/attachment-index/export` | Export attachment index to Excel |
| `POST` | `/v1/staff/attachment-index/page` | Page query attachment index |
| `POST` | `/v1/staff/attachment-index/updateAttachment` | updateAttachment |
| `GET` | `/v1/staff/attachment-index/{attachmentId}` | Get attachment detail |

### <a id="staff--attendance-admin"></a>Attendance Admin

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/admin/attendance-records` | 手动创建考勤记录 |

### <a id="staff--audit-logs"></a>Audit Logs

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/audit-logs/page` | Query audit logs with pagination |
| `POST` | `/v1/staff/audit-logs/scan` | Scan audit annotations |

### <a id="staff--auto-assign-rule"></a>Auto Assign Rule

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/auto-assign/history/page` | Get auto assign history |
| `POST` | `/v1/staff/auto-assign/rule` | Create a auto assign rule |
| `PUT` | `/v1/staff/auto-assign/rule` | Update a auto assign rule |
| `POST` | `/v1/staff/auto-assign/rule/page` | Page query auto assign rules |
| `PUT` | `/v1/staff/auto-assign/rule/status` | Update auto assign rule status only |
| `DELETE` | `/v1/staff/auto-assign/rule/{id}` | Delete a auto assign rule |
| `POST` | `/v1/staff/auto-assign/workload/page` | Query staff workload |

### <a id="staff--csv测试"></a>CSV测试

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/csv-test/check-header-mapping` | 检查表头映射 |
| `GET` | `/v1/staff/csv-test/parse-first-record` | 测试第一条记录解析 |
| `GET` | `/v1/staff/csv-test/parse-headers` | 测试CSV表头解析 |

### <a id="staff--chat-session-management"></a>Chat Session Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/session-staff/active` | Get active sessions |
| `POST` | `/v1/staff/session-staff/assign` | Assign session |
| `GET` | `/v1/staff/session-staff/chat/token` | Get chat platform token |
| `POST` | `/v1/staff/session-staff/close` | Close chat session |
| `POST` | `/v1/staff/session-staff/history/page` | Page query session history |
| `POST` | `/v1/staff/session-staff/page` | Page query sessions |
| `POST` | `/v1/staff/session-staff/start` | Start chat session |
| `POST` | `/v1/staff/session-staff/upload/file` | Upload file |
| `GET` | `/v1/staff/session-staff/{sessionId}` | Get session by ID |

### <a id="staff--configuration-management"></a>Configuration Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/configs/variables/{type}` | List template variables |
| `GET` | `/v1/staff/configs/{namespace}` | List config items |
| `PUT` | `/v1/staff/configs/{namespace}/batch` | Batch update config items |
| `DELETE` | `/v1/staff/configs/{namespace}/{key}` | Delete config item |
| `GET` | `/v1/staff/configs/{namespace}/{key}` | Get config item |
| `PUT` | `/v1/staff/configs/{namespace}/{key}` | Update config item |

### <a id="staff--department-management"></a>Department Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/departments` | Create department |
| `POST` | `/v1/staff/departments/options/batch` | Get department options |
| `POST` | `/v1/staff/departments/page` | Query departments |
| `DELETE` | `/v1/staff/departments/{departmentId}/members` | Remove department members |
| `POST` | `/v1/staff/departments/{departmentId}/members` | Add department members |
| `GET` | `/v1/staff/departments/{id}` | Get department by ID |
| `PUT` | `/v1/staff/departments/{id}` | Update department |

### <a id="staff--email-banlist-management"></a>Email Banlist Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/email-banlists` | Create email banlist entry |
| `POST` | `/v1/staff/email-banlists/page` | Page query email banlist |
| `DELETE` | `/v1/staff/email-banlists/{id}` | Delete email banlist entry |
| `GET` | `/v1/staff/email-banlists/{id}` | Get email banlist entry by ID |
| `PUT` | `/v1/staff/email-banlists/{id}` | Update email banlist entry |

### <a id="staff--email-configuration"></a>Email Configuration

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/emails` | Create email configuration |
| `POST` | `/v1/staff/emails/authenticate` | Authenticate email |
| `POST` | `/v1/staff/emails/options/batch` | Get email options by IDs |
| `POST` | `/v1/staff/emails/page` | Page query emails |
| `GET` | `/v1/staff/emails/{id}` | Get email by ID |
| `PUT` | `/v1/staff/emails/{id}` | Update email configuration |

### <a id="staff--form-entry-management"></a>Form Entry Management

| Method | Path | Summary |
|--------|------|---------|
| `PUT` | `/v1/staff/form-entries/{id}` | Update form entry |

### <a id="staff--form-entry-value-management"></a>Form Entry Value Management

| Method | Path | Summary |
|--------|------|---------|
| `PUT` | `/v1/staff/form-entry-values` | Update form entry value |

### <a id="staff--form-management"></a>Form Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/forms` | Create form |
| `GET` | `/v1/staff/forms/field/{fieldId}` | Get form field |
| `POST` | `/v1/staff/forms/options/batch` | Get form options by IDs |
| `POST` | `/v1/staff/forms/page` | Page query forms |
| `GET` | `/v1/staff/forms/topic/{topicId}` | Get forms by topic |
| `GET` | `/v1/staff/forms/{id}` | Get form by ID |
| `PUT` | `/v1/staff/forms/{id}` | Update form |

### <a id="staff--hr-organization-managers"></a>HR Organization Managers

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/hr-org-managers` | Create organization manager |
| `GET` | `/v1/staff/hr-org-managers/active-relation` | Get active manager relation |
| `POST` | `/v1/staff/hr-org-managers/batch` | Batch create or update managers |
| `GET` | `/v1/staff/hr-org-managers/check-exists` | Check manager relationship exists |
| `POST` | `/v1/staff/hr-org-managers/list` | List organization managers |
| `GET` | `/v1/staff/hr-org-managers/org-unit/{orgUnitId}` | Get managers by organization unit |
| `GET` | `/v1/staff/hr-org-managers/org-unit/{orgUnitId}/effective-on` | Get managers effective on date |
| `PUT` | `/v1/staff/hr-org-managers/org-unit/{orgUnitId}/expire-all` | Expire all managers for organization unit |
| `POST` | `/v1/staff/hr-org-managers/page` | Page query organization managers |
| `GET` | `/v1/staff/hr-org-managers/staff/{staffId}` | Get managers by staff |
| `PUT` | `/v1/staff/hr-org-managers/staff/{staffId}/expire-all` | Expire all managers for staff |
| `DELETE` | `/v1/staff/hr-org-managers/{id}` | Delete organization manager |
| `GET` | `/v1/staff/hr-org-managers/{id}` | Get organization manager by ID |
| `PUT` | `/v1/staff/hr-org-managers/{id}` | Update organization manager |
| `PUT` | `/v1/staff/hr-org-managers/{id}/expire` | Expire organization manager |

### <a id="staff--hr-organization-unit-management"></a>HR Organization Unit Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/hr-org-units` | Create organization unit |
| `GET` | `/v1/staff/hr-org-units/active` | Get all active organization units |
| `POST` | `/v1/staff/hr-org-units/by-codes` | Get organization units by codes |
| `GET` | `/v1/staff/hr-org-units/check-code` | Check if code is available |
| `GET` | `/v1/staff/hr-org-units/check-name` | Check if name is available |
| `GET` | `/v1/staff/hr-org-units/count` | Get organization unit count |
| `GET` | `/v1/staff/hr-org-units/count/{unitType}` | Get organization unit count by type |
| `POST` | `/v1/staff/hr-org-units/descendants` | Get organizations with descendants |
| `POST` | `/v1/staff/hr-org-units/options` | Get organization unit options |
| `POST` | `/v1/staff/hr-org-units/page` | Page query organization units |
| `GET` | `/v1/staff/hr-org-units/parent/{parentId}/children` | Get children by parent ID |
| `GET` | `/v1/staff/hr-org-units/roots` | Get root organization units |
| `GET` | `/v1/staff/hr-org-units/tree` | Get organization tree |
| `GET` | `/v1/staff/hr-org-units/tree/{rootId}` | Get organization tree from root |
| `GET` | `/v1/staff/hr-org-units/type/{unitType}` | Get organization units by type |
| `DELETE` | `/v1/staff/hr-org-units/{id}` | Delete organization unit |
| `GET` | `/v1/staff/hr-org-units/{id}` | Get organization unit detail |
| `PUT` | `/v1/staff/hr-org-units/{id}` | Update organization unit |
| `PUT` | `/v1/staff/hr-org-units/{id}/activate` | Activate organization unit |
| `GET` | `/v1/staff/hr-org-units/{id}/ancestors` | Get ancestors |
| `GET` | `/v1/staff/hr-org-units/{id}/basic` | Get organization unit basic info |
| `PUT` | `/v1/staff/hr-org-units/{id}/deactivate` | Deactivate organization unit |
| `GET` | `/v1/staff/hr-org-units/{id}/descendants` | Get descendants |
| `PUT` | `/v1/staff/hr-org-units/{id}/move` | Move organization unit |

### <a id="staff--hrm-batch-sync"></a>HRM Batch Sync

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/admin/hrm-batch-sync/create-teams` | Create supervisor Teams |
| `POST` | `/v1/staff/admin/hrm-batch-sync/sync` | Sync HRM employees |
| `POST` | `/v1/staff/admin/hrm-batch-sync/sync-complete` | Complete supervisor Team sync |
| `POST` | `/v1/staff/admin/hrm-batch-sync/update-hr-department` | Update employee hrDepartmentId |
| `POST` | `/v1/staff/admin/hrm-batch-sync/update-supervisor-ids` | Update supervisor IDs |

### <a id="staff--hrm-kafka-control"></a>HRM Kafka Control

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/admin/hrm-kafka/pause` | Pause Kafka consumer |
| `POST` | `/v1/staff/admin/hrm-kafka/reset-offset` | Reset consumer group offset to beginning |
| `POST` | `/v1/staff/admin/hrm-kafka/resume` | Resume Kafka consumer |
| `GET` | `/v1/staff/admin/hrm-kafka/status` | Get Kafka consumer status |

### <a id="staff--kafka-admin"></a>Kafka Admin

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/admin/kafka/consumers` | List all Kafka consumers |
| `GET` | `/v1/staff/admin/kafka/consumers/{containerId}/exists` | Check if Kafka consumer exists |
| `POST` | `/v1/staff/admin/kafka/consumers/{containerId}/pause` | Pause Kafka consumer |
| `POST` | `/v1/staff/admin/kafka/consumers/{containerId}/reset-offset` | Reset consumer group offset to beginning |
| `POST` | `/v1/staff/admin/kafka/consumers/{containerId}/resume` | Resume Kafka consumer |
| `GET` | `/v1/staff/admin/kafka/consumers/{containerId}/status` | Get Kafka consumer status |

### <a id="staff--leave-balance-management"></a>Leave Balance Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/leave-balances` | Create leave balance |
| `DELETE` | `/v1/staff/leave-balances/batch` | Batch delete leave balances |
| `POST` | `/v1/staff/leave-balances/batch` | Get leave balances by IDs |
| `POST` | `/v1/staff/leave-balances/batch-update` | Batch update used minutes |
| `POST` | `/v1/staff/leave-balances/export` | Export leave balances to Excel |
| `POST` | `/v1/staff/leave-balances/import` | Import leave balances from Excel |
| `GET` | `/v1/staff/leave-balances/import-template` | Download leave balance import template |
| `POST` | `/v1/staff/leave-balances/initialize` | Initialize staff balances |
| `GET` | `/v1/staff/leave-balances/low-balance` | Get low balance records |
| `GET` | `/v1/staff/leave-balances/me/all-types-with-balances/{period}` | Get all leave types with balances |
| `GET` | `/v1/staff/leave-balances/me/period/{period}` | Get my balances |
| `POST` | `/v1/staff/leave-balances/page` | Page query leave balances |
| `POST` | `/v1/staff/leave-balances/release` | Release leave minutes |
| `POST` | `/v1/staff/leave-balances/reserve` | Reserve leave minutes |
| `GET` | `/v1/staff/leave-balances/staff/{staffId}/period/{period}` | Get balances by staff and period |
| `GET` | `/v1/staff/leave-balances/staff/{staffId}/type/{leaveTypeId}/period/{period}` | Get balance by staff, type and period |
| `GET` | `/v1/staff/leave-balances/staff/{staffId}/type/{leaveTypeId}/period/{period}/check` | Check balance availability |
| `GET` | `/v1/staff/leave-balances/staff/{staffId}/type/{leaveTypeId}/period/{period}/remaining` | Get remaining balance |
| `DELETE` | `/v1/staff/leave-balances/{id}` | Delete leave balance |
| `GET` | `/v1/staff/leave-balances/{id}` | Get leave balance |
| `PUT` | `/v1/staff/leave-balances/{id}` | Update leave balance |

### <a id="staff--leave-data-fix"></a>Leave Data Fix

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/leave/data-fix/execute` | Fix Historical Leave Data |
| `GET` | `/v1/staff/leave/data-fix/preview` | Preview Leave Data Fix |
| `POST` | `/v1/staff/leave/data-fix/recalculate` | Recalculate All Leave Balances |
| `GET` | `/v1/staff/leave/data-fix/recalculate/preview` | Preview Leave Balance Recalculation |

### <a id="staff--leave-migration-management"></a>Leave Migration Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/leave/migration/execute` | Execute Leave Migration |
| `GET` | `/v1/staff/leave/migration/status` | Get Migration Status |

### <a id="staff--leave-request-management"></a>Leave Request Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/leave/balance` | 查询假期余额 |
| `POST` | `/v1/staff/leave/requests/export` | 导出请假记录 |
| `POST` | `/v1/staff/leave/requests/list` | 列表查询请假记录 |
| `POST` | `/v1/staff/leave/requests/page` | 分页查询请假记录 |
| `POST` | `/v1/staff/leave/requests/preview` | Preview Leave Impact |
| `GET` | `/v1/staff/leave/requests/{id}` | Get Leave Request |
| `GET` | `/v1/staff/leave/requests/{id}/approval-history` | 获取请假审批历史 |
| `PUT` | `/v1/staff/leave/requests/{id}/cancel` | 撤销请假申请 |

### <a id="staff--leave-revoke-request-management"></a>Leave Revoke Request Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/leave/revoke/requests` | Submit leave revoke request |
| `POST` | `/v1/staff/leave/revoke/requests/list` | List leave revoke requests |
| `POST` | `/v1/staff/leave/revoke/requests/page` | Page query leave revoke requests |
| `GET` | `/v1/staff/leave/revoke/requests/{id}` | Get leave revoke request detail |
| `POST` | `/v1/staff/leave/revoke/requests/{id}/cancel` | Cancel leave revoke request |

### <a id="staff--leave-type-management"></a>Leave Type Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/leave-types` | Create leave type |
| `DELETE` | `/v1/staff/leave-types/batch` | Batch delete leave types |
| `POST` | `/v1/staff/leave-types/batch` | Get leave types by IDs |
| `GET` | `/v1/staff/leave-types/code/{code}` | Get leave type by code |
| `GET` | `/v1/staff/leave-types/exists/code/{code}` | Check code existence |
| `GET` | `/v1/staff/leave-types/options` | Get all options |
| `POST` | `/v1/staff/leave-types/options/batch` | Get options by IDs |
| `POST` | `/v1/staff/leave-types/page` | Page query leave types |
| `DELETE` | `/v1/staff/leave-types/{id}` | Delete leave type |
| `GET` | `/v1/staff/leave-types/{id}` | Get leave type |
| `PUT` | `/v1/staff/leave-types/{id}` | Update leave type |

### <a id="staff--notification-channel-management"></a>Notification Channel Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/notification/channels` | Create notification channel |
| `POST` | `/v1/staff/notification/channels/options/batch` | Get notification channel options |
| `POST` | `/v1/staff/notification/channels/page` | Page query notification channels |
| `DELETE` | `/v1/staff/notification/channels/{id}` | Delete notification channel |
| `GET` | `/v1/staff/notification/channels/{id}` | Get notification channel by ID |
| `PUT` | `/v1/staff/notification/channels/{id}` | Update notification channel |

### <a id="staff--notification-instance-management"></a>Notification Instance Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/notification/instances/page` | Page query notification instances |
| `POST` | `/v1/staff/notification/instances/personal/page` | Page query notification instances |
| `POST` | `/v1/staff/notification/instances/read/batch` | Mark multiple as read |
| `POST` | `/v1/staff/notification/instances/system/publish` | Publish system notification |
| `GET` | `/v1/staff/notification/instances/unread-counts` | Get unread notification counts |
| `DELETE` | `/v1/staff/notification/instances/{id}` | delete notification |
| `GET` | `/v1/staff/notification/instances/{id}` | Get notification instance by ID |
| `PUT` | `/v1/staff/notification/instances/{id}` | update notification |
| `POST` | `/v1/staff/notification/instances/{id}/read` | Mark as read |

### <a id="staff--notification-setting-management"></a>Notification Setting Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/notification/settings` | Create notification setting |
| `POST` | `/v1/staff/notification/settings/options/batch` | Get notification setting options |
| `POST` | `/v1/staff/notification/settings/page` | Page query notification settings |
| `DELETE` | `/v1/staff/notification/settings/{id}` | Delete notification setting |
| `GET` | `/v1/staff/notification/settings/{id}` | Get notification setting by ID |
| `PUT` | `/v1/staff/notification/settings/{id}` | Update notification setting |

### <a id="staff--notification-template-group-management"></a>Notification Template Group Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/notification/template-groups` | Create notification template group |
| `POST` | `/v1/staff/notification/template-groups/batch` | Get notification template groups by IDs |
| `POST` | `/v1/staff/notification/template-groups/page` | Page query notification template groups |
| `GET` | `/v1/staff/notification/template-groups/{id}` | Get notification template group by ID |
| `PUT` | `/v1/staff/notification/template-groups/{id}` | Update notification template group |

### <a id="staff--notification-template-management"></a>Notification Template Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/notification/templates` | Create notification template |
| `GET` | `/v1/staff/notification/templates/{id}` | Get notification template by ID |
| `PUT` | `/v1/staff/notification/templates/{id}` | Update notification template |

### <a id="staff--overtime-request-management"></a>Overtime Request Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/overtime/balance` | 查询加班余额 |
| `POST` | `/v1/staff/overtime/requests/batch-delete` | 批量删除加班申请 |
| `POST` | `/v1/staff/overtime/requests/export` | 导出加班申请 |
| `POST` | `/v1/staff/overtime/requests/list` | 列表查询加班申请 |
| `POST` | `/v1/staff/overtime/requests/page` | 分页查询加班申请 |
| `POST` | `/v1/staff/overtime/requests/pending-approval/page` | 查询待审批的加班申请 |
| `GET` | `/v1/staff/overtime/requests/statistics` | 查询加班统计 |
| `GET` | `/v1/staff/overtime/requests/{id}` | 查询加班申请详情 |
| `POST` | `/v1/staff/overtime/requests/{id}/cancel` | 取消加班申请 |

### <a id="staff--permission-management"></a>Permission Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/permissions` | Create permission |
| `GET` | `/v1/staff/permissions/tree` | Get permission tree |
| `PUT` | `/v1/staff/permissions/{id}` | Update permission |

### <a id="staff--push-setting"></a>Push Setting

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/push-settings` | Get push setting |
| `PUT` | `/v1/staff/push-settings` | Update push setting |

### <a id="staff--push-token"></a>Push Token

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/push-tokens/register` | Register push token |
| `POST` | `/v1/staff/push-tokens/unregister` | Unregister push token |

### <a id="staff--role-management"></a>Role Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/roles` | Create role |
| `POST` | `/v1/staff/roles/options/batch` | Get role options by IDs |
| `POST` | `/v1/staff/roles/page` | Page query roles |
| `GET` | `/v1/staff/roles/{id}` | Get role by ID |
| `PUT` | `/v1/staff/roles/{id}` | Update role |

### <a id="staff--sla-management"></a>SLA Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/slas` | Create SLA |
| `POST` | `/v1/staff/slas/options/batch` | Get options by ids |
| `POST` | `/v1/staff/slas/page` | Page query SLAs |
| `GET` | `/v1/staff/slas/{id}` | Get SLA |
| `PUT` | `/v1/staff/slas/{id}` | Update SLA |

### <a id="staff--schedule-entry-management"></a>Schedule Entry Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/schedules/{scheduleId}/entries` | Get schedule entries |
| `POST` | `/v1/staff/schedules/{scheduleId}/entries` | Create schedule entry |
| `DELETE` | `/v1/staff/schedules/{scheduleId}/entries/{id}` | Delete schedule entry |
| `PUT` | `/v1/staff/schedules/{scheduleId}/entries/{id}` | Update schedule entry |

### <a id="staff--schedule-management"></a>Schedule Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/schedules` | Create schedule |
| `POST` | `/v1/staff/schedules/apply` | Apply schedule |
| `POST` | `/v1/staff/schedules/apply/preview` | Preview schedule apply |
| `POST` | `/v1/staff/schedules/options/batch` | Get options by ids |
| `POST` | `/v1/staff/schedules/page` | Page query schedules |
| `GET` | `/v1/staff/schedules/type/{type}` | Get schedules by type |
| `GET` | `/v1/staff/schedules/{id}` | Get schedule |
| `PUT` | `/v1/staff/schedules/{id}` | Update schedule |

### <a id="staff--shift-auto-publish-management"></a>Shift Auto Publish Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/shift-auto-publish/manual` | Manual Auto Publish Shifts |

### <a id="staff--shift-bidding"></a>Shift Bidding

| Method | Path | Summary |
|--------|------|---------|
| `DELETE` | `/v1/staff/shift-bidding` | Delete unbid shifts |
| `GET` | `/v1/staff/shift-bidding` | Query shift bidding calendar |
| `POST` | `/v1/staff/shift-bidding/bid` | Bid for a shift by time slot |

### <a id="staff--shift-instance-management"></a>Shift Instance Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/shift-instances` | Create Shift Instance |
| `POST` | `/v1/staff/shift-instances/batch-delete` | Batch Delete by Conditions |
| `POST` | `/v1/staff/shift-instances/batch-delete-selected` | Batch Delete Selected |
| `POST` | `/v1/staff/shift-instances/batch-publish` | Batch Publish by Conditions |
| `POST` | `/v1/staff/shift-instances/batch-revert-to-draft` | Batch Revert to Draft by Conditions (Admin Only) |
| `POST` | `/v1/staff/shift-instances/page` | Page Query Shift Instances |
| `POST` | `/v1/staff/shift-instances/publish` | Publish Shifts |
| `POST` | `/v1/staff/shift-instances/unpublish` | Unpublish Shifts |
| `POST` | `/v1/staff/shift-instances/update-for-leave` | Update Shift Instances for Leave |
| `DELETE` | `/v1/staff/shift-instances/{id}` | Delete Shift Instance |
| `GET` | `/v1/staff/shift-instances/{id}` | Get Shift Instance |
| `PUT` | `/v1/staff/shift-instances/{id}` | Update Shift Instance |

### <a id="staff--staff-attendance-confirmations"></a>Staff Attendance Confirmations

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/attendance-confirmations/clock-out` | Clock Out并填写午餐和休息时间 |
| `POST` | `/v1/staff/attendance-confirmations/confirm` | 确认考勤 (Agree操作) |
| `POST` | `/v1/staff/attendance-confirmations/dispute` | 提交考勤异议 (Reject操作) |
| `POST` | `/v1/staff/attendance-confirmations/disputes/export` | 导出考勤异议记录 |
| `POST` | `/v1/staff/attendance-confirmations/disputes/page` | 分页查询所有考勤异议（后台管理） |
| `GET` | `/v1/staff/attendance-confirmations/disputes/pending` | 查询待审批的考勤异议 (Team Leader) |
| `GET` | `/v1/staff/attendance-confirmations/disputes/{id}` | 获取考勤异议详情 |
| `POST` | `/v1/staff/attendance-confirmations/disputes/{id}/approve` | 批准考勤异议 (Team Leader) |
| `POST` | `/v1/staff/attendance-confirmations/disputes/{id}/reject` | 拒绝考勤异议 (Team Leader) |
| `POST` | `/v1/staff/attendance-confirmations/disputes/{id}/revise` | 员工修改考勤异议（退回修改后重新提交或撤回） |
| `GET` | `/v1/staff/attendance-confirmations/history` | 查询考勤确认历史 |
| `GET` | `/v1/staff/attendance-confirmations/history/all` | 获取所有考勤确认历史 |
| `GET` | `/v1/staff/attendance-confirmations/pending` | 获取待确认的每日考勤摘要 |

### <a id="staff--staff-attendance-records"></a>Staff Attendance Records

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/attendance-records/batch-push-to-hrm` | Batch Push Attendance Records to HRM |
| `POST` | `/v1/staff/attendance-records/export` | 导出考勤报表 |
| `POST` | `/v1/staff/attendance-records/list` | List Query Attendance Records |
| `POST` | `/v1/staff/attendance-records/page` | Page Query Attendance Records |
| `POST` | `/v1/staff/attendance-records/push-to-hrm/{id}` | Push Attendance Record to HRM |
| `PUT` | `/v1/staff/attendance-records/{id}` | Update Attendance Record (Admin Only) |

### <a id="staff--staff-attendance-summary"></a>Staff Attendance Summary

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/attendance-summary` | Create Attendance Summary |
| `POST` | `/v1/staff/attendance-summary/generate` | Generate Attendance Summaries |
| `GET` | `/v1/staff/attendance-summary/id/{id}` | Get Attendance Summary by ID |
| `POST` | `/v1/staff/attendance-summary/page` | Page Query Attendance Summaries |
| `GET` | `/v1/staff/attendance-summary/range/{staffId}` | Get Summaries by Date Range |
| `GET` | `/v1/staff/attendance-summary/statistics/{staffId}` | Get Summary Statistics |
| `GET` | `/v1/staff/attendance-summary/working-hours/{staffId}` | 获取工作时长统计 |
| `DELETE` | `/v1/staff/attendance-summary/{id}` | Delete Attendance Summary |
| `PUT` | `/v1/staff/attendance-summary/{id}` | Update Attendance Summary |

### <a id="staff--staff-authentication"></a>Staff Authentication

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/auth/current` | Get current staff |
| `GET` | `/v1/staff/auth/dummy-email` | Generate dummy email address |
| `PUT` | `/v1/staff/auth/language` | Update language |
| `POST` | `/v1/staff/auth/login` | Staff login |
| `POST` | `/v1/staff/auth/login/iam` | Staff IAM login |
| `POST` | `/v1/staff/auth/logout` | Staff logout |
| `PUT` | `/v1/staff/auth/password` | Update password |
| `GET` | `/v1/staff/auth/signature` | Get signature |
| `PUT` | `/v1/staff/auth/signature` | Update signature |
| `POST` | `/v1/staff/auth/switch-tenant` | Switch tenant |
| `GET` | `/v1/staff/auth/tenant` | Get current tenant |
| `GET` | `/v1/staff/auth/tenants` | Get valid tenant list |
| `PUT` | `/v1/staff/auth/timezone` | Update timezone |
| `GET` | `/v1/staff/auth/validate` | Validate session token |
| `PUT` | `/v1/staff/auth/work-status` | Update staff work status |

### <a id="staff--staff-dashboard"></a>Staff Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/dashboard/staff/department-count` | Get staff counts by department |
| `POST` | `/v1/staff/dashboard/ticket/activity-stats` | Get ticket activity statistics by department |
| `POST` | `/v1/staff/dashboard/ticket/average-resolution-time` | Get average resolution time statistics by department |
| `POST` | `/v1/staff/dashboard/ticket/count-stats` | Get comprehensive ticket count statistics |
| `POST` | `/v1/staff/dashboard/ticket/department-count` | Get ticket counts by department |
| `POST` | `/v1/staff/dashboard/ticket/sla-achieved` | Get SLA achievement statistics by department |
| `POST` | `/v1/staff/dashboard/ticket/topic-count` | Get ticket counts by topic |
| `POST` | `/v1/staff/dashboard/ticket/trend` | Get ticket count trend over time |

### <a id="staff--staff-face-management"></a>Staff Face Management

| Method | Path | Summary |
|--------|------|---------|
| `DELETE` | `/v1/staff/staff-face/delete/{staffId}` | Delete Face |
| `POST` | `/v1/staff/staff-face/page` | Page Face |
| `POST` | `/v1/staff/staff-face/register/{staffId}` | Register Face |
| `PUT` | `/v1/staff/staff-face/update/{staffId}` | Update Face |
| `POST` | `/v1/staff/staff-face/verify/{staffId}` | Verify Face |
| `GET` | `/v1/staff/staff-face/{staffId}` | Get Staff Face |

### <a id="staff--staff-hrm-attendance"></a>Staff HRM Attendance

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/hrm/attendance/query` | Query HRM Attendance Records |

### <a id="staff--staff-hierarchy"></a>Staff Hierarchy

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/hierarchy/tree` | Get staff hierarchy tree |
| `POST` | `/v1/staff/hierarchy/validate-manager` | Validate manager assignment |
| `GET` | `/v1/staff/hierarchy/{staffId}/subordinates` | Get direct subordinates |

### <a id="staff--staff-management"></a>Staff Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/staff` | Create staff |
| `POST` | `/v1/staff/staff/hr-page` | Page query staff for HR |
| `GET` | `/v1/staff/staff/iam-user/check` | Check IAM user by email |
| `POST` | `/v1/staff/staff/import` | Import staff from Excel |
| `POST` | `/v1/staff/staff/options/batch` | Get staff options by IDs |
| `POST` | `/v1/staff/staff/page` | Page query staff |
| `GET` | `/v1/staff/staff/template` | Generate staff import template |
| `GET` | `/v1/staff/staff/{id}` | Get staff by ID |
| `PUT` | `/v1/staff/staff/{id}` | Update staff |
| `PUT` | `/v1/staff/staff/{id}/password/reset` | Reset staff password |

### <a id="staff--staff-period-work-status"></a>Staff Period Work Status

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/period-work-status` | Create staff period work status |
| `PUT` | `/v1/staff/period-work-status` | Update staff period work status |
| `POST` | `/v1/staff/period-work-status/page` | Page query staff period work status |
| `DELETE` | `/v1/staff/period-work-status/{id}` | Delete staff period work status |
| `GET` | `/v1/staff/period-work-status/{id}` | Get staff period work status by ID |

### <a id="staff--staff-ticket-report"></a>Staff Ticket Report

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/report/extend/data-entry` | Get data entry report with configurable field aggregations |
| `POST` | `/v1/staff/report/extend/data-entry/export` | Export data entry report to Excel |
| `POST` | `/v1/staff/report/staff/work-status` | Get staff work status data |
| `POST` | `/v1/staff/report/staff/work-status/export` | Export staff work status data to Excel |
| `POST` | `/v1/staff/report/ticket/activity` | Get ticket activity statistics |
| `POST` | `/v1/staff/report/ticket/activity/export` | Export ticket activity statistics to Excel |
| `POST` | `/v1/staff/report/ticket/sla` | Get ticket SLA and AHT statistics |
| `POST` | `/v1/staff/report/ticket/sla/export` | Export ticket SLA and AHT statistics to Excel |
| `POST` | `/v1/staff/report/ticket/sla/new` | Get new ticket SLA and AHT statistics |
| `POST` | `/v1/staff/report/ticket/sla/new/export` | Export new ticket SLA and AHT statistics to Excel |
| `POST` | `/v1/staff/report/ticket/status` | Get ticket status statistics |
| `POST` | `/v1/staff/report/ticket/status/export` | Export ticket status statistics to Excel |

### <a id="staff--staff-websocket"></a>Staff WebSocket

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/websocket/stats` | Get WebSocket statistics |

### <a id="staff--storage-api"></a>Storage API

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/attachments` | - |
| `POST` | `/v1/staff/attachments` | - |
| `POST` | `/v1/staff/attachments/clone` | - |
| `POST` | `/v1/staff/attachments/images` | Upload image attachment |
| `DELETE` | `/v1/staff/attachments/{id}` | - |

### <a id="staff--survey-config"></a>Survey Config

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/survey/config/rules` | List Survey Rules |
| `POST` | `/v1/staff/survey/config/rules` | Create Survey Rule |
| `DELETE` | `/v1/staff/survey/config/rules/{ruleId}` | Delete Survey Rule |
| `PUT` | `/v1/staff/survey/config/rules/{ruleId}` | Update Survey Rule |

### <a id="staff--survey-dashboard"></a>Survey Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/report/survey/dashboard` | Get survey dashboard data |

### <a id="staff--survey-ratings"></a>Survey Ratings

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/survey/ratings/page` | Page query survey ratings overview |

### <a id="staff--survey-send-logs"></a>Survey Send Logs

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/survey/send-logs/debug/{ticketId}/token` | [DEBUG] Get survey token by ticket ID - LOCAL ENV ONLY |
| `POST` | `/v1/staff/survey/send-logs/page` | Page query survey send logs |

### <a id="staff--tag-management"></a>Tag Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/tags` | Create a new tag |
| `POST` | `/v1/staff/tags/options/batch` | - |
| `POST` | `/v1/staff/tags/page` | Page query tags |
| `DELETE` | `/v1/staff/tags/{id}` | Delete tag by ID |
| `GET` | `/v1/staff/tags/{id}` | Get tag by ID |
| `PUT` | `/v1/staff/tags/{id}` | Update an existing tag |

### <a id="staff--team-management"></a>Team Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/teams` | Create team |
| `POST` | `/v1/staff/teams/import` | Import teams from Excel |
| `POST` | `/v1/staff/teams/options/batch` | Get team options by IDs |
| `POST` | `/v1/staff/teams/page` | Page query teams |
| `GET` | `/v1/staff/teams/template` | Generate team import template |
| `GET` | `/v1/staff/teams/{id}` | Get team by ID |
| `PUT` | `/v1/staff/teams/{id}` | Update team |
| `DELETE` | `/v1/staff/teams/{teamId}/members` | Remove team members |
| `POST` | `/v1/staff/teams/{teamId}/members` | Add team members |

### <a id="staff--ticket-collaborators"></a>Ticket Collaborators

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket-collaborators/batch-update` | Batch update ticket collaborators |
| `POST` | `/v1/staff/ticket-collaborators/query` | Query ticket collaborators |

### <a id="staff--ticket-create-template-management"></a>Ticket Create Template Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket-create-templates` | Create ticket create template |
| `POST` | `/v1/staff/ticket-create-templates/list` | List ticket create templates |
| `POST` | `/v1/staff/ticket-create-templates/options/batch` | - |
| `POST` | `/v1/staff/ticket-create-templates/page` | Page query ticket create templates |
| `GET` | `/v1/staff/ticket-create-templates/{id}` | Get ticket create template by ID |
| `PUT` | `/v1/staff/ticket-create-templates/{id}` | Update ticket create template |

### <a id="staff--ticket-display-status"></a>Ticket Display Status

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/ticket/display-status` | Get display statuses |
| `POST` | `/v1/staff/ticket/display-status` | Create display status |
| `POST` | `/v1/staff/ticket/display-status/options/batch` | Get display status options by IDs |
| `POST` | `/v1/staff/ticket/display-status/page` | Page query display statuses |
| `GET` | `/v1/staff/ticket/display-status/{id}` | Get display status by ID |
| `PUT` | `/v1/staff/ticket/display-status/{id}` | Update display status |

### <a id="staff--ticket-filter-group-management"></a>Ticket Filter Group Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket/filter-group` | Create a new filter group |
| `PUT` | `/v1/staff/ticket/filter-group` | Update an existing filter group |
| `POST` | `/v1/staff/ticket/filter-group/page` | Page query filter groups |
| `DELETE` | `/v1/staff/ticket/filter-group/{id}` | Delete filter group by ID |
| `GET` | `/v1/staff/ticket/filter-group/{id}` | Get filter group by ID |

### <a id="staff--ticket-filter-job"></a>Ticket Filter Job

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/ticket/filter-job/running-info` | Get Running Job Info |
| `POST` | `/v1/staff/ticket/filter-job/start` | Start Ticket Filter Job |

### <a id="staff--ticket-filter-management"></a>Ticket Filter Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket/filter` | Create a new filter |
| `PUT` | `/v1/staff/ticket/filter` | Update an existing filter |
| `GET` | `/v1/staff/ticket/filter/fields` | List all fields that can be used in filters |
| `GET` | `/v1/staff/ticket/filter/group/{groupId}` | List filters by group ID |
| `DELETE` | `/v1/staff/ticket/filter/{id}` | Delete filter by ID |
| `GET` | `/v1/staff/ticket/filter/{id}` | Get filter by ID |

### <a id="staff--ticket-macro-management"></a>Ticket Macro Management

| Method | Path | Summary |
|--------|------|---------|
| `GET` | `/v1/staff/ticket/macros` | Query macros |
| `POST` | `/v1/staff/ticket/macros` | Create macro |
| `POST` | `/v1/staff/ticket/macros/options/batch` | Get macro options |
| `POST` | `/v1/staff/ticket/macros/page` | Query macros |
| `GET` | `/v1/staff/ticket/macros/{id}` | Get macro by ID |
| `PUT` | `/v1/staff/ticket/macros/{id}` | Update macro |

### <a id="staff--ticket-management"></a>Ticket Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/tickets` | Create ticket |
| `GET` | `/v1/staff/tickets/brief/{id}` | Get ticket brief info |
| `PUT` | `/v1/staff/tickets/bulk/department` | Update ticket department assignments in bulk |
| `PUT` | `/v1/staff/tickets/bulk/staff` | Update ticket staff assignments in bulk |
| `PUT` | `/v1/staff/tickets/bulk/status` | Update ticket status |
| `PUT` | `/v1/staff/tickets/bulk/team` | Update ticket team assignments in bulk |
| `POST` | `/v1/staff/tickets/chat-summary` | Generate chat summary for email |
| `POST` | `/v1/staff/tickets/display-status-logs` | Query display status logs |
| `POST` | `/v1/staff/tickets/export` | Export tickets |
| `POST` | `/v1/staff/tickets/exportAuditLog` | Export audit log |
| `POST` | `/v1/staff/tickets/message-processes/page` | Query ticket message processes |
| `GET` | `/v1/staff/tickets/message/{ticketMessageId}/email-headers` | Get email header information for a ticket message |
| `GET` | `/v1/staff/tickets/message/{ticketMessageId}/email-userInfo` | Get email user info information for a ticket message |
| `GET` | `/v1/staff/tickets/number/{code}` | Get ticket by number |
| `POST` | `/v1/staff/tickets/number/{ticketNumber}/timeline` | Get ticket timeline by number |
| `POST` | `/v1/staff/tickets/options/batch` | Get ticket options by IDs |
| `POST` | `/v1/staff/tickets/page` | Page query tickets |
| `POST` | `/v1/staff/tickets/reminder` | Create ticket reminder |
| `GET` | `/v1/staff/tickets/{id}` | Get ticket by ID |
| `PUT` | `/v1/staff/tickets/{id}` | Update ticket |
| `POST` | `/v1/staff/tickets/{id}/reply` | Reply to ticket |
| `POST` | `/v1/staff/tickets/{originalTicketId}/parallel` | Create parallel ticket |
| `DELETE` | `/v1/staff/tickets/{sourceId}/relate/{targetId}` | Unrelate tickets |
| `POST` | `/v1/staff/tickets/{sourceId}/relate/{targetId}` | Relate tickets |
| `POST` | `/v1/staff/tickets/{targetId}/merge` | Merge tickets |
| `PUT` | `/v1/staff/tickets/{ticketId}/department` | Update ticket department assignments |
| `POST` | `/v1/staff/tickets/{ticketId}/execute-macro/{macroId}` | Execute macro |
| `POST` | `/v1/staff/tickets/{ticketId}/follow` | Toggle ticket follow |
| `POST` | `/v1/staff/tickets/{ticketId}/force-open` | - |
| `PUT` | `/v1/staff/tickets/{ticketId}/form-entries` | Update ticket form entries |
| `GET` | `/v1/staff/tickets/{ticketId}/form-entries/{topicId}` | Get ticket form entries |
| `POST` | `/v1/staff/tickets/{ticketId}/handover` | Hand over ticket |
| `POST` | `/v1/staff/tickets/{ticketId}/messages/{messageId}/answer-status` | Update answer status |
| `PUT` | `/v1/staff/tickets/{ticketId}/messages/{messageId}/internal-note` | Update internal note message |
| `PUT` | `/v1/staff/tickets/{ticketId}/messages/{messageId}/scheduled-time` | Update scheduled send time |
| `POST` | `/v1/staff/tickets/{ticketId}/print` | Generate ticket print HTML |
| `GET` | `/v1/staff/tickets/{ticketId}/summary` | Get ticket AI summary |
| `POST` | `/v1/staff/tickets/{ticketId}/timeline` | Get ticket timeline |

### <a id="staff--ticket-priority"></a>Ticket Priority

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket/priorities` | Create a new ticket priority |
| `GET` | `/v1/staff/ticket/priorities/list` | Get all enabled ticket priorities |
| `POST` | `/v1/staff/ticket/priorities/options/batch` | Get priority options by IDs |
| `POST` | `/v1/staff/ticket/priorities/page` | Query ticket priorities with pagination |
| `GET` | `/v1/staff/ticket/priorities/{id}` | Get ticket priority details |
| `PUT` | `/v1/staff/ticket/priorities/{id}` | Update an existing ticket priority |

### <a id="staff--ticket-search"></a>Ticket Search

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/tickets/search` | Search tickets |

### <a id="staff--ticket-view-management"></a>Ticket View Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket-views` | Create ticket view |
| `POST` | `/v1/staff/ticket-views/favorites` | List favorite ticket views |
| `GET` | `/v1/staff/ticket-views/fields` | List all fields that can be used in ticket views |
| `POST` | `/v1/staff/ticket-views/ids` | Get ticket view by ID list |
| `POST` | `/v1/staff/ticket-views/list` | List accessible views |
| `DELETE` | `/v1/staff/ticket-views/{id}` | Delete ticket view |
| `GET` | `/v1/staff/ticket-views/{id}` | Get ticket view by ID |
| `PUT` | `/v1/staff/ticket-views/{id}` | Update ticket view |
| `DELETE` | `/v1/staff/ticket-views/{id}/favorite` | Unfavorite a ticket view |
| `POST` | `/v1/staff/ticket-views/{id}/favorite` | Favorite a ticket view |

### <a id="staff--topic-management"></a>Topic Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/topics` | Create topic |
| `POST` | `/v1/staff/topics/options/batch` | Get topic options by IDs |
| `POST` | `/v1/staff/topics/page` | Page query topics |
| `GET` | `/v1/staff/topics/{id}` | Get topic by ID |
| `PUT` | `/v1/staff/topics/{id}` | Update topic |

### <a id="staff--uf-dashboard"></a>UF Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/uf-dashboard/count` | Get UF Dashboard count statistics |
| `GET` | `/v1/staff/uf-dashboard/facility-states` | Get all distinct facility states |
| `POST` | `/v1/staff/uf-dashboard/statistics` | Get UF statistics grouped by facility and organization |
| `POST` | `/v1/staff/uf-dashboard/statistics/by-facility` | Get UF ticket statistics grouped by facility |
| `POST` | `/v1/staff/uf-dashboard/statistics/by-state` | Get UF ticket statistics grouped by facility state |
| `POST` | `/v1/staff/uf-dashboard/ticket-count-trend` | Get UF ticket count trend over time |

### <a id="staff--wfm-dashboard"></a>Wfm Dashboard

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/report/staff/productive/report` | Get staff productive report |
| `POST` | `/v1/staff/report/staff/productivity/timeline` | Get staff productivity timeline |
| `POST` | `/v1/staff/report/staff/workforce/page` | Get staff workforce page data |
| `POST` | `/v1/staff/report/staff/workforce/shift-timeline` | Get staff shift timeline data |
| `POST` | `/v1/staff/report/staff/workforce/statistic` | Get staff statistic data |
| `POST` | `/v1/staff/report/staff/workforce/ticket/activity` | Get ticket activity statistics |
| `POST` | `/v1/staff/report/staff/workforce/timeline` | Get staff workforce timeline data |

### <a id="staff--workflow-definition-management"></a>Workflow Definition Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/workflow/definition/activate/{key}` | Activate process definition by key |
| `POST` | `/v1/staff/workflow/definition/deploy` | Deploy workflow definition |
| `POST` | `/v1/staff/workflow/definition/deploy-file` | Deploy workflow definition by file |
| `POST` | `/v1/staff/workflow/definition/page` | Query process definitions |
| `POST` | `/v1/staff/workflow/definition/suspend/{key}` | Suspend process definition by key |
| `GET` | `/v1/staff/workflow/definition/{id}` | Get process definition by ID |

### <a id="staff--workflow-diagram-management"></a>Workflow Diagram Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/workflow/diagram/info` | Get workflow diagram information |

### <a id="staff--workflow-instance-management"></a>Workflow Instance Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/workflow/instances/cancel` | Cancel process instance |
| `POST` | `/v1/staff/workflow/instances/historic/page` | Query historic process instances |
| `POST` | `/v1/staff/workflow/instances/start` | Start workflow |
| `POST` | `/v1/staff/workflow/instances/tasks/complete` | Complete task |
| `POST` | `/v1/staff/workflow/instances/tasks/historic/page` | Query historic tasks |
| `POST` | `/v1/staff/workflow/instances/tasks/my-tasks/page` | Query my tasks |
| `POST` | `/v1/staff/workflow/instances/tasks/page` | Query active tasks |
| `GET` | `/v1/staff/workflow/instances/tasks/{taskId}` | Get historic task by ID |
| `GET` | `/v1/staff/workflow/instances/{processInstanceId}` | Get historic process instance by ID |

### <a id="staff--anomaly-analysis-controller"></a>anomaly-analysis-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/report/staff/workforce/exception` | - |

### <a id="staff--customer-controller"></a>customer-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/customers` | - |
| `DELETE` | `/v1/staff/customers/batch/organization` | - |
| `PUT` | `/v1/staff/customers/batch/organization` | - |
| `POST` | `/v1/staff/customers/options/batch` | - |
| `POST` | `/v1/staff/customers/page` | - |
| `GET` | `/v1/staff/customers/phone/{phone}` | - |
| `GET` | `/v1/staff/customers/{id}` | - |
| `PUT` | `/v1/staff/customers/{id}` | - |
| `PUT` | `/v1/staff/customers/{id}/password/reset` | - |

### <a id="staff--customer-organization-controller"></a>customer-organization-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/customer-organizations` | - |
| `POST` | `/v1/staff/customer-organizations/options/batch` | - |
| `POST` | `/v1/staff/customer-organizations/page` | - |
| `GET` | `/v1/staff/customer-organizations/{id}` | - |
| `PUT` | `/v1/staff/customer-organizations/{id}` | - |

### <a id="staff--facility-controller"></a>facility-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/extend/facility` | - |
| `POST` | `/v1/staff/extend/facility/options/batch` | - |
| `POST` | `/v1/staff/extend/facility/page` | - |
| `GET` | `/v1/staff/extend/facility/{id}` | - |
| `PUT` | `/v1/staff/extend/facility/{id}` | - |

### <a id="staff--roster-controller"></a>roster-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/extend/roster` | - |
| `POST` | `/v1/staff/extend/roster/page` | - |
| `GET` | `/v1/staff/extend/roster/personnel-list` | - |
| `GET` | `/v1/staff/extend/roster/running-job-info` | - |
| `POST` | `/v1/staff/extend/roster/update-job` | - |
| `DELETE` | `/v1/staff/extend/roster/{id}` | - |
| `GET` | `/v1/staff/extend/roster/{id}` | - |
| `PUT` | `/v1/staff/extend/roster/{id}` | - |

### <a id="staff--roster-primary-contact-review-controller"></a>roster-primary-contact-review-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/extend/roster/primary-contact-review/batch-confirm` | - |
| `GET` | `/v1/staff/extend/roster/primary-contact-review/contact-rules` | - |
| `GET` | `/v1/staff/extend/roster/primary-contact-review/exclude-emails` | - |
| `POST` | `/v1/staff/extend/roster/primary-contact-review/page` | - |
| `GET` | `/v1/staff/extend/roster/primary-contact-review/stats` | - |
| `POST` | `/v1/staff/extend/roster/primary-contact-review/submit` | - |
| `POST` | `/v1/staff/extend/roster/primary-contact-review/unlock/{id}` | - |

### <a id="staff--teams-channel-controller"></a>teams-channel-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/extend/teams/channel/credentials` | - |
| `GET` | `/v1/staff/extend/teams/channel/credentials/status` | - |
| `POST` | `/v1/staff/extend/teams/channel/credentials/test` | - |
| `GET` | `/v1/staff/extend/teams/channel/kb/config` | - |
| `PUT` | `/v1/staff/extend/teams/channel/kb/config` | - |
| `GET` | `/v1/staff/extend/teams/channel/kb/list` | - |
| `GET` | `/v1/staff/extend/teams/channel/oauth/callback` | - |
| `GET` | `/v1/staff/extend/teams/channel/oauth/url` | - |
| `POST` | `/v1/staff/extend/teams/channel/page` | - |
| `POST` | `/v1/staff/extend/teams/channel/sync` | - |
| `GET` | `/v1/staff/extend/teams/channel/{id}` | - |
| `PUT` | `/v1/staff/extend/teams/channel/{id}/enabled` | - |

### <a id="staff--ticket-escalation-controller"></a>ticket-escalation-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket-escalations` | - |
| `GET` | `/v1/staff/ticket-escalations/ticket/{ticketId}/channels` | - |
| `GET` | `/v1/staff/ticket-escalations/ticket/{ticketId}/current` | - |
| `GET` | `/v1/staff/ticket-escalations/ticket/{ticketId}/list` | - |
| `GET` | `/v1/staff/ticket-escalations/ticket/{ticketId}/summary/stream` | - |
| `GET` | `/v1/staff/ticket-escalations/{ticketEscalationId}/messages` | - |
| `POST` | `/v1/staff/ticket-escalations/{ticketEscalationId}/reply` | - |

### <a id="staff--ticket-side-conversation-controller"></a>ticket-side-conversation-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/ticket/side-conversations` | - |
| `POST` | `/v1/staff/ticket/side-conversations/reply` | - |
| `GET` | `/v1/staff/ticket/side-conversations/ticket/{ticketId}` | - |
| `GET` | `/v1/staff/ticket/side-conversations/{id}` | - |
| `POST` | `/v1/staff/ticket/side-conversations/{sideConversationId}/messages` | - |

### <a id="staff--user-info-controller"></a>user-info-controller

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/staff/user/batch-parse-and-create` | - |
| `GET` | `/v1/staff/user/search` | - |

---
## <a id="source-tenant"></a>TENANT

### <a id="tenant--tenant-management"></a>Tenant Management

| Method | Path | Summary |
|--------|------|---------|
| `POST` | `/v1/tenant/tenants` | Create tenant |
| `POST` | `/v1/tenant/tenants/batch` | Get tenants by IDs |
| `GET` | `/v1/tenant/tenants/domain-available` | Check domain availability |
| `GET` | `/v1/tenant/tenants/domain/{domain}` | Get tenant by domain |
| `GET` | `/v1/tenant/tenants/enabled` | Get all enabled tenants |
| `POST` | `/v1/tenant/tenants/page` | Page query tenants |
| `DELETE` | `/v1/tenant/tenants/{id}` | Delete tenant |
| `GET` | `/v1/tenant/tenants/{id}` | Get tenant by ID |
| `PUT` | `/v1/tenant/tenants/{id}` | Update tenant |
