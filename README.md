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