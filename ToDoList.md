#TODO delete this once complete

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

:white_check_mark: ~~update endpoints with try: except: blocks~~

:white_check_mark: ~~try this to write more dynamic 404 messages:~~
https://flask.palletsprojects.com/en/2.1.x/errorhandling/ Returning API Errors as JSON

:white_check_mark: ~~test error handling~~

:question: implement Migrations and reset database

:black_square_button: separate error handling into its own file?

### Authorisation and 
:white_check_mark: setup Auth0 with three roles - 

:white_check_mark: get Auth header, decode and verfiy JWT, takes argument to describe action

:white_check_mark: add @requires decorator to endpoints

:white_check_mark: raise error if; token expried, claims invalid, token invalid, improper action

:white_check_mark: update setup.sh file

:black_square_button: test authorisation - almost finished

:black_square_button: update docstrings with auth details

:black_square_button: update readme with auth and role details

### Testing
:white_check_mark: add test folder/files

:white_check_mark: add tests for one success and one failure for each endpoint
- ~~GET actors~~
- ~~GET movies~~
- ~~GET actor movies~~
- ~~GET movie actors~~
- ~~POST actor~~
- ~~POST movie~~
- POST actor to movie
- ~~PATCH actor~~
- ~~PATCH movie~~
- ~~DELETE actor~~
- DELETE movie

:black_square_button: add tests demonstrating role-based access (two for each role)
https://knowledge.udacity.com/questions/321996
https://knowledge.udacity.com/questions/724461 - include tokens in setup.sh
https://knowledge.udacity.com/questions/199305

:black_square_button: update setup.sh file with tokens

:white_check_mark: update README with testing database setup and how to run tests

### Deployment
:black_square_button: host API on Render or AWS

:black_square_button: add URL and details to README

:black_square_button: update README with instructions to setup authentication so endpoints can be tested

### Code Quality and Documentation
:black_square_button: run pycodestyle against all .py files

:black_square_button: check all comments and docstrings

:black_square_button: all secrets~and tokens stored as environment variables

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

:black_square_button: pg_dump and save output to .psql file (pg_dump capstone > capstone3.psql)

:black_square_button: ensure Auth0 is running and jwt tokens will be valid before submission

# https://knowledge.udacity.com/questions/703470
:black_square_button: Add to readme - run login url and logrin as each user to get new tokens - save to setup.sh file
run source setup.sh

To be on the safe side I recommend providing a username and password for each role and the login URL.

:black_square_button: update setup.sh file with tokens

:black_square_button: test all endpoints, roles and tests


# consider
:black_square_button: setup migrations and instructions flask db upgrade to setup a blank database
:black_square_button: psql instructions for schema only, or scema + data?


#NOTE
downgraded itsdangerous to version 1.1.0 to remove the depretiation warning from unittest