#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Movie, Actor, Perform
from datetime import date
from config import myTokens

assistant_auth_header = {'Authorization': myTokens['assistant']}

director_auth_header = {'Authorization': myTokens['director']}

producer_auth_header = {'Authorization': myTokens['producer']}


class CapstoneTestCase(unittest.TestCase):

    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'capstonedb_test'
        self.database_path = \
            'postgresql://{}:{}@{}/{}'.format('postgres', 'badiou',
                'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            # create all tables

            self.db.create_all()

        self.new_movie = {'title': 'Titanic',
                          'release_date': '2000-03-03'}
        self.new_actor = {'name': 'Leonardo DICAPRIO', 'age': 40,
                          'gender': 'M'}

    def tearDown(self):
        """Executed after reach test"""

        pass

#################################################################################################################
#               TEST GET ALL MOVIES STATUS_CODE=200..... STATUS_CODE=404.............. STATUS=401
#################################################################################################################

    def test_get_all_movies(self):
        res = self.client().get('/movies',
                                headers=assistant_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_error_401_get_all_movies(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_error_404_get_movies(self):
        res = self.client().get('/movies?page=10000',
                                headers=assistant_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

#################################################################################################################
#               TEST GET ALL ACTORS STATUS_CODE=200..... STATUS_CODE=404........STATUS=401
#################################################################################################################

    def test_get_all_actors(self):
        res = self.client().get('/actors',
                                headers=assistant_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_error_401_get_all_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])

    def test_error_404_get_actors(self):
        res = self.client().get('/actors?page=10000',
                                headers=assistant_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])

#################################################################################################################
#               TEST STATUS_CODE 403 FOR DELETE ACTOR BY CASTING ASSISTANT
#################################################################################################################

    def test_error_403_delete_actor(self):
        res = self.client().delete('/actors/1',
                                   headers=assistant_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No permission found.')

#################################################################################################################
#               TEST STATUS_CODE 403 FOR DELETE ACTOR BY CASTING DIRECTOR
#################################################################################################################

    def test_error_403_delete_movie(self):
        res = self.client().delete('/movies/1',
                                   headers=director_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No permission found.')

#################################################################################################################
#               TEST STATUS_CODE 200 ADD ACTOR BY CASTING DIRECTOR
#################################################################################################################

    def test_create_new_question(self):
        res = self.client().post('/actors', json=self.new_actor,
                                 headers=director_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['total_actors']))

#################################################################################################################
#               TEST STATUS_CODE 200 CREATE MOVIE BY EXCECUTIVE PRODUCER
#################################################################################################################

    def test_create_new_movie(self):
        res = self.client().post('/movies', json=self.new_movie,
                                 headers=producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['total_actors']))

#################################################################################################################
#               TEST STATUS_CODE 403 FOR CREATE MOVIE BY CASTING DIRECTOR
#################################################################################################################

    def test_error_403_create_movie(self):
        res = self.client().delete('/movies/1',
                                   headers=director_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'No permission found.')

#################################################################################################################
#               TEST STATUS_CODE 404 FOR PATCH MOVIE BY CASTING EXECUTIVE PRODUCER
#################################################################################################################

    def test_error_404_update_movie(self):
        updatted_movie = {'title': 'Black Panthers',
                          'release_date': '3000-06-03'}
        res = self.client().patch('/movies/1000', json=updatted_movie,
                                  headers=producer_auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'],
                         'Movie with id 123412 not found in database.')

#################################################################################################################
#               TEST STATUS_CODE 200 FOR PATCH MOVIE BY CASTING EXECUTIVE PRODUCER
#################################################################################################################

    def test_update_movie(self):
        res = self.client().patch('/movies/1', json=self.new_movie,
                                  headers=producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['id'], 1)

#################################################################################################################
#               TEST STATUS_CODE 200 FOR PATCH ACTOR BY CASTING EXECUTIVE PRODUCER
#################################################################################################################

    def test_update_actor(self):
        res = self.client().patch('/actors/1', json=self.new_actor,
                                  headers=producer_auth_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['id'], 1)


if __name__ == '__main__':
    unittest.main()

			