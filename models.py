import os
# from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from datetime import datetime
import json
from enums import GenreEnum

# from sqlalchemy import Column, String, Integer, Boolean, create_engine
# from sqlalchemy.sql.schema import PrimaryKeyConstraint

# Get the database path from the environment variable in setup.sh
# Reference: https://knowledge.udacity.com/questions/217605#217639
# Reference: https://www.geeksforgeeks.org/python-os-environ-object/

database_path = os.environ['DATABASE_URI']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

#TODO - remove this
# def setup_migration(app):
#     migrate = Migrate(app,db)

#     with app.app_context():
#         db.create_all()

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database - used in the test_capstone.py file
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
# Ref: coffee_shop project
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()

# ----------------------------------------------------------------------------#
# Association Table - many-to-many relationship
# ----------------------------------------------------------------------------#
#TODO
# Using association table as only the actor id and movie id columns are used
# Ref: https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#relationship-patterns
actors_movies = db.Table('actors_movies',
                                     db.Column(
                                         "actor_id",
                                          db.Integer,
                                          db.ForeignKey("actors.id"),
                                          primary_key=True),
                                     db.Column(
                                         "movie_id",
                                         db.Integer,
                                         db.ForeignKey("movies.id"),
                                         primary_key=True)
                                     )

# ----------------------------------------------------------------------------#
# Actor Model
# ----------------------------------------------------------------------------#
class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    movies = db.relationship(
            'Movie',
            secondary="actors_movies",
            back_populates="actors"
    #     lazy=True,
    #     # Ref: https://knowledge.udacity.com/questions/637391#637486
    #TODO is delete needed to remove movie from actor if deleted and visa versa?
    #     cascade="all, delete"
    )

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            actor = Actor(name=req_name, age=27, gender=Male)
            actor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.name = 'Tom Cruise'
            actor.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from database
        the model must exist in the database
        EXAMPLE
            actor = Actor(name=req_name, age=27, gender=Male)
            actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        # Ref: https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/?ref=lbp
        if len(self.movies) == 0:
            movies = "This actor has not been cast in any movies"
        elif len(self.movies) == 1:
            movies = "This actor has been cast in "+ str(len(self.movies)) +" movie"
        else:
            movies = "This actor has been cast in "+ str(len(self.movies)) +" movies"
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "movies": movies

        }
    
    #TODO: is this needed?
    def __repr__(self):
        return f'Actor: {self.id}, {self.name}, {self.age}, {self.gender}'

# ----------------------------------------------------------------------------#
# Movie Model
# ----------------------------------------------------------------------------#
class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    #TODO - check default is correct
    # default=datetime.now()
    release_date = db.Column(db.DateTime(), nullable=False)
    genre = db.Column(db.Enum(GenreEnum), nullable=False)
    # Ref: https://knowledge.udacity.com/questions/510080#510112
    # The backref is now considered legacy
    # Ref: https://docs.sqlalchemy.org/en/20/orm/backref.html
    actors = db.relationship(
            'Actor',
            secondary="actors_movies",
            back_populates="movies"
    #     lazy=True,
    #     # Ref: https://knowledge.udacity.com/questions/637391#637486
    #     cascade="all, delete"
    )

    '''
    insert()
        inserts a new model into a database
        the model must have a unique id or null id
        EXAMPLE
            actor = Actor(name=req_name, age=27, gender=Male)
            actor.insert()
    '''

    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    update()
        updates a model in a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.name = 'Tom Cruise'
            actor.update()
    '''

    def update(self):
        db.session.commit()

    '''
    delete()
        deletes a model from database
        the model must exist in the database
        EXAMPLE
            actor = Actor(name=req_name, age=27, gender=Male)
            actor.delete()
    '''

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

    def format(self):
        # Ref: https://www.geeksforgeeks.org/python-ways-to-find-length-of-list/?ref=lbp
        if len(self.actors) == 0:
            actors = "This movie has no actors"
        elif len(self.actors) == 1:
            actors = "This movie has "+ str(len(self.actors)) +" actor"
        else:
            actors = "This movie has "+ str(len(self.actors)) +" actors"
        return {
            "id": self.id,
            "title": self.title,
            "release date": self.release_date,
            "genre": self.genre,
            "actors": actors
        }
    #TODO: is this needed?
    def __repr__(self):
        return f'Actor: {self.id}, {self.title}, {self.release_date}'