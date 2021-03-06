# Pods running with container port on GKE

Create a service with deployment.
```
kubectl apply -f pods_containerport_deployment.yml
kubectl apply -f pods_containerport_svc.yml
```

Get service and endpoint details 
```
kubectl describe services 
kubectl get ep coontainer-port-svc
```

```
$ kubectl get ep coontainer-port-svc
NAME                  ENDPOINTS                      AGE
coontainer-port-svc   10.4.1.6:8000,10.4.2.11:8000   48m
```

if we try to connect this socket it will not connect.
```
$ curl 10.4.1.6:8000
curl: (7) Failed to connect to 10.4.1.6 port 8000: Connection refused
```

we are running this from machine which has different IP other than cluster. If we run this command from inside of cluster it will be successful.
We but cannot do that.
But we can do port forwarding.

 - On chosen node, create a firewall rule that allows TCP traffic on your node port
 - at least in GKE, `kubectl port-forward $(kubectl get pod --selector="app=web" --output jsonpath='{.items[0].metadata.name}') 8080:8000`
   - then click on web preview on port 8080

e.g,
```
$(kubectl get pod --selector="app=web" --output jsonpath='{.items[0].metadata.name}') 8080:8000
Forwarding from 127.0.0.1:8080 -> 8000
Handling connection for 8080
Handling connection for 8080
Handling connection for 8080
Handling connection for 8080
```

![web preview on 8080](./8080.png)
