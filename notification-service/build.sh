docker build --no-cache -t notification-service:latest .
kubectl apply -f ../k8s/notification-service-deployment.yaml

