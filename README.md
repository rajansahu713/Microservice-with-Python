<h1 align="center"> Microservice with Python</h1>

We are going to build microservice using Python popular frameworks Django and Flask.

Prerequisites
* Django
* Flask
* Docker

> Note: Docker must be install in your system to run this application.

After cloning the repo. 

## Part-1

Go to Blogs directory and run the below commnand.

```docker
docker compose up --build
```
* When it finish you will see same message as you see when you run a django application.

* Now open another tab in the same directory and type the below command
    ```docker
    docker compose exec backend sh
    ``` 
* By using this command you will enter inside the backend terminal now you have to do all the migration as you do in a normal django applications.

## Part 2:
* Now come to main directory and you have to do same think as you did for the django appliacation.

But for flask migration please follow the below mention command.

```python
python manager db init # to initialize the database
python manager db migrate # to migrate new changes
python manager db upgrade
```





