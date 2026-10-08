#!/usr/bin/env bash
# Portable equivalent of the executed command; supply the existing Python environment.
set -euo pipefail
python_bin="${1:-python3}"
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
env -i \
  PATH=/usr/local/bin:/usr/bin:/bin LANG=C.UTF-8 PYTHONDONTWRITEBYTECODE=1 \
  DD_TRACE_ENABLED=false DD_INSTRUMENTATION_TELEMETRY_ENABLED=false \
  DD_REMOTE_CONFIGURATION_ENABLED=false DD_DYNAMIC_INSTRUMENTATION_ENABLED=false \
  DD_SYMBOL_DATABASE_UPLOAD_ENABLED=false DD_PROFILING_ENABLED=false \
  DD_APPSEC_ENABLED=false DD_IAST_ENABLED=false DD_LLMOBS_ENABLED=false \
  "$python_bin" "$script_dir/reproduce.py"
