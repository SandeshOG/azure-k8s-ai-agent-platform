#!/bin/bash
# Deployment script by Sandesh Lanjewar
set -e

echo "Building image..."
docker build -t azure-k8s-ai-agent-platform:latest .

echo "Applying manifests..."
kubectl apply -f k8s/

echo "Done. Check status: kubectl get pods -l app=ai-agent-platform"