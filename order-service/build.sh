#!/bin/bash

docker build --no-cache -t order-service:latest .
kubectl apply -f ../k8s/order-service-deployment.yaml

