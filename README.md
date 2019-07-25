# Kubernetes tutorial

# Docker hub 
https://cloud.docker.com/u/nikhil101/repository/docker/nikhil101/django-k8s

# checkout each tag

1. pods-creation
1. pods-replication

# Service
service created. Service not accessible.
Execute pods_port.yml & pods_svc.yaml

# Deployment
https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/
run kubernetes_dep.yml & 
```
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service
```

