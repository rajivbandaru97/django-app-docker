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

For better understanding, clone this project and study the DockerFile to gt in more details of the same.
