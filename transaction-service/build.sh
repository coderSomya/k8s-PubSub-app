#!/bin/bash

docker build --no-cache -t transaction-service:latest .
kubectl apply -f ../k8s/transaction-service-deployment.yaml

