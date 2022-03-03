.PHONY: plan apply clean

all: clean setup apply

clean:
        @echo "Clean"

setup:
        docker build -t robertwijntjes/fast-api:1.0.0 .
		minikube start 
		minikube cache add robertwijntjes/fast-api:1.0.0
		helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
		helm repo update


apply:
		kubectl apply -f api.yaml --namespace=fast-api
		kubectl port-forward service/fast-api-svc 8080 --namespace=fast-api
		kubectl port-forward service/prometheus-prometheus-node-exporter 9100   --namespace=prometheus
		kubectl port-forward service/prometheus-operated  9090 --namespace=prometheus
		kubectl port-forward deployment/prometheus-grafana 3000 --namespace=prometheus