.PHONY: plan apply clean

all: plan setup apply

plan:
	@echo "Checking prerequisites for execution"
	@minikube version
	@kubectl version  --client
	@docker version
	@helm version

setup:
	@docker build -t robertwijntjes/fast-api:1.0.0 .
	@minikube start 

apply:
	@echo "Appling to Cluster"
	@kubectl apply namespace.yml
	@kubectl apply -f api.yaml -n=fast-api
	@helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	@helm repo update
	@helm install prometheus prometheus-community/kube-prometheus-stack --namespace=prometheus --create-namespace --wait
	@kubectl port-forward service/prometheus-prometheus-node-exporter 9100   --namespace=prometheus
	@kubectl port-forward service/prometheus-operated  9090 --namespace=prometheus
	@kubectl port-forward deployment/prometheus-grafana 3000 --namespace=prometheus
	@kubectl port-forward service/fast-api-svc 8080