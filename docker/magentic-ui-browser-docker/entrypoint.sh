#!/usr/bin/env bash
set -e

umask 000

if ! command -v magentic-ui >/dev/null 2>&1; then
    echo "Installing Magentic-UI..."
    pip install -e /workspace
fi

exec "$@"