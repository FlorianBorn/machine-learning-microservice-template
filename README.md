# machine-learning-microservice-template

## Project
The goal of this project is to propose a machine learning template for simple machine learning use cases.

Typical roles which are involved in devoloping and deploying a machine learning model are Data Engineers, Data Scientists and ML-Engineers.
Data Engineers connect different data sources and make the data easily accessible to the Data Scientist, who uses the Data to develop the final model architecure. After the Data Scientist is happy with the performance of the model, it is ready to be deployed to production. The ML-Engineer then takes the model and bakes it into a web service and deploys it to production.

This machine learning lifecycle (which is heavily inspired by uber) shows the process from defining the machine learning problem to operate the model in production.
![alt text](docs/ml-lifecycle.png "Machine Learning Lifecycle")

The idea is to have a reusable project and code structure
This template is comprised of 2 sub-templates. 
This first sub-template is about how to organize the code, which is created during the creation of the machine learning model.
The second sub-template is about deploying the model as microservice.

This project also serves as capstone project of Udacity's Cloud DevOps Nanodegree.

## Files & Folders
**ansible**: contains all files, which are required to setup the initial infrastructure  
**dockerfiles**: contains Dockerfiles and build scripts to build a runtime image which is used in the deployment pipelines and the production image which  contains the final web service  
**docs**: contains files/images used for documentation  
**helm**: contains a helm chart, which is used to deploy the web service to a kubernetes cluster  
**jenkins**: contains all Jenkinsfiles and required helper files which are needed during each stage  
**model_bin**: contains the model binary  
**tests**: contains test requests  
**utils**: contains the source code to build the model  
**main.py**: the web service  


## Project Setup
### Infrastructure & Tools
![alt text](docs/ml-template-project-architecture.png "Infrastructure Setup")
Github will serve as single source of truth. 
Jenkins is used as CI/CD Tool. This project contains 3 Jenkinspipelines. The first one will train a machine learning model. The second one
Jenkins is used as CI/CD Tool, which is linked to github. It gets all neccessary files from there and runs   


**Github**: The single source of truth. Here, all project related file are stored (source code but also configuration files, dockerfiles, helm charts, build scripts, and so on)  
**Jenkins**: Jenkins is used as CI/CD Tool.  
**Docker Hub**: A registry where all Docker Images are stored.  
**Ansible**: A configuration management tool. Here, it is used to set up a Microk8s cluster on the target machine.  
**Kubernetes**: k8s is used as deployment target for the final docker image.  
