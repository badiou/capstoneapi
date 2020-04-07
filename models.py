#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from sqlalchemy import Column, String, Integer, create_engine, Date
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import date

database_name = 'capstonedb'
database_path = 'postgresql://{}:{}@{}/{}'.format('postgres', 'badiou',
        'localhost:5432', database_name)

db = SQLAlchemy()

ENV = 'prod'


def setup_db(app, database_path=database_path):
    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = database_path
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:

        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = \
            'postgres://urbivbabugqsxp:b0f0d0a89407c9887c2b1b58cc9cb7b68a15f81546aee13f68ce4539a88f7548@ec2-3-229-210-93.compute-1.amazonaws.com:5432/df2g9tkipvj2t1'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()


#################################################################################################################################################
#
#                           Model Actor

################################################################################################################################################

class Actor(db.Model):

    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    performs = db.relationship('Perform', backref=db.backref('actors',
                               lazy=True))

    def __init__(
        self,
        name,
        age,
        gender,
        ):

        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            }


##################################################################################################################################################
#
#                           Model Movie

#################################################################################################################################################

class Movie(db.Model):

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    performs = db.relationship('Perform', backref=db.backref('movies',
                               lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {'id': self.id, 'title': self.title,
                'release_date': self.release_date}


################################################################################################################################################
#
#                           Model Perform

###############################################################################################################################################

class Perform(db.Model):

    __tablename__ = 'performs'
    id = db.Column(db.Integer, primary_key=True)
    actors_id = db.Column(db.Integer, db.ForeignKey('movies.id'),
                          nullable=False)
    movies_id = db.Column(db.Integer, db.ForeignKey('actors.id'),
                          nullable=False)
    role = db.Column(String)

    def __init__(
        self,
        actors_id,
        movies_id,
        role,
        ):

        self.actors_id = actors_id
        self.movies_id = movies_id
        self.role = role

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'actors_id': self.actors_id,
            'movies_id': self.movies_id,
            'role': self.role,
            }



			