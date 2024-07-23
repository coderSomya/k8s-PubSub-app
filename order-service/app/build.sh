#!/bin/bash

docker build -t order-service:latest .
kubectl apply -f ../k8s/order-service-deployment.yaml

