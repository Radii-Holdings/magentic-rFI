#!/bin/bash
set -e

echo "Starting services..."
echo "DISPLAY=$DISPLAY"

# Ensure default ports are set if not provided at runtime
NO_VNC_PORT=${NO_VNC_PORT:-6080}
PLAYWRIGHT_PORT=${PLAYWRIGHT_PORT:-37367}

# Start supervisord to manage all processes
exec supervisord -c /etc/supervisor/conf.d/supervisord.conf
