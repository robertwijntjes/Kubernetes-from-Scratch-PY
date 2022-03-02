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

## Checking the Results
##### Checking the minikube dashboard
```
minikube dashboard
```

##### Checking the endpoint
![image](https://user-images.githubusercontent.com/15350162/156442467-13c449f7-f37a-43a5-be12-98c840522358.png)

