#!/usr/bin/env bash
# source scripts/setup-local-env.sh
set -euo pipefail

if [[ -n "${ZSH_VERSION:-}" ]]; then
  SCRIPT_PATH="${(%):-%N}"
elif [[ -n "${BASH_VERSION:-}" ]]; then
  SCRIPT_PATH="${BASH_SOURCE[0]}"
else
  SCRIPT_PATH="$0"
fi

SCRIPT_DIR="$(cd "$(dirname "${SCRIPT_PATH}")" && pwd)"
ROOT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
ENV_FILE="${ROOT_DIR}/.env.mock"
EXAMPLE_FILE="${ROOT_DIR}/.env.mock.example"

usage() {
  cat <<'EOF'
Usage:
  source scripts/setup-local-env.sh
  source scripts/setup-local-env.sh /path/to/custom.env

This script must be sourced so the exported variables stay in the current shell.

Behavior:
  - Loads variables from .env.mock by default
  - Falls back to .env.mock.example if .env.mock does not exist
  - Exports the variables for the current shell session

Expected variables:
  TICKETS_BASE_URL
  TICKETS_TOKEN
  TICKETS_TIMEZONE
  TENANT_ID
  SYSTEM_LANGUAGE
  MODE
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  return 0 2>/dev/null || exit 0
fi

is_sourced=0
if [[ -n "${ZSH_VERSION:-}" ]]; then
  case "${ZSH_EVAL_CONTEXT:-}" in
    *:file) is_sourced=1 ;;
  esac
elif [[ -n "${BASH_VERSION:-}" ]]; then
  if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    is_sourced=1
  fi
fi

if [[ ${is_sourced} -ne 1 ]]; then
  echo "This script must be sourced, not executed." >&2
  echo "Use: source scripts/setup-local-env.sh" >&2
  exit 1
fi

if [[ $# -gt 1 ]]; then
  usage >&2
  return 1
fi

if [[ $# -eq 1 ]]; then
  ENV_FILE="$1"
fi

if [[ ! -f "${ENV_FILE}" ]]; then
  if [[ "${ENV_FILE}" == "${ROOT_DIR}/.env.mock" && -f "${EXAMPLE_FILE}" ]]; then
    echo "No .env.mock found, loading ${EXAMPLE_FILE} instead." >&2
    ENV_FILE="${EXAMPLE_FILE}"
  else
    echo "Env file not found: ${ENV_FILE}" >&2
    return 1
  fi
fi

set -a
# shellcheck disable=SC1090
source "${ENV_FILE}"
set +a

get_var_value() {
  local name="$1"
  if [[ -n "${ZSH_VERSION:-}" ]]; then
    printf '%s' "${(P)name-}"
  else
    printf '%s' "${!name-}"
  fi
}

required_vars=(
  TICKETS_BASE_URL
  TICKETS_TOKEN
  TICKETS_TIMEZONE
  TENANT_ID
  SYSTEM_LANGUAGE
  MODE
)

missing_vars=()
for var_name in "${required_vars[@]}"; do
  if [[ -z "$(get_var_value "${var_name}")" ]]; then
    missing_vars+=("${var_name}")
  fi
done

if [[ ${#missing_vars[@]} -gt 0 ]]; then
  echo "Loaded ${ENV_FILE}, but required variables are missing: ${missing_vars[*]}" >&2
  return 1
fi

echo "Loaded local mock environment from ${ENV_FILE}" >&2
echo "TICKETS_BASE_URL=${TICKETS_BASE_URL}" >&2
echo "TICKETS_TIMEZONE=${TICKETS_TIMEZONE}" >&2
echo "TENANT_ID=${TENANT_ID}" >&2
echo "SYSTEM_LANGUAGE=${SYSTEM_LANGUAGE}" >&2
echo "MODE=${MODE}" >&2
echo "TICKETS_TOKEN=[set]" >&2
