# Kubernetes-hosting-Python-api-container

### Requirements
In order to get this to work there are a few prerequisites:
* [Minikube](https://phoenixnap.com/kb/install-minikube-on-ubuntu)
* [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
* [Docker](https://docs.docker.com/engine/install/ubuntu/)
* [Helm](https://helm.sh/docs/intro/install/)
* Ubuntu, but you can just make small changes and it will work.


### Recommended way for Replication
##### 1. Using the makefile:
###### Check for errors, as without this passing, the rest won't work
```
make plan
```

###### Builds the cluster
```
make setup
```

###### Provisions resources in the cluster
```
make apply
```
##### 2. Port Forwarding
```
kubectl port-forward service/prometheus-prometheus-node-exporter 9100   --namespace=prometheus
kubectl port-forward service/prometheus-operated  9090 --namespace=prometheus
kubectl port-forward deployment/prometheus-grafana 3000 --namespace=prometheus
kubectl port-forward service/fast-api-svc 8080 --namespace=fast-api
```
### Manual Steps for Replication
###### Build the Image
```
docker build -t robertwijntjes/fast-api:1.0.0 .
```
###### Start the Minikube cluster and add image
```
minikube start 
minikube cache add robertwijntjes/fast-api:1.0.0
```

###### Apply Kubernetes charts to the cluster
```
kubectl apply -f namespace.yaml
kubectl apply -f api.yaml -n=fast-api
```
###### Add Helm Repo 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
###### Apply [Helm Chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) to the cluster
```
helm install prometheus prometheus-community/kube-prometheus-stack --namespace=prometheus --create-namespace --wait
```

##### Add Port Forward
- Prometheus node Exporter      
`kubectl port-forward service/prometheus-prometheus-node-exporter 9100   --namespace=prometheus`        
- Prometheus UI    
`kubectl port-forward service/prometheus-operated  9090 --namespace=prometheus`  
- Prometheus Grafana   
`kubectl port-forward deployment/prometheus-grafana 3000 --namespace=prometheus`
- Fast-Api Server   
`kubectl port-forward service/fast-api-svc 8080 --namespace=fast-api`

### Checking the Results
###### Checking the minikube dashboard
```
minikube dashboard
```
###### Testing the image locally
```
docker run -p 8080:8080 --name fastapi robertwijntjes/fast-api:1.0.0
```

##### Checking the endpoint
###### Fast-Api Server
![image](https://user-images.githubusercontent.com/15350162/156442467-13c449f7-f37a-43a5-be12-98c840522358.png)
###### Prometheus
![image](https://user-images.githubusercontent.com/15350162/156640290-6fe9dbd5-1db5-46ea-bf5f-796c783ad4c9.png)
###### Metrics Page
![image](https://user-images.githubusercontent.com/15350162/156640365-53b539b8-af03-49bc-bfc5-ecddf03e4b4d.png)
###### Grafana
![image](https://user-images.githubusercontent.com/15350162/156640391-6791e566-db67-4a90-a164-cda7a40b1a1d.png)


