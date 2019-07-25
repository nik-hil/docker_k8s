# Kubernetes tutorial

# Docker hub 
https://cloud.docker.com/u/nikhil101/repository/docker/nikhil101/django-k8s

# checkout each tag

1. pods-creation
1. pods-replication

# Service

## Via NodePort
https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/
Deploy pods_nodeport.yml
```
kubectl expose deployment hello-world --type=NodePort --name=example-service
```
In GKE, Services & Incress (page) -> Port -> Port forwarding

## Via Loadbalancer
https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/

Deploy pods_loadbalancer.yml

```
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service
```

