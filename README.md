# FSND_capstone

<details>
<summary>

## Introduction and Motivation
</summary>

Full Stack Nanodegree Capstone Project
</details>

## Table of Contents

- [1. Accessing the App](#1-accessing-the-app)
- [2. Running the App Locally](#2-running-the-app-locally)
    - [2.1 Installing Dependencies](#21-installing-dependencies)


## 1. Accessing the App

The deployed application can be accessed via this link: 
For endpoints that require authentication, see the `setup.sh` file for relevant Auth0 information.
###

## AUTH0 login URL:

#TODO use :5000 url? if yes, update Auth0

https://dev-dudattxg70vfdgkq.au.auth0.com/authorize?audience=castingAgencyAPI&response_type=token&client_id=t4oSkhZhgtTiA9Tcy1eR6eEYiF88QtXg&redirect_uri=http://127.0.0.1:8080/login-results

https://dev-dudattxg70vfdgkq.au.auth0.com/authorize?audience=castingAgencyAPI&response_type=token&client_id=t4oSkhZhgtTiA9Tcy1eR6eEYiF88QtXg&redirect_uri=http://127.0.0.1:5000/login-results

If the tokens supplied have expired, login as as the the users to get new tokens
after loging in, copy the text between **login-result#access_token=** and **&expires_in=** in the resulting url:

> 127.0.0.1:8080/login-results#access_token=***eyJhbGciO....pGPtjyO6EQ***&expires_in=7200&token_type=Bearer

and replace the tokens in the setup.sh file.

run the setup script to apply the new tokens:
```bash
source ./setup.sh
```

# Casting Assistant

casting_assistant@gmail.com
passwordAssistant3456#

# Casting Director

casting_director@gmail.com
passwordDirector8756@

# Executive Producer

executive_producer@gmail.com
passwordProducer4704$





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

# Key dependancies
#TODO - rmove?
https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
PostgreSQL
Flask
SQLAlchemy
Flask-CORS

3. configure database
change DATABASE_URI variable in setup.sh file if needed to match you local Postgresql database username and password

```bash
DATABASE_URL="postgresql://{username}:{password}@localhost:5432/capstone"
```

4. Run the setup.sh file to set the env variables for Auth0, database uri and flask setting to run the app locally
```bash
source ./setup.sh

# Optional - Run these commands to check that env variables have been set
echo $DATABASE_URL
echo $FLASK_APP
echo $FLASK_DEBUG
echo $FLASK_ENVIRONMENT
```

5. To run the sever locally, run:
```bash
#TODO remove once set up
cd FSND_capstone
source .venv/bin/activate

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
dropdb capstone && createdb capstone

psql capstone
\q

exit
```
#TODO: don't do this - loading the intial data from capstone.psql fails
#TODO: can use this if command sudo -u postgres psql -d capstone < capstone-data.psql
#is used (psql file created from pg_dump --data-only capstone > capstone-data.psql)
#Using flask db upgrade and .psql is a problem if the schema and the database contents diverge,
#so the idea was discarded.
~~3. **Add tables to database from migrations directory:**~~
```bash
#flask db upgrade
# sudo -u postgres -i
# psql capstone
# #check that the three tables have been created
# \dt
# #check columns and relationships of tables
# \d actors
# \d movies
# \d actors_movies
# \q
# exit

```

2. **Load the initial data into the database:**
```bash
sudo -u postgres psql -d capstone < capstone.psql


sudo -u postgres -i

psql capstone
#check that the three tables have been created
\dt

#check columns and relationships of tables
\d actors
\d movies
\d actors_movies

#check that initial data has loaded
SELECT * FROM actors;
SELECT * FROM movies;
SELECT * FROM actors_movies;

\q

exit

```

**Running Tests**
```bash
sudo -u postgres -i
dropdb capstone_test
createdb capstone_test
exit
sudo -u postgres psql -d capstone_test < capstone.psql
python test_flaskr.py

# to run individual tests
python test_flaskr.py CapstoneTestCase.test_name
# example
python test_flaskr.py CapstoneTestCase.test_delete_movie_403
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
