__Prerequisites__:
- Docker
- Minikube

# Get started:

## Start minikube
```
minikube start
```

## Deploy kafka
```
kubectl apply -f k8s/kafka/zookeeper-deployment.yaml
kubectl apply -f k8s/kafka/kafka-deployment.yaml
```

## Deploy Postgres
```
kubectl apply -f k8s/postgres/postgres-deployment.yaml
```

## Build and Deploy Services
```
cd order-service && ./build.sh && cd ..
cd consumer-service && ./build.sh && cd ..
cd transaction-service && ./build.sh && cd ..
cd analytics-service && ./build.sh && cd ..
cd notification-service && ./build.sh && cd ..
```
