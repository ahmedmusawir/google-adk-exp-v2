#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# 1. Check if an agent name was provided as an argument.
if [ -z "$1" ]; then
  echo "❌ Error: No agent name provided."
  echo "Usage: ./deploy.sh <agent_name>"
  echo "Example: ./deploy.sh greeting_agent"
  exit 1
fi

AGENT_NAME=$1
AGENT_PATH="simple/$AGENT_NAME"
SERVICE_NAME=$(echo "$AGENT_NAME" | tr '_' '-')-service

# 2. Verify that the agent directory actually exists.
if [ ! -d "$AGENT_PATH" ]; then
  echo "❌ Error: Agent directory '$AGENT_PATH' not found."
  exit 1
fi

# 3. Announce the deployment plan.
echo "🚀 Beginning deployment for agent: $AGENT_NAME"
echo "   Project: $GOOGLE_CLOUD_PROJECT"
echo "   Region: $GOOGLE_CLOUD_LOCATION"
echo "   Service Name: $SERVICE_NAME"
echo "   Source Path: $AGENT_PATH"
echo "--------------------------------------------------"

# 4. Run the specialized ADK deployment command.
adk deploy cloud_run \
  --project="$GOOGLE_CLOUD_PROJECT" \
  --region="$GOOGLE_CLOUD_LOCATION" \
  --service_name="$SERVICE_NAME" \
  --with_ui \
  --port=8080 \
  "$AGENT_PATH"

# 4. Run the specialized ADK deployment command.
# adk deploy cloud_run \
#   --project="$GOOGLE_CLOUD_PROJECT" \
#   --region="$GOOGLE_CLOUD_LOCATION" \
#   --service_name="$SERVICE_NAME" \
#   --with_ui \
#   "$AGENT_PATH"

echo "--------------------------------------------------"
echo "✅ Base deployment completed successfully!"