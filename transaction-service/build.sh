#!/bin/bash

docker build -t transaction-service:latest .
kubectl apply -f ../k8s/transaction-service-deployment.yaml

