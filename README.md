# Kubernetes-hosting-Python-api-container

### Requirements
In order to get this to work there are a few prerequisites:
* Minikube
* Kubectl
* Docker

### Steps for Replication
##### Build the Image
```
docker build -t robertwijntjes/fast-api:1.0.0 .
```
##### Test Locally
```
docker run -p 8080:8080 --name fastapi robertwijntjes/fast-api:1.0.0
```
##### Minikube
```
minikube start
minikube cache add robertwijntjes/fast-api:1.0.0

```

### Kubernetes
```
kubectl apply -f api.yaml
kubectl port-forward service/fast-api-svc 8080

```
