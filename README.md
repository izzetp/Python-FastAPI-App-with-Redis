## Python-FastAPI-App-with-Redis

# FastAPI App with Redis on Kubernetes

---

## Prerequisites

Ensure the following are installed and configured on your machine:

* [Docker](https://www.docker.com/)
* [Minikube](https://minikube.sigs.k8s.io/)
* [kubectl](https://kubernetes.io/docs/tasks/tools/)
* A [Docker Hub](https://hub.docker.com/) account (and you're logged in via `docker login`)

---

## Deployment Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Python-FastAPI-App-with-Redis.git
cd Python-FastAPI-App-with-Redis
```

---

### 2. Build and Push Docker Image

Build your FastAPI Docker image from the `src/` directory and push it to Docker Hub:

```bash
minikube start

cd src
docker build -t <your-dockerhub-username>/fastapi-app:latest .
docker push <your-dockerhub-username>/fastapi-app:latest
cd ..
```

> Replace `<your-dockerhub-username>` with your actual Docker Hub username.

---

### 3. Apply Redis manifests


```bash

kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml

```

---

### 4. Deploy the FastAPI App

Substitute your DockerHub username into the deployment file and apply it.

**On Windows (PowerShell):**

```powershell
(Get-Content fastapi-deployment.yaml) -replace '\$\{DOCKER_USERNAME\}', '<your-dockerhub-username>' | kubectl apply -f -
```

**On Linux/macOS:**

```bash
export DOCKER_USERNAME=<your-dockerhub-username>
envsubst < fastapi-deployment.yaml | kubectl apply -f -
```

---

### 5. Create FastAPI Service

Apply the FastAPI service YAML:

```bash
kubectl apply -f fastapi-service.yaml
```

---

### 6. Access the Application

Expose the FastAPI service using Minikube:

```bash
minikube service fastapi-service
```

This will open the FastAPI app in your browser.

You can also test it manually:

```
http://127.0.0.1:<PORT>/weather/London
```

---

## Verifying the Setup

Check if all pods are running:

```bash
kubectl get pods
```

View logs of the FastAPI pod (replace with actual pod name):

```bash
kubectl logs <fastapi-pod-name>
```

---
