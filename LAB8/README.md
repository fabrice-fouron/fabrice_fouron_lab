# Lab 8
## Setup
Things to install: python

- For python, create an environment from which you will run the code. Install the following packages: ```uvicorn```, ```fastapi```

#### On Docker, you will need to download the following images:
- ```minio/minio```
- ```redis```
- ```boky/postfix```

The ```docker-compose.yaml``` file specifies the services that will be given 

## How to run
First, you need to open the terminal in the **LAB8/** folder.

To run the server, you enter the followin command in the console:
```
uvicorn main:app --port 8080
```

#### There are different routes that are available:
- ```/save-files``` It gives the ability to save files on the MinIO object storage service. It uses the GET verb -> (http://localhost:8080/save-files)
- ```/new-email``` It uses the email service postfix to send an email to a user. It uses the GET verb -> (http://localhost:8080/save-files)
- ```/set-user-info``` It uses the Redis service to save information. It uses the POST verb -> (http://localhost:8080/set-user-info)
- ```/get-user-info``` It uses the Redis service to get information on a user given a specific ID. It uses the POST verb -> (http://localhost:8080/get-user-info). The query string parameter needed is the id. Add ```?student_id={id}``` to get the information needed
