#!/bin/bash

docker build -t consumer-service:latest .
kubectl apply -f ../k8s/consumer-service-deployment.yaml

