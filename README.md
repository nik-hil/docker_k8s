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

Command line to expose deployment
```
kubectl expose deployment hello-world --type=LoadBalancer --name=my-service
```
Or use file, pods_loadbalancer_svc.yml

# BLUE GREEN Deployment

Deploy blue.yml & blue_svc.yml. Connect the service,
```
kubectl describe svc bg-service
```

Deploy green.yml. Check the pod list
```
kubectl get pods -o wide
```
Connect the service. It is pointing towards blue.

Deploy green_svc.yml. Connect the service. It is pointing towards green.




