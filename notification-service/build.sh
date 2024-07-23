docker build -t notification-service:latest .
kubectl apply -f ../k8s/notification-service-deployment.yaml

