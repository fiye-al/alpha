#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="project_alpha"
DOCKER_TAG="fiye-al/$IMAGE_NAME:latest"

echo "=== Building Docker image $DOCKER_TAG ==="
docker build -t "$DOCKER_TAG" .

echo "=== Pushing to Docker Hub ==="
docker push "$DOCKER_TAG"

echo "=== Deployment complete ==="
