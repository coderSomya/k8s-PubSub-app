#!/bin/bash

docker build -t analytics-service:latest .
kubectl apply -f ../k8s/analytics-service-deployment.yaml

