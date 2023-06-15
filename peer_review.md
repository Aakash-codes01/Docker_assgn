# PEER REVIEW 

## peer name

### Ashish chouhan
 
### Docker Assignment

- first created a custom docker file where he used airlfow as a base image and install psycopg in it <br>
- then created a docker compose file where he mentioned build for his docker file <br>
- then created a dag in dags folder and mounted it in the airlfow <br>
- In his dag he used psycopg to create connection between postgres and airflow container for executing his tasks <br>


### Kubernetes Assignment

- Made a custom docker image for postgres with airflow installed in it. The container made from this image will be used as a database for airflow and also to store dag execution data in a table. 
- published that custom docker image onto docker hub
- in the custom image he used a base postgres image and installed python in it and installed airflow in it
- Then installed minikube 
- and started a local cluster
- created deployments for postgres pod
- get inside the pod and initialed the db for airflow
- created a service for postgres
- created his dag
- started the airlfow service 
- accessed the web ui
- created the connection and trigerred the dag


## peer name

### Ankit kumar

### Docker Assignment

- Included all dependecies in docker-compose.yaml file
- created connection with postgres from airlfow web ui
- imported required module
- Created dag with all required parameter
- Created CREATE_TABLE TASK with using postgresOpreator

### Kubernetes Assignment

- installed minikube to make a kubernetes cluster.
- with the help of postgres-deployment.yaml file, created the pod containing postgres container 
- run below command to initialise the database and make a user.
-  created service of type clusterIP by running postgres-service.yaml to give access to postgres pods inside the cluster.
- kubectl apply -f postgres-service.yaml
- used the airflow-deployment.yaml file,the pod containing airflow container will be created
- Created a service of type loadbalancer by running airflow-service.yaml to access airflow webserver from my local system .
- kubectl apply -f airflow-service.yaml
- created docker_dag as time_task.py inside airflow scheduler
 


 
 
