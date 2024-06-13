# FSND_capstone

## Introduction and Motivation

Full Stack Nanodegree Capstone Project

## Table of Contents

- [1. Accessing the App](#1-accessing-the-app)
- [2. Running the App Locally](#2-running-the-app-locally)
    - [2.1 Installing Dependencies](#21-installing-dependencies)


## 1. Accessing the App

The deployed application can be accessed via this link: 
For endpoints that require authentication, see the `setup.sh` file for relevant Auth0 information.
###

## 2. Running the App Locally

### 2.1 Installing Dependencies

#### Python 3.7

*instructions to install*

#### Virtual Environment

*instructions to install*

#### PIP

## Launching the App
1. virtual env

2. Install dependancies
```bash
pip install -r requirements.txt
```

3. configure database
change DATABASE_URI variable in setup.sh file if needed to match you local Postgresql database username and password

```bash
DATABASE_URL="postgresql://{username}:{password}@localhost:5432/capstone"
```

4. Run the setup.sh file to set the env variables for Auth0, database uri and flask setting to run the app locally
```bash
source ./setup.sh

# Optional - Run these commands to check that env variables have been set
echo $DATABASE_URI
echo $FLASK_APP
echo $FLASK_DEBUG
echo $FLASK_ENVIRONMENT
```

5. To run the sever locally, run:
```bash
#TODO remove once set up
cd FSND_capstone
conda activate capstone_env

# activate virtual_env


flask run --reload

# use run_local.sh
```

## Create database

```bash
#TODO on wsl
# psql -U dev -h 127.0.0.1 -d postgres
# CREATE DATABASE capstone;
# /q


sudo -u postgres -i
createdb capstone

psql capstone
\q

exit

```
#TODO
2. **Create the database:**
Start Postgres and 
```bash
# psql -U postgres
# CREATE DATABASE fyyur;
# \q

sudo -u postgres -i
createdb capstone

psql capstone
\q

exit
```

3. **Add tables to database from migrations directory:**
```bash
flask db upgrade

sudo -u postgres psql -d capstone < capstone.psql
```

2. **Load the initial data into the database:**
```

psql -U postgres -d fyyur

# Add data into tables by copying contents of data.txt file.
# This loads data into the tables so that the id's match the mock data.

# Check the data - there should be 3 records in both venues (id 1-3) and artists (id 4-6) and 5 records in shows (id 1-5).

SELECT * FROM venues;
SELECT * FROM artists;
SELECT * FROM shows;
\q

```

**Running Tests**
```bash
sudo -u postgres -i
dropdb capstone_test
createdb capstone_test
sudo -u postgres psql -d capstone_test < capstone.psql
python test_app.py
```
## Actor Endpoints

### GET  /actors
#TODO
- General:
    - Fetches a list of question objects, success value, categories, total number of questions and current category.
    - Results are paginated in groups of 10. Includes an optional query parameter to choose page number, starting from 1.
    - Request Arguments: page (int).
    - Request Body: None.
    - Returns: A list  of question objects, paginated in groups of 10, success value, categories, total number of questions and current category. 
- Sample 1: `curl http://127.0.0.1:5000/actors`

```{
    "Actors": [
        {
            "age": 23,
            "gender": "Female",
            "id": 2,
            "name": "Jane Doe"
        }
    ],
    "success": true
}
```

If there are no actors in the database, the following json message will show:
```
{
    "error": "404 Not Found: There are no actors in the database",
    "success": false
}
```


### POST /actors/add 
 - General:
    - Creates a new actor using the submitted name, age and gender.
    - Request Arguments: None
    - Request Body: {"name": "Jane Doe", "age": 23, "gender": "Female"}
    - Returns: The id of the created actor, and the success value.

- Sample: `curl -d '{"name": "Jane Doe", "age": 23, "gender": "Female"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/actors/add`

curl -d '{"name": "John Doe", "age": 37, "gender": "Male"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/actors/add
```{
  "created": 3, 
  "success": true
}
```

### EDIT  /actors/${actor_id}/edit
#TODO
- General:
    - Creates a new movie using the submitted title and release date.
    - Request Arguments: None
    - Request Body: {"title": "test movie", "release_date": "test answer"}
    - Returns: The id of the created movie, and the success value.

#TODO - this isn't working
- Sample: `curl -d '{"name": "Jane Doe edit", "age": 23, "gender": "Female"}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/actors/2/edit`


```{ 
  "success": true,
  "edited movie": {}
}
```

### DELETE  /actors/${actor_id}/delete
- General:
    - Deletes the actor of the given actor_id if it exists. 
    - Request Arguments: actor_id (int).
    - Request Body: None.
    - Returns: The id of the deleted actor, and the success value. 

- Sample: `curl -X DELETE http://127.0.0.1:5000/actors/1/delete`

```{
  "deleted": 1, 
  "success": true
}
```
## Movie Endpoints

### GET  /movies
#TODO
- General:
    - Fetches a list of question objects, success value, categories, total number of questions and current category.
    - Results are paginated in groups of 10. Includes an optional query parameter to choose page number, starting from 1.
    - Request Arguments: page (int).
    - Request Body: None.
    - Returns: A list  of question objects, paginated in groups of 10, success value, categories, total number of questions and current category. 
- Sample 1: `curl http://127.0.0.1:5000/movies`

```{
    "Actors": [
        {
            "age": 23,
            "gender": "Female",
            "id": 2,
            "name": "Jane Doe"
        }
    ],
    "success": true
}
```

### POST /movies/add 
 - General:
    - Creates a new movie using the submitted title and release date.
    - Request Arguments: None
    - Request Body: {"title": "test movie", "release_date": "test answer"}
    - Returns: The id of the created movie, and the success value.

- Sample: `curl -d '{"title": "test movie", "release_date": "2010-07-10", "genre": "Action"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/movies/add`
```{
  "created": 3, 
  "success": true
}
```

If a correct genre is not entered
`curl -d '{"title": "second movie", "release_date": "2024-10-21", "genre": "x"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/movies/add`
```{
  "entered_genre": "x", 
  "error": "A genre from the following list must be entered:", 
  "genre list": [
    "Action", 
    "Adventure", 
    "Animation", 
    "Biography", 
    "Comedy", 
    "Crime", 
    "Documentary", 
    "Drama", 
    "Family", 
    "Fantasy", 
    "History", 
    "Horror", 
    "Musical", 
    "Romance", 
    "Scifi"
  ]
}
```

### EDIT  /movies/${movie_id}/edit
#TODO
- General:
    - Creates a new movie using the submitted title and release date.
    - Request Arguments: None
    - Request Body: {"title": "test movie", "release_date": "test answer"}
    - Returns: The id of the created movie, and the success value.

#TODO - this isn't working
- Sample: `curl -d '{"title": "test movie edit", "release_date": "2010-07-10"}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/movies/2/edit`


```{ 
  "success": true,
  "edited movie": {}
}
```


### DELETE  /movies/${movie_id}/delete
- General:
    - Deletes the movie of the given movie_id if it exists. 
    - Request Arguments: movie_id (int).
    - Request Body: None.
    - Returns: The id of the deleted movie, and the success value. 

- Sample: `curl -X DELETE http://127.0.0.1:5000/movies/1/delete`

```{
  "deleted": 1, 
  "success": true
}
```




#TODO
#references
rubric details
https://knowledge.udacity.com/questions/304257

https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#relationship-patterns

implement message in abort statement + integrity errors if any values must be unique?
abort(404, message = "No actor with that id exists")
https://rest-apis-flask.teclado.com/docs/sql_storage_sqlalchemy/insert_models_sqlalchemy/

many-to-many
https://rest-apis-flask.teclado.com/docs/sqlalchemy_many_to_many/many_to_many_relationships/

??
https://www.digitalocean.com/community/tutorials/how-to-use-many-to-many-database-relationships-with-flask-sqlalchemy

https://www.imdb.com/list/ls050274118/

source .setup.sh
https://knowledge.udacity.com/questions/159048#159135
os.envrion
https://knowledge.udacity.com/questions/217605#217639


other
https://www.nucamp.co/blog/coding-bootcamp-back-end-with-python-and-sql-deploying-flask-applications-best-practices

pg_dump
https://www.postgresqltutorial.com/postgresql-administration/postgresql-backup-database/


# TODO LIST

:white_check_mark: ~~move models to separate file~~

:white_check_mark: ~~add many-to-many relationship between Actor and Movie~~

:question: one-to-many relationship - Director and Movies?

:question: allow linking of more than one actor to a movie and visa versa
change endpoint (remove last int and add code to get request_body)

:black_square_button: test if a default date for Movie works

:question: remove nullable = False or have default 'None' in POST and PATCH endpionts?

:black_square_button: update README:
- curl -X POST http://127.0.0.1:5000/movie/3/actor/2

 curl -X POST http://127.0.0.1:5000/movie/3/actor/2
```{
  "error": "404 Not Found: No movie with id 3 exists", 
  "success": false
}
```
curl -X POST http://127.0.0.1:5000/movie/1/actor/2
```{
  "error": "404 Not Found: No actor with id 2 exists", 
  "success": false
}
```

curl -X POST http://127.0.0.1:5000/movie/1/actor/1
```{
  "Actor linked": 1, 
  "Movie linked": 1, 
  "success": true
}
```

- GET: curl http://127.0.0.1:5000/actor/1/movies
- GET: curl http://127.0.0.1:5000/movie/3/actors

:white_check_mark: ~~@app.errorhandler for at least four status codes~~

:black_square_button: update endpoints with try: except: blocks

:white_check_mark: ~~try this to write more dynamic 404 messages:~~
https://flask.palletsprojects.com/en/2.1.x/errorhandling/ Returning API Errors as JSON

:black_square_button: test error handling

:black_square_button: implement Migrations and reset database

### Authorisation and 
:black_square_button: setup Auth0 with three roles - 

:black_square_button: get Auth header, decode and verfiy JWT, takes argumnet to describe action

:black_square_button: add @requires decorator to endpoints

:black_square_button: raise error if; token expried, claims invalid, token invalid, improper action

:black_square_button: update setup.sh file

:black_square_button: test authorisation

:black_square_button: update docstrings with auth details

:black_square_button: update readme with auth and role details

### Testing
:black_square_button: add test folder/files

:black_square_button: add tests for one success and one failure for each endpoint
- GET actors
- GET movies
- GET actor movies
- GET movie actors
- POST actor
- POST movie
- POST actor to movie
- PATCH actor
- PATCH movie
- DELETE actor
- DELETE movie

:black_square_button: add tests demonstrating role-based access (two for each role)
https://knowledge.udacity.com/questions/321996
https://knowledge.udacity.com/questions/724461 - include tokens in setup.sh
https://knowledge.udacity.com/questions/199305

:black_square_button: update setup.sh file with tokens

:black_square_button: update README with testing database setup and how to run tests

### Deployment
:black_square_button: host API on Render or AWS

:black_square_button: add URL and details to README

:black_square_button: update README with instructions to setup authentication so endpoints can be tested

### Code Quality and Documentation
:black_square_button: run pycodestyle against all .py files

:black_square_button: check all comments and docstrings

:black_square_button: all secrets stored as environment variables

:black_square_button: README includes

    :black_square_button: Motivation for the project

    :black_square_button: Project dependencies

    :black_square_button: Local development

    :black_square_button: Hosting instructions

    :black_square_button: Detailed instructions for scripts to setup authentication

    :black_square_button: Detailed instructions to install project dependencies

    :black_square_button: Detailed instructions to run the development server

    :black_square_button: Documentation of API behaviour

    :black_square_button: Documentaion of RBAC controls

### Final Setup
:black_square_button: create db

:black_square_button: run migrations to add tables

:black_square_button: run app and use curl commands to add actors, movies and link some of them together

:black_square_button: pg_dump and save output to .psql file

:black_square_button: ensure Auth0 is running and jwt tokens will be valid before submission

:black_square_button: update setup.sh file with tokens

:black_square_button: test all endpoints, roles and tests
