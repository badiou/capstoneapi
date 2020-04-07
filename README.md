# Full Stack Capstone Casting API
## Content
1. Motivation
2. API Documentation
3. Authentification
4. Existing roles

## Motivation
The CAPSTONE CASTING API project is the latest Full stack developer course project on the www.udacity.com.
This project aims to revisit all the concepts seen in this course. It is :
- Modeling of the database for a web application using the SQLAlchemy ORM (in the files models.py)
- CRUDs to interact with the database: (app.py)
- Automated unit tests (in the file test_app.py)
- Authentication and authorization using Auth0 (auth.py)
- Deployment on heroku (Procfile, setup.sh)

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies:

```bash
pip install -r requirements.txt
```
Heroku looks for a requirements.txt file that needs to include all of your dependencies.

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server locally
To execute your API locally, you need to modify in the models.py file, the value ENV = 'prod' to ENV = 'dev'.
You must then launch the migrations to create your database. These migrations are managed using the following commands:
- python manage.py db init
- python manage.py db migrate
- python manage.py db upgrade.

After performing these migrations, you will then execute the commands to launch your API. To test all endpoints of your API, please use the `CapstoneAPI_localhost.postman_collection.json` file by importing it from Postman. If you don't have postman, you can download it from https://www.postman.com.
To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## API DOCUMENTATION

Getting starter
## API REFERENCE 
This API has been deployed on heroku and is available from the link https://capstoneapi.herokuapp.com

## Error Handling
Errors are retourned as JSON objects in the following format:
{
    "success":False
    "error": 400
    "message":"Bad request
}

The API will return four error types when requests fail:
. 400: Bad request
. 500: Internal server error
. 422: Unprocessable
. 404: Not found
. 401: Unauthorized


## Endpoints

### GET/movies
    GENERAL: 
        This endpoints returns a list of movies object, success value, total number of the movies. 

            Sample: curl https://capstoneapi.herokuapp.com/movies

            {
                "movies": [
                    {
                        "id": 1,
                        "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                        "title": "Thomas NGIJOL"
                    },
                    {
                        "id": 3,
                        "release_date": "Wed, 02 Dec 2020 00:00:00 GMT",
                        "title": "Casanova"
                    }
                ],
                "success": true,
                "total_movies": 2
            }

###  GET/movies(movie_id)
    GENERAL: This endpoint allows you to get for a particular Movie using its id. This endpoint
     returns one movie, and the status_code
            Sample: curl https://capstoneapi.herokuapp.com/movies/1

            {
                "movie": [
                    {
                        "id": 1,
                        "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                        "title": "Thomas NGIJOL"
                    }
                ],
                "success": true
            }

###  GET/actors
    GENERAL: 
        This endpoints returns a list of actors object, success value, total number of the actors. 

            Sample: curl https://capstoneapi.herokuapp.com/actors

            {
                "actors": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    },
                    {
                        "age": 45,
                        "gender": "M",
                        "id": 5,
                        "name": "Jamel Debouzze"
                    }
                ],
                "success": true
            }

###  GET/actors(actor_id)
    GENERAL: This endpoint allows you to get for a particular actor using its id. This endpoint 
    returns one actor, and the status_code
            Sample: curl https://capstoneapi.herokuapp.com/actors/1

            {
                "actor": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    }
                ],
                "success": true
            }


###  DELETE/actors(actor_id)
    GENERAL: Delete the actor  of the given ID if it exists. Return the id of the deleted actor, 
    success value, total of actors and actor list based on current page number. Results are paginated in groups of 10.

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/actors/5
            {
                "actors": [
                    {
                        "age": 32,
                        "gender": "M",
                        "id": 1,
                        "name": "Badiou OURO"
                    }
                ],
                "deleted": 5,
                "success": true,
                "total_actors": 1
            }


        ###  DELETE/movies(movie_id)
            GENERAL: Delete the movie  of the given ID if it exists. Return the id of the deleted movie, 
            success value, total of movies and movies list based on current page number. Results are
             paginated in groups of 10.

            Sample: curl - X DELETE https://capstoneapi.herokuapp.com/movies/5

            {
        "actors": [
            {
                "id": 1,
                "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                "title": "Thomas NGIJOL"
            }
        ],
        "deleted": 3,
        "success": true,
        "total_movies": 1
    }


