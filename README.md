# Kubernetes-hosting-Python-api-container

### Requirements
In order to get this to work there are a few prerequisites:
* Minikube
* Kubectl
* Docker
* Helm

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

### Grafana and Prometheus
##### Add Helm Repo 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
##### Install Prometheus Stack
- prometheus-community/kube-state-metrics
- prometheus-community/prometheus-node-exporter
- grafana/grafana
  
https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

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

### Checking the Results
##### Checking the minikube dashboard
```
minikube dashboard
```

##### Checking the endpoint
![image](https://user-images.githubusercontent.com/15350162/156442467-13c449f7-f37a-43a5-be12-98c840522358.png)
![image](https://user-images.githubusercontent.com/15350162/156640290-6fe9dbd5-1db5-46ea-bf5f-796c783ad4c9.png)
![image](https://user-images.githubusercontent.com/15350162/156640365-53b539b8-af03-49bc-bfc5-ecddf03e4b4d.png)
![image](https://user-images.githubusercontent.com/15350162/156640391-6791e566-db67-4a90-a164-cda7a40b1a1d.png)


