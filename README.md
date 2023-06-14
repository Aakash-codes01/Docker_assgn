# Docker_assgn


## 1) Create a dag with following tasks:
- Task to create a simple table
- Task to insert few custom values in to the created table in previous step.
- Task to select the values from the table

I have created a table as records, added few values into it and then using command line, we can see values inserted into the table.
I have also created a postgres connection for connecting with postgres.

<img width="1440" alt="Screenshot 2023-05-11 at 9 11 16 PM" src="https://github.com/Aakash-codes01/Airflow_assignment/assets/123653783/f2479861-6943-460b-944e-08e71f91a826">

<img width="1440" alt="Screenshot 2023-05-11 at 9 20 01 PM" src="https://github.com/Aakash-codes01/Airflow_assignment/assets/123653783/3b52ac59-220a-4067-b971-1af3b65f09bc">


# Kubernetes assgn

- firstly Installed minikube for creating a local kubernetes cluster that will contain all my pods . <br>
- used the following commands for installations
  `brew install minikube`<br>
- started a minikube cluster
  `minikube start`<br>
  
- Created a postgres deployment for creating a pod  <br>
  `kubectl apply -f post-deployment.yaml` <br>
  
- for making the postgres pod as a metadata db for airflow airflow init command needs to be executed but it requires python and airflow Added dependencies of python and airflow in a postgres image by using the following commands inside the postgres pod.
  `apt-get -y update`<br>
  `apt-get  -y install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget`<br>
  `wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tgz`<br>
  `tar -xf Python-3.7.12.tgz`<br>
  `cd /Python-3.7.12`<br>
  `./configure --enable-optimizations`<br>
  `make -j $(nproc)`<br>
  `make altinstall`<br>
  `apt-get install libpq-dev`<br>
  `pip3.7 install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"`<br>
  `airflow db init` <br>
  `airflow users create -u airflow -p airflow -f akash -l singhal -e akashSinghal@gmail.com -r Admin` <br>
 
- to make the pod accessible from other pods made a postgres-service.yaml and created a service using <br>
  `kubectl apply -f post-service.yaml` <br>
- created an airflow deployment for making an airlfow pod <br>
  `kubectl apply -f airflow-deployment.yaml` <br>
- similarly for airflow to be accessible created a service for airflow <br>
  `kubectl apply -f airflow-service.yaml` <br>
  
- Now to create a dag i use minkube ssh command and then docker ps for listing all the conatiner filnally get inside the airlfow scheduler and inserted a dag from first question   <br>
- started the airflow service and accessed the web ui trigreed the dag and get the output <br>

  
- Results in table : <br>
  <img width="379" alt="Screenshot 2023-06-14 at 12 52 26 PM" src="https://github.com/aroraarin/DockerAndKubernetes/assets/122515163/a04f1d52-54f8-4aa2-9955-0a381ab39851">

  
  





