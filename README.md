# Full Stack Capstone Casting API

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

Within directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` to find the application. 

## API REFERENCE

Getting starter
## API REFERENCE 
Currently, this app can be run locally is also deployed online on the heroku cloud platform. You can run the application online using the link https://capstoneapi.herokuapp.com

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
    GENERAL: This endpoint allows you to get for a particular Movie using its id. This endpoint returns one movie, and the status_code
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
    GENERAL: This endpoint allows you to get for a particular actor using its id. This endpoint returns one actor, and the status_code
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
    GENERAL: Delete the actor  of the given ID if it exists. Return the id of the deleted actor, success value, total of actors and actor list based on current page number. Results are paginated in groups of 10.

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
    GENERAL: Delete the movie  of the given ID if it exists. Return the id of the deleted movie, success value, total of movies and movies list based on current page number. Results are paginated in groups of 10.

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
    GENERAL: This endpoint is used to create a new movie. We return the ID of the new movie created, the movie that was created, the list of movies and the number of movies.

    Sample: curl -X POST https://capstoneapi.herokuapp.com/movies -H "Content-Type:application/json" -d "{"title":"Casanova","release_date":"2020-12-02"}"

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
    GENERAL: This endpoint is used to create a new actor. We return the ID of the new actor created, the movie that was created, the list of actors and the number of actors.

    Sample: curl -X POST https://capstoneapi.herokuapp.com/actors -H "Content-Type:application/json" -d "{"name":"Jamel Debouzze","age":45,"gender":"M"}"

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
    GENERAL: This endpoint allows you to modify an actor. It returns the modified actor, the actor ID that was modified and status_code

    Sample: curl -X PATCH https://capstoneapi.herokuapp.com/actors/1 -H "Content-Type:application/json" -d "{"name":"Badiou OURO","gender":"M","age":32}"

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
    GENERAL: This endpoint allows you to modify an movie. It returns the modified movie, the movie ID that was modified and status_code

    Sample: curl -X PATCH https://capstoneapi.herokuapp.com/movie/1 -H "Content-Type:application/json" -d "{"title":"Thomas NGIJOL","release_date":"2001-03-09"}"

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
5. Go to settings and find domain. Copy AUTH0_DOMAIN  and remplace it in your Auth0 file. For example if you domain is `fsndtogo.eu.auth0.com` you may have on your `auth.py` file
`AUTH0_DOMAIN=fsndtogo.eu.auth0.com`
6. Click on API Tab
7. Create a new API: Set the name of your API. For example you can use the name `capstone`
    1. Name : capstone
    2. Identifier capstone
    3. Do not change the value of the algorithm. Leave it on RS256
8. Get API_AUDIENCE et remplace it in your auth.py file `API_AUDIENCE = 'capstone'`

### Your can use my own token i set on the config.py file.

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

4. The `capstoneAPI_online.postman_collection.json` file can be used to test the API. If you have a 401 error, you need to get another token from your Auth0 domain to test the endpoints.

To show the example of bearer token you can show it in your `config.py file`

##  Testing
To run the tests, run
```
dropdb capstonedb_test
createdb capstonedb_test
psql capstonedb_test < capstonedb.sql
python test_app.py
```