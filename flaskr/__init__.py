import datetime
from dateutil import parser
import os
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
import json
from enums import GenreEnum
from werkzeug.exceptions import HTTPException
from .auth.auth import AuthError, requires_auth

# https://flask.palletsprojects.com/en/2.3.x/tutorial/factory/
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    with app.app_context():
        setup_db(app)

    #TODO - not using migrations - so remove
    #setup_migration(app)
    #TODO
    CORS(app)

    # #TODO: swap to using config file and Migrate? Fyyur - or use settings like in Trivia App?
    # # moment = Moment(app)

    # # # https://knowledge.udacity.com/questions/720875
    # # db.init_app(app)

    #TODO
    # The after_request function has been added in to manage a CORS 'Access-Control-Allow-Origin' error that would prevent the frontend from working correctly depite the fact the CORS has been configured in Auth0.
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, PATCH, POST, POST, DELETE, OPTIONS"
        )
        return response
        
    #TODO: leave this as / or /login-results?
    @app.route("/")
    def index():
        return jsonify({'message': "Welcome to the Casting Agency App!"})
        
    # ----------------------------------------------------------------------------#
    # Actor Endpoints
    # ----------------------------------------------------------------------------#

    @app.route("/actors")
    @requires_auth("view:actors")
    def get_actors(payload):
        """ The get_actors function uses the GET method to
        list all the avaliable actors in the agency.

        The endpoint returns a list of actors if the user has the required 
        view permissions.

        Raises:
        HTTPException: 404, "resource not found", if there are no
        actors in the database.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            allActors = Actor.query.all()

            if len(allActors) == 0:
                abort(404, description="There are no actors in the database")

            actors = list(map(lambda actor: actor.format(), allActors))

            return jsonify(
                {
                    "success": True,
                    "actors":actors,
                }
                )
        
        except Exception as e:
            customExceptionHandler(e)

    @app.route("/actor/<int:actor_id>/movies")
    @requires_auth("view:actors")
    def get_actor_movies(payload, actor_id):
        """ The get_actor_movies function uses the GET method to
        list the movies an actor is cast in based on the actor_id.

        The endpoint returns a list of movies an actor is cast in
        if the user has the required view permissions.

        Raises:
        #TODO - will this work if actor has no movies? or just send message
        "actor has not been cast in any movies yet"
        HTTPException: 404, "resource not found", if there are no
        questions in the category.
        VS
        HTTPException: 404, "resource not found", if the actor_id is not
        in the database.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id
                ).one_or_none()
            if actor is None:
                abort(404, description="No actor with id "+ str(actor_id) +" exists")
            
            movies = [movie.format() for movie in actor.movies]
            
            if len(movies) == 0:
                return jsonify({
                    "success": True,
                    "actor":actor.name,
                    "movies cast in": "The actor "+ actor.name + " has not been cast in any movies yet"
                    })

            return jsonify(
                {
                    "success": True,
                    "actor":actor.name,
                    "movies cast in": movies
                }
                )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/actors/add", methods=["POST"])
    @requires_auth("post:actors")
    def add_actor(payload):
        """ The add_actor endpoint uses the POST method to
        add a new actor to the database.

        The endpoint takes the submitted name, age and gender
        and adds the new actor object to the database.

        Raises:
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        body = request.get_json()
        new_name = body.get("name")
        new_age = body.get("age")
        new_gender = body.get("gender")

        try: 
            actor = Actor(
                name=new_name,
                age=new_age,
                gender=new_gender,
            )

            actor.insert()

            return jsonify(
                {
                    "success": True,
                    "created": actor.format(),
                }
            )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/actors/<int:actor_id>/edit", methods=["PATCH"])
    @requires_auth("update:actors")
    def edit_actor(payload, actor_id):
        """ The edit_actor function uses the PATCH method to
        edit a chosen actor from the database.

        The endpoint takes the actor id and, if the actor exists,
        edits it and commits it back to the database.

        Raises:
        HTTPException: 404, "resource not found", if the actor does
        not exist.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        body = request.get_json()
        try:
            actor = Actor.query.filter(
                Actor.id == actor_id
                ).one_or_none()

            if actor is None:
                abort(404, description="No actor with id "+ str(actor_id) +" exists")
            
            #TODO - what if one of the column names is missing?
            if "name" in body:
                actor.name = body.get("name")
            if "age" in body:
                actor.age = body.get("age")
            if "gender" in body:
                actor.gender = body.get("gender")
            actor.update()

            return jsonify(
                {
                    "success": True,
                    "actor": actor.format(),
                }
            )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/actors/<int:actor_id>/delete", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actor(payload, actor_id):
        """ The delete_actor function uses the DELETE method to
        delete a chosen actor from the database.

        The endpoint takes the actor id and, if the actor exists,
        deletes it from the database.

        Raises:
        HTTPException: 404, "resource not found", if the actor does
        not exist.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try: 
            actor = Actor.query.filter(
                    Actor.id == actor_id
                    ).one_or_none()
            if actor is None:
                abort(404, description="No actor with id "+ str(actor_id) +" exists")
            
            actor.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": actor_id,
                }
            )

        except Exception as e:
            customExceptionHandler(e)

    # ----------------------------------------------------------------------------#
    # Movie Endpoints
    # ----------------------------------------------------------------------------#

    @app.route("/movies")
    @requires_auth("view:movies")
    def get_movies(payload):
        """ The get_movies function uses the GET method to
        list all the avaliable movies in the agency.

        The endpoint returns an list of movies if the user has the required 
        view permissions.

        Raises:
        HTTPException: 404, "resource not found", if there are no
        movies in the database.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            allMovies = Movie.query.all()

            if len(allMovies) == 0:
               abort(404, description ="There are no movies in the database")


            movies = list(map(lambda movie: movie.format(), allMovies))

            return jsonify(
                {
                    "success": True,
                    "movies":movies,
                }
                )
        #TODO fix this
        except Exception as e:
            customExceptionHandler(e)

    @app.route("/movie/<int:movie_id>/actors")
    @requires_auth("view:movies")
    def get_movie_actors(payload, movie_id):
        """ The get_movie_actors function uses the GET method to
        list the actors cast in a movie based on the movie_id.

        The endpoint returns a list of actors cast in a movie
        if the user has the required view permissions.

        Raises:
        #TODO - will this work if movie has no actors? or just send message
        "movie does not have any cast members yet"
        HTTPException: 404, "resource not found", if there are no
        actors cast in the movie.
        VS
        HTTPException: 404, "resource not found", if the movie_id is not
        in the database.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id
                ).one_or_none()
            if movie is None:
                abort(404, description="No movie with id "+ str(movie_id) +" exists")
            
            actors = [actor.format() for actor in movie.actors]
            
            if len(actors) == 0:
                return jsonify({
                    "success": True,
                    "movie":movie.title,
                    "actors cast": "The movie "+ movie.title + " does not have any cast members yet"
                    })

            return jsonify(
                {
                    "success": True,
                    "movie":movie.title,
                    "actors cast": actors
                }
                )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/movies/add", methods=["POST"])
    @requires_auth("post:movies")
    def add_movie(payload):
        """ The add_movie endpoint uses the POST method to
        add a new movie to the database.

        The endpoint takes the submitted movie title and
        release date and adds the new movie object to the
        database.

        Raises:
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        body = request.get_json()
        #TODO: where to start try statement?

        new_title = body.get("title")
        new_release_date = body.get("release_date")

        # if "title" in body:
        #     new_title = body.get("title")
        # else:
        #     abort(422, description="A movie title must be provided")
        # # Provide a more descriptive error message if the release_date value is not included or isn't a date
        # # dateutil.parser is used to covert the string date into a datetime object for the purposes of 
        # # checking
        # # Ref: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
        # # Ref: https://dateutil.readthedocs.io/en/stable/index.html
        # if "release_date" in body and isinstance(parser.parse(body.get("release_date")), datetime.datetime) :
        #     new_release_date = body.get("release_date")
        # else:
        #     abort(422, description="A release date must be provided")

        genre_list = [genre.value for genre in GenreEnum]
        if "genre" in body:
            if body.get("genre") in genre_list:
                new_genre = body.get("genre")
            else:
                return jsonify(
                    {
                        "entered_genre": body.get("genre"),
                        "error": "A genre from the following list must be entered:",
                        "genre list": genre_list
                    }
                )
        else:
            abort(422, description="A genre must be provided")
        
        try: 
            movie = Movie(
                title=new_title,
                release_date=new_release_date,
                genre=new_genre
            )

            movie.insert()

            return jsonify(
                {
                    "success": True,
                    "created": movie.format(),
                }
            )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/movies/<int:movie_id>/edit", methods=["PATCH"])
    @requires_auth("update:movies")
    def edit_movie(payload, movie_id):
        """ The edit_movie function uses the PATCH method to
        edit a chosen movie from the database.

        The endpoint takes the movie id and, if the movie exists,
        edits it and commits it back to the database.

        Raises:
        HTTPException: 404, "resource not found", if the movie does
        not exist.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        body = request.get_json()
        try:
            movie = Movie.query.filter(
                Movie.id == movie_id
                ).one_or_none()

            if movie is None:
                abort(404, description="No movie with id "+ str(movie_id) +" exists")

            #TODO what if column names aren't listed in the body? doesn't seem to be an issue
            if "title" in body:
                movie.title = body.get("title")
            if "release_date" in body:
                movie.release_date = body.get("release_date")

            genre_list = [genre.value for genre in GenreEnum]
            if "genre" in body:
                if body.get("genre") in genre_list:
                    movie.genre = body.get("genre")
                else:
                    return jsonify(
                        {
                                "entered_genre": body.get("genre"),
                                "error": "A genre from the following list must be entered:",
                                "genre list": genre_list
                        }
                    )
                
            movie.update()

            return jsonify(
                {
                    "success": True,
                    "movie": movie.format(),
                }
            )
       
        except Exception as e:
            customExceptionHandler(e)

    @app.route("/movies/<int:movie_id>/delete", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movie(payload, movie_id):
        """ The delete_actor function uses the DELETE method to
        delete a chosen actor from the database.

        The endpoint takes the actor id and, if the actor exists,
        deletes it from the database.

        Raises:
        HTTPException: 404, "resource not found", if the actor does
        not exist.
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            movie = Movie.query.filter(
                    Movie.id == movie_id
                    ).one_or_none()
            
            if movie is None:
                abort(404, description="No movie with id "+ str(movie_id) +" exists")
            
            movie.delete()

            return jsonify(
                {
                    "success": True,
                    "deleted": movie_id,
                }
            )

        except Exception as e:
            customExceptionHandler(e)

    @app.route("/movie/<int:movie_id>/actor/<int:actor_id>", methods=["POST"])
    @requires_auth("post:cast_actors")
    def link_movie_to_actor(payload, movie_id, actor_id):
        """ The add_movie endpoint uses the POST method to
        add a new movie to the database.

        The endpoint takes the submitted movie title and
        release date and adds the new movie object to the
        database.

        Raises:
        HTTPException: 422, "unprocessable", if the request cannot be
        completed.
        """
        try:
            #TODO what about get_or_404? will this remove lines of code?
            movie = Movie.query.filter(
                    Movie.id == movie_id
                    ).one_or_none()
            
            if movie is None:
                abort(404, description="No movie with id "+ str(movie_id) +" exists")

            actor = Actor.query.filter(
                    Actor.id == actor_id
                    ).one_or_none()
            
            if actor is None:
                abort(404, description="No actor with id "+ str(actor_id) +" exists")
                #TODO https://flask.palletsprojects.com/en/2.1.x/errorhandling/
                # Returning API Errors as JSON
                # abort(404, description="The actor with id " + actor_id + " does not exist.")

            movie.actors.append(actor)
            movie.insert()

            return jsonify(
                {
                    "success": True,
                    "movie": movie.title,
                    "actor cast": actor.name
                }
            )
        #TODO: https://flask.palletsprojects.com/en/2.1.x/errorhandling/
        # Generic Exception Handlers section

        except Exception as e:
            customExceptionHandler(e)

    # ----------------------------------------------------------------------------#
    # Error Handling.
    # ----------------------------------------------------------------------------#

    # The below exception handler function allows any abort() inside
    # the try blocks to work wihle also minimising duplicate code.
    # https://stackoverflow.com/questions/17746897/flask-abort-inside-try-block-behaviour
    def customExceptionHandler(e):
        if isinstance(e, HTTPException):
            # If the error has a unique message passed as a description parameter,
            # it will be passed through to the error handler
            # If no description parameter is defined, if will pass the default
            # error message
            abort(e.code, e.description)
        else:
            abort(422)

    @app.errorhandler(400)
    def bad_request(error):
        """The bad_request error handler returns the error code and 
        a json message, when a method is aborted with a 400
        error.
        """

        return (
            jsonify({
                "success": False,
                "error": f"{error.code}: {error.name}",
                "message": error.description
            }),
            400,
        )

    #TODO: update to allow message to be passed in abort(404) code
    @app.errorhandler(404)
    def not_found(error):
        """The not_found error handler returns the error code and 
        a json message, when a method is aborted with a
        404 error.
        """

        return (
            jsonify({
                "success": False,
                "error": f"{error.code}: {error.name}",
                "message": error.description
            }),
            404,
        )

    @app.errorhandler(405)
    def method_not_allowed(error):
        """The method_not_allowed error handler returns a json
        message, "method not allowed", when a method is aborted with
        a 405 error.
        """
        return (
            jsonify({
                "success": False,
                "error": f"{error.code}: {error.name}",
                "message": error.description
            }),
            405,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        """The unprocessable error handler returns a json
        message, "unprocessable", when a method is aborted with a 422
        error.
        """
        return (
            jsonify({
                "success": False,
                "error": f"{error.code}: {error.name}",
                "message": error.description
            }),
            422,
        )

    @app.errorhandler(500)
    def internal_server_error(error):
        """The internal_server_error error handler returns a json
        message, "internal server error", when a method is aborted with
        a 500 error.
        """
        return (
            jsonify({
                "success": False,
                "error": f"{error.code}: {error.name}",
                "message": error.description
            }),
            500,
        )

    @app.errorhandler(AuthError)
    def auth_error(error):
        """The auth_error error handler returns an appropriate json message when an authorization error is raised.

        Args:
        error (Any): The error code passed by the raised AuthError.

        Returns:
        response: The status code and JSON string defined by the raised AuthError..
        """
        response = jsonify(error.error)
        response.status_code = error.status_code
        return response

    return app

#TODO use this instead of return app for render deployment?
app = create_app()

if __name__ == '__main__':
    app.run()
