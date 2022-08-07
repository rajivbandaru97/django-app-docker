The main goal here was to create a container for a django application on docker.

For this we had a django project that was already created, we created a Dockerfile for the django project in order to get the environment needed to run the django application.

We used the python3.9:buster to create python based environment on docker, and later on specified more and more details, such as instaling requirements for the django app required using requirements.txt

We also provided the command to run the django project in the dockerfile itself, so that when the docker is run, the container is created and so does the app starts running all by itself.

Now after we had the Dockerfile created, in powershell, we used the following command:

docker-build . -t blockchain-3

In the above command, we are using the docker-build functionality to get the environment created. The "." specifies the directory the project is in. It is highly recommended to use the docker-build from the root folder itself.
-t here defines the tag blockchain-3 which we have given here, you can give any other name of your choice.

Once the command is run, it completes different stages of initialising everything sequentially as per Dockerfile. After the build is completed, we go for the run of the docker container for our django web app.

Now, we use the following command to run the container:

docker run -d -p 8000:8000 blockchain-3

In this command, we are running the docker container that was previously created. "-d" has been used to run the service in the background. 8000:8000 here is the port initialaisation as in which port will our container run.

Once the command is executed, go to your browser and type localhost:8000.

VOILA!!

You will see your django web app running on the container.

**UPDATE**
I have now added a new deployment.yaml file as well to the same. This contains the configuration needed to get the same running on the kubernetes as well locally.

Requirements:
1. Kubectl
2. Minikube(to get dashboard view of the same)

In the deployment.yaml, I have mentioned entirely the configuration for the kubernetes pod creation to run the same. If you will look closely, you will see the number of replicas created to be 5. This has been done so that there is always availability for the web app even if one pod goes down, others will back it up.

Now, we have mentioned the service name in the same, and also the target port, wherein we have provided with the port number of our docker container that we have initialised on. The image name too we have taken as the name of the container created on docker.

**RUNNING ON KUBERNETES**
To run the same on the kubernetes, we put in the following command:

kubectl apply -f deployment.yaml

This command will initialise the entire pod to be created on kubernetes as per the configuration mentioned in deployment.yaml and our kubernetes pod for the same will be created.

To check our app on the kubernetes dashboard, we use the following command:

minikube dashboard

Once you enter this command, in your browser, you will seee the dashboard on the same and also see the stats regarding it, as of how many resources are being used and so on.

Now, to check details regarding your kubernetes service, you run the following command:

minikube service django-test-service

Here, the name of my service is django-test-service, hence I have mentioned the same as in here. You can put in the name of your service as you have mentioned in the deployment.yaml file

This will then yield the service usage parameters as well for the deployment of the pod that you had created.

For better understanding, clone this project and study the DockerFile and also the deployment.yaml file to get in more details of the same.

#HappyLearning
