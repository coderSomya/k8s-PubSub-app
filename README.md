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
kubectl apply -f kubernetes/kafka/zookeeper-deployment.yaml
kubectl apply -f kubernetes/kafka/kafka-deployment.yaml
```

## Deploy Postgres
```
kubectl apply -f kubernetes/postgres/postgres-deployment.yaml
```

## Build and Deploy Services
```
cd order-service && ./build.sh && cd ..
cd consumer-service && ./build.sh && cd ..
cd transaction-service && ./build.sh && cd ..
cd analytics-service && ./build.sh && cd ..
cd notification-service && ./build.sh && cd ..
```
