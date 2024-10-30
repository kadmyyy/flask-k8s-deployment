1. Clone the repository:

bash

git clone https://github.com/kadmyyy/projet-docker_api.git
cd projet-docker_api

2- Build and push the Docker images (if not already done):

bash

docker build -t your-docker-username/api:latest -f Dockerfile .
docker push your-docker-username/api:latest

3- Navigate to the Kubernetes folder:

bash

cd k8s

4- Apply the Kubernetes manifests:

bash

kubectl apply -f backend-configmap.yaml
kubectl apply -f backend-secret.yaml
kubectl apply -f database-configmap.yaml
kubectl apply -f database-secret.yaml
kubectl apply -f database-deployment.yaml
kubectl apply -f database-service.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f backend-service.yaml

5- Access the API:

    Forward the port to localhost:

    bash

kubectl port-forward service/backend-service 5000:5000

Open your browser and go to http://localhost:5000/.