###  POST/movies
    GENERAL: This endpoint is used to create a new movie. We return the ID of the new movie created, 
    the movie that was created, the list of movies and the number of movies.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/movies 
            -H "Content-Type:application/json" -d "{"title":"Casanova","release_date":"2020-12-02"}"

                {    
            "movies": [
                {
                    "id": 1,
                    "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                    "title": "Thomas NGIJOL"
                },
                {
                    "id": 4,
                    "release_date": "Wed, 02 Dec 2020 00:00:00 GMT",
                    "title": "Casanova"
                }
            ],
            "created": 4,
            "success": true,
            "total_movies": 2
            }



###  POST/actors
    GENERAL: This endpoint is used to create a new actor. We return the ID of the new actor 
    created, the movie that was created, the list of actors and the number of actors.

            Sample: curl -X POST https://capstoneapi.herokuapp.com/actors 
            -H "Content-Type:application/json" -d "{"name":"Jamel Debouzze","age":45,"gender":"M"}"

                {
                    "actors": [
                        {
                            "age": 32,
                            "gender": "M",
                            "id": 1,
                            "name": "Badiou OURO"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 6,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 7,
                            "name": "Jamel Debouzze"
                        },
                        {
                            "age": 45,
                            "gender": "M",
                            "id": 8,
                            "name": "Jamel Debouzze"
                        }
                    ],
                    "created": 8,
                    "success": true,
                    "total_actors": 4
                }


###  PATCH/actors(actor_id)
    GENERAL: This endpoint allows you to modify an actor. It returns the modified actor,
     the actor ID that was modified and status_code

            Sample: curl -X PATCH https://capstoneapi.herokuapp.com/actors/1 
            -H "Content-Type:application/json" -d "{"name":"Badiou OURO","gender":"M","age":32}"

                {
                    "actor": [
                        {
                            "age": 32,
                            "gender": "M",
                            "id": 1,
                            "name": "Badiou OURO"
                        }
                    ],
                    "id": 1,
                    "success": true
                    }


###  PATCH/movie(movie_id)
    GENERAL: This endpoint allows you to modify an movie. It returns the modified movie, 
    the movie ID that was modified and status_code

            Sample: curl -X PATCH https://capstoneapi.herokuapp.com/movie/1 
            -H "Content-Type:application/json" -d "{"title":"Thomas NGIJOL","release_date":"2001-03-09"}"

                {
                    "id": 1,
                    "movie": [
                        {
                            "id": 1,
                            "release_date": "Fri, 09 Mar 2001 00:00:00 GMT",
                            "title": "Thomas NGIJOL"
                        }
                    ],
                    "success": true
                    }

## Authentification

All API Endoints are decorated with Auth0 permission. You need to config Auth0

1. Login to https://auth0.com/
2. Click on Application Tab
3. Create Application
4. Give the name like `Capstone` and select "regular Web Application
5. Go to settings and find domain. Copy AUTH0_DOMAIN  and remplace it in your Auth0 file. 
For example if you domain is `fsndtogo.eu.auth0.com` you may have on your `auth.py` file
`AUTH0_DOMAIN=fsndtogo.eu.auth0.com`
6. Click on API Tab
7. Create a new API: Set the name of your API. For example you can use the name `capstone`
    1. Name : capstone
    2. Identifier capstone
    3. Do not change the value of the algorithm. Leave it on RS256
8. Get API_AUDIENCE et remplace it in your auth.py file `API_AUDIENCE = 'capstone'`

### Your can see the example of token i set on the config.py file.

### Existing roles

 This API works with 3 roles that have been created on Auth0

1. CASTING ASSISTANT:

    - GET/movie : can get all movies
    - GET/actors : can get all actors
    - GET/actors(actor_id): Get a specific actor by ID
    - GET/actors(movie_id): Get a specific movie by ID

2. CASTING DIRECTOR (EVERYTHING FROM CASTING ASSISTANT AND.......)
    - POST/actors: can create an new actor
    - PATCH/movies: can edit movie
    - PATCH/actors: can edit actor
    - DELETE/actors: Delete a specific actor by ID

3. EXECUTIVE DIRECTOR (EVERYTHING FROM CASTING DIRECTOR AND.......)
    - POST/movies: can create a new movie
    - DELETE/movies: can delete a specific movie by ID


To test the API endpoints, you need to pass a bearer token authorization parameter. 

4. The `capstoneAPI_online.postman_collection.json` file can be used to test the API. If you have a 401 error, 
you need to get another token from your Auth0 domain to test the endpoints.

To show the example of bearer token you can show it in your `config.py` file

##  Testing using capstonedb_test
To run the tests, run
```
dropdb capstonedb_test
createdb capstonedb_test
python test_app.py
```