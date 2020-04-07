#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie, Perform
from auth import AuthError, requires_auth

# initialisation of number of movies or actors per page

number_per_page = 10


######################################################################################################################################
#
#                                        PAGINATE ACTORS
#
######################################################################################################################################

def paginate_actors(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * number_per_page
    end = start + number_per_page
    actors = [actor.format() for actor in selection]
    current_actors = actors[start:end]
    return current_actors


######################################################################################################################################
#
#                                       PAGINATE MOVIES
#
######################################################################################################################################

def paginate_movies(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * number_per_page
    end = start + number_per_page
    movies = [movie.format() for movie in selection]
    current_movies = movies[start:end]
    return current_movies


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

######################################################################################################################################
#
#                                        DECORATOR after_request
#
######################################################################################################################################

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response

########################################################################################################################################
#
#                                        GET ALL ACTORS & GET ONE ACTOR BY ID
#
#######################################################################################################################################

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_all_actors(payload):
        actors = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_actors(request, actors)
        if len(current_actors) == 0:
            abort(404)
        return jsonify({'success': True, 'actors': current_actors})

    @app.route('/actors/<int:actor_id>', methods=['GET'])
    @requires_auth('get:one-actor')
    def get_one_actor(payload, actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        if actor is None:
            abort(404)
        else:
            return jsonify({'success': True, 'actor': [actor.format()]})

#########################################################################################################################################
#
#                                        GET ALL MOVIES and GET ONE MOVIE BY ID
#
#########################################################################################################################################

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_all_movies(payload):
        movies = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_movies(request, movies)
        if len(current_movies) == 0:
            abort(404)
        return jsonify({'success': True, 'movies': current_movies,
                       'total_movies': len(Movie.query.all())})

    @app.route('/movies/<int:movie_id>', methods=['GET'])
    @requires_auth('get:one-movie')
    def get_one_movie(payload, movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        if movie is None:
            abort(404)
        else:
            return jsonify({'success': True, 'movie': [movie.format()]})

#########################################################################################################################################
#
#                                        POST ACTOR
#
########################################################################################################################################

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(payload):
        body = request.get_json()

        if not body:
            abort(400)

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)

        if not new_name:
            abort(400, {'Message': 'Request does not contain name'})

        if not new_age:
            abort(400, {'Message': 'Request does not contain age'})

        if not new_gender:
            abort(400, {'Message': 'Request does not contain gender'})

        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        actor.insert()
        selection = Actor.query.order_by(Actor.id).all()
        current_actors = paginate_actors(request, selection)

        return jsonify({
            'success': True,
            'created': actor.id,
            'actors': current_actors,
            'total_actors': len(Actor.query.all()),
            })

#########################################################################################################################################
#
#                                        POST MOVIE
#
########################################################################################################################################

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(payload):
        body = request.get_json()

        if not body:
            abort(400)
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)
        if not new_title:
            abort(400, {'Message': 'Request does not contain title'})

        if not new_release_date:
            abort(400,
                  {'Message': 'Request does not contain release_date'})

        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()
        selection = Movie.query.order_by(Movie.id).all()
        current_movies = paginate_movies(request, selection)

        return jsonify({
            'success': True,
            'created': movie.id,
            'movies': current_movies,
            'total_movies': len(Movie.query.all()),
            })

###############################################################################################################################################
#
#                                        DELETE ACTOR
#
##############################################################################################################################################

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        try:
            actor = Actor.query.filter(Actor.id
                    == actor_id).one_or_none()
            if actor is None:
                abort(404)
            actor.delete()
            selection = Actor.query.order_by(Actor.id).all()
            current_actors = paginate_actors(request, selection)
            return jsonify({
                'success': True,
                'deleted': actor_id,
                'actors': current_actors,
                'total_actors': len(Actor.query.all()),
                })
        except:
            abort(422)  # Unprocessable Entity

###############################################################################################################################################
#
#                                        DELETE MOVIE
#
##############################################################################################################################################

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        try:
            movie = Movie.query.filter(Movie.id
                    == movie_id).one_or_none()
            if movie is None:
                abort(404)
            movie.delete()
            selection = Movie.query.order_by(Movie.id).all()
            current_movies = paginate_movies(request, selection)
            return jsonify({
                'success': True,
                'deleted': movie_id,
                'actors': current_movies,
                'total_movies': len(Movie.query.all()),
                })
        except:
            abort(422)  # Unprocessable Entity

############################################################################################################################################
#
#                                        PATCH ACTOR
#
############################################################################################################################################

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actor')
    def update_actor(payload, actor_id):
        try:
            body = request.get_json()
            actor_updated = Actor.query.filter(Actor.id
                    == actor_id).one_or_none()
            if actor_updated is None:
                abort(404)
            if 'age' in body and 'name' in body and 'gender' in body:
                actor_updated.name = body.get('name', None)
                actor_updated.age = body.get('age', None)
                actor_updated.gender = body.get('gender', None)
            actor_updated.update()
            return jsonify({'success': True, 'id': actor_updated.id,
                           'actor': [actor_updated.format()]})
        except:
            abort(400)

############################################################################################################################################
#
#                                        PATCH MOVIE
#
############################################################################################################################################

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movie')
    def update_movie(payload, movie_id):
        try:
            body = request.get_json()
            movie_updated = Movie.query.filter(Movie.id
                    == movie_id).one_or_none()
            if movie_updated is None:
                abort(404)
            if 'title' in body and 'release_date' in body:
                movie_updated.title = body.get('title', None)
                movie_updated.release_date = body.get('release_date',
                        None)

            movie_updated.update()
            return jsonify({'success': True, 'id': movie_updated.id,
                           'movie': [movie_updated.format()]})
        except:
            abort(400)

############################################################################################################################################
#
#                                        ERROR HANDLING
#
############################################################################################################################################

    @app.errorhandler(422)
    def unprocessable(error):
        return (jsonify({'success': False, 'error': 422,
                'message': 'Unprocessable'}), 422)

    @app.errorhandler(400)
    def bad_request(error):
        return (jsonify({'success': False, 'error': 400,
                'message': 'Bad request'}), 400)

    @app.errorhandler(404)
    def ressource_not_found(error):
        return (jsonify({'success': False, 'error': 404,
                'message': 'Not found'}), 404)

    @app.errorhandler(AuthError)
    def get_auth_eror(AuthError):
        return (jsonify({'success': False, 'error': 401,
                'message': AuthError.error}), 401)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

			