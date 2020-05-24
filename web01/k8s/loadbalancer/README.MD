# Pods running with loadbalancer service on GKE

Create a service with deployment.
```
kubectl apply -f pods_deployment.yml
kubectl apply -f pods_svc.yml
```

Get service and endpoint details 
```
kubectl describe services 
kubectl get svc
```

```
$ kubectl get svc
NAME                TYPE           CLUSTER-IP   EXTERNAL-IP     PORT(S)          AGE
django-k8s-svc      LoadBalancer   10.8.3.208    34.72.51.238     80:31002/TCP   2m9s

 kubectl describe service django-k8s-svc
Name:                     django-k8s-svc
Namespace:                default
Labels:                   <none>
Annotations:              Selector:  app=web
Type:                     LoadBalancer
IP:                       10.8.3.208
LoadBalancer Ingress:     34.72.51.238
Port:                     <unset>  8000/TCP
TargetPort:               8000/TCP
NodePort:                 <unset>  30558/TCP
Endpoints:                10.4.0.8:8000,10.4.2.5:8000
Session Affinity:         None
External Traffic Policy:  Cluster
Events:
  Type    Reason                Age                 From                Message
  ----    ------                ----                ----                -------
  Normal  EnsuringLoadBalancer  113s (x3 over 15m)  service-controller  Ensuring load balancer
  Normal  EnsuredLoadBalancer   69s (x3 over 15m)   service-controller  Ensured load balancer
```

It takes some time to populate EXTERNAL-IP. We can see website running at EXTERNAL-IP:80
