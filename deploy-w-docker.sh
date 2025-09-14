#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

SERVICE_NAME="greeting-agent-service"

echo "🚀 Beginning deployment for service: $SERVICE_NAME"
echo "   Using gcloud run deploy for full control..."
echo "--------------------------------------------------"

gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --allow-unauthenticated \
  --set-env-vars="GOOGLE_API_KEY=AIzaSyAvNyVK8eU-RtASg-6A8isZq5rXOIRo9L8"

echo "--------------------------------------------------"
echo "✅ If there are no errors above, the deployment is complete!"