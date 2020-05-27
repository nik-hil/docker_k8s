# Kubernetes tutorial

# Docker hub 
https://cloud.docker.com/u/nikhil101/repository/docker/nikhil101/django-k8s

# checkout each tag

1. pods-creation
1. pods-replication

# Replicaset

You create a pod and create replicaset
```
kubectl create -f pods.yml
kubectl create -f pods_replica_run_with_pods.yml
```

Or you can create a replicaset which will create desired no of pods.
```
kubectl create -f pods_replica.yml
```


# Service

## Via containerPort

See, [containerPort](./web01/k8s/container_port/README.MD) & [Kubernetes site](https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/#creating-a-service-for-an-application-running-in-two-pods)

## Via NodePort
https://kubernetes.io/docs/tasks/access-application-cluster/service-access-application-cluster/
Deploy pods_nodeport.yml
```
kubectl expose deployment hello-world --type=NodePort --name=example-service
```
In GKE, Services & Incress (page) -> Port -> Port forwarding

## Via Loadbalancer

See [this](https://github.com/nik-hil/docker_k8s/blob/master/web01/k8s/loadbalancer/README.MD)

https://kubernetes.io/docs/tutorials/stateless-application/expose-external-ip-address/


# BLUE GREEN Deployment

[Go to folder](https://github.com/nik-hil/docker_k8s/tree/master/web01/k8s/blue_green_deployment)

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

# Ingress Conroller (nginx)

```
kubectl apply -f pods_node.yml

kubectl expose deployment hello-world --type=NodePort --name=node-svc

kubectl apply -f pods_nodeport_ingress.yml
```

This will create a ingress controller but we cannot access it.

Create an ingress loadbalancer, https://kubernetes.github.io/ingress-nginx/deploy/#prerequisite-generic-deployment-command


# For GCP
Internet is full with example which works perfectly on minikube. But having ingress on minikube is not same as on cloud. Public IP doesnot exist on minikube. Which is big missing part.

Easiest working example with public IP, is at https://cloud.google.com/kubernetes-engine/docs/tutorials/configuring-domain-name-static-ip#config-connector_1




