#!/usr/bin/env bash
set -euo pipefail

repo_url="https://github.com/flop-labs/technocore-chat.git"
commit="53079408c1581f46eff6acbf6e2eada289d4332c"
workdir="${1:-technocore-chat-audit}"

if ! command -v uv >/dev/null 2>&1; then
  printf 'error: uv is required: https://docs.astral.sh/uv/\n' >&2
  exit 1
fi

if [[ -e "$workdir" ]]; then
  printf 'error: refusing to overwrite existing path: %s\n' "$workdir" >&2
  exit 1
fi

git clone "$repo_url" "$workdir"
cd "$workdir"
git checkout "$commit"

uv sync --frozen
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run coverage run -m pytest tests -q
uv run coverage report

requirements_file="$(mktemp)"
trap 'rm -f "$requirements_file"' EXIT
uv export --frozen --no-dev --format requirements-txt > "$requirements_file"
if command -v pip-audit >/dev/null 2>&1; then
  pip-audit -r "$requirements_file"
else
  printf 'note: pip-audit not installed; dependency vulnerability check skipped\n' >&2
fi

if command -v bandit >/dev/null 2>&1; then
  # Bandit uses a non-zero status when it reports findings. Preserve the report
  # without confusing expected audit findings with a broken reproduction run.
  bandit_status=0
  bandit -r src mcp/src scripts || bandit_status=$?
  printf 'bandit exit status: %s (review every reported finding)\n' "$bandit_status"
else
  printf 'note: bandit not installed; static security scan skipped\n' >&2
fi

printf '\nAudit reproduction complete for %s\n' "$commit"
