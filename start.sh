#!/bin/bash

kubectl apply -f myapp/flask/flask.yaml
kubectl apply -f myapp/flask/gateway.yaml
kubectl apply -f myapp/flask/external.yaml
kubectl apply -f myapp/nginx/nginx.yaml
kubectl apply -f myapp/nginx/gateway.yaml