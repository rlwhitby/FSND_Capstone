import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, db_drop_and_create_all, Movie, Actor
# Reference: https://knowledge.udacity.com/questions/857358
# from settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

# Find reference for this part of setup
#https://knowledge.udacity.com/questions/972850
# tokens exist in setup.sh
# https://knowledge.udacity.com/questions/533049
TEST_DATABASE_URI = os.environ['TEST_DATABASE_URI']
ASSISTANT_TOKEN = os.environ['ASSISTANT_TOKEN']
DIRECTOR_TOKEN = os.environ['DIRECTOR_TOKEN']
PRODUCER_TOKEN = os.environ['PRODUCER_TOKEN']

# is this good practice? find reference
# VALID_ACTOR = {"name": "valid actor", "age": 54, "gender": "male"}
# INVALID_ACTOR = {"name": "invalid"}
#  VALID_ACTOR_PATCH = {"age": 46}

class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone project test case"""

    def setUp(self):
        """Define test variables and initialize app."""

        # https://knowledge.udacity.com/questions/373159
        # read again  - might be useful?
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_DATABASE_URI)
        self.casting_assistent = ASSISTANT_TOKEN
        self.casting_director = DIRECTOR_TOKEN
        self.executive_producer = PRODUCER_TOKEN

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            db_drop_and_create_all()

    def tearDown(self):
        """Executed after each test"""
        pass

    #Ref: https://knowledge.udacity.com/questions/294099
    # helper function that produces a header in the correct format

    # https://knowledge.udacity.com/questions/492044
    # if issues with self. being passed
    def get_headers(token):
        return {"Authorization": f"Bearer {token}"}
    """
    TODO
    Write at least one test for each test for successful operation and
    for expected errors.
    """
    # Ref: https://knowledge.udacity.com/questions/972850
    def test_get_actors(self):
        """ The test_get_actors test uses the GET method and the correct
        authorisation to get all the avaliable actors from the test database.

        The assert statements check that the endpoint returns:
        - a status code of 200
        - a json object with: 
            - a "success" value of True, and
            - that "actors" contains values.
        """
        res = self.client().get("/actors")
        #TODO
        # auth_header = get_headers(self.casting_assistent)
        # res = self.client().get("/actors",
        #                         headers=auth_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    # # Ref: https://knowledge.udacity.com/questions/350483
    # def test_405_get_categories_wrong_method(self):
    #     """ The test_405__get_categories test uses the incorrect
    #     POST method to validate that the expected HTTP exception is
    #     raised if the incorrect method is used to query the endpoint.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 405
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "method not allowed".
    #     """
    #     res = self.client().post("/categories")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "method not allowed")

    # def test_get_paginated_questions(self):
    #     """ The test_get_paginated_questions test uses the GET method to
    #     get all the avaliable questions from the test database.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True
    #         - that "questions" contains values
    #         - a total number of questions
    #         - that "categories" contains values
    #         - that "current_cateogry" is None
    #     """
    #     res = self.client().get("/questions")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     # There should be questions in the list
    #     self.assertTrue(len(data["questions"]))
    #     self.assertTrue(data["total_questions"])
    #     self.assertTrue(len(data["categories"]))
    #     self.assertEqual(data["current_category"], None)

    # def test_404_get_questions_beyond_valid_page(self):
    #     """ The test_404_get_questions_beyond_valid_page test uses
    #     a page that would not contain data (1000) to validate that the
    #     expected HTTP exception is raised if no questions were found.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 404
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "resource not found".
    #     """
    #     res = self.client().get("/questions?page=1000")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "resource not found")

    # # Ref: from API Development and Documentation Course
    # # Delete a different question in each attempt
    # def test_delete_question(self):
    #     """ The test_delete_question test uses the DELETE method to
    #     delete a question from the test database.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True, and
    #         - a "deleted" value matching the id in the endpoint.
    #     """
    #     res = self.client().delete("/questions/2")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertEqual(data["deleted"], 2)

    # def test_404_delete_question_does_not_exist(self):
    #     """ The test_404_delete_question_does_not_exist test validates
    #     that the expected HTTP exception is raised if the deletion of
    #     a question that does not exist in the database is attempted.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 404
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "resource not found".
    #     """
    #     res = self.client().delete("/questions/1000")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "resource not found")

    # def test_create_new_question(self):
    #     """ The test_create_new_question test uses the POST method to
    #     add a new question to the test database.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True, and
    #         - a "created" value.
    #     """
    #     res = self.client().post(
    #         "/questions/add",
    #         json={"question": "new question",
    #               "answer": "new answer",
    #               "category": "1",
    #               "difficulty": 4}
    #         )
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["created"])

    # def test_422_if_question_invalid(self):
    #     """ The test_422_if_question_invalid test uses an incorrect
    #     category type (integer instead of string) to validate that the
    #     expected HTTP exception is raised if the incorrect json data is
    #     passed to the endpiont.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 422
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "unprocessable".
    #     """
    #     # Category is incorrectly added as an int value
    #     res = self.client().post(
    #         "/questions/add",
    #         json={"question": "invalid question",
    #               "answer": "new answer",
    #               "category": 0,
    #               "difficulty": 4
    #               })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "unprocessable")

    # def test_get_questions_from_search(self):
    #     """ The test_get_questions_from_search test uses the POST
    #     method to return questions based on a given search term from
    #     the test database.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True
    #         - that "questions" contains values
    #         - a total number of questions, and
    #         - that "current_cateogry" is None.
    #     """
    #     res = self.client().post("/questions/search",
    #                              json={'searchTerm': 'who'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     # There should be questions in the list
    #     self.assertTrue(data["questions"])
    #     self.assertTrue(data["total_questions"])
    #     self.assertEqual(data["current_category"], None)

    # def test_404_no_search_result(self):
    #     """ The test_404_no_search_result test uses a search term that
    #     does not exist in any question in the test database to validate
    #     that the expected HTTP exception is raised if no questions are
    #     found.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 404
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "resource not found".
    #     """
    #     res = self.client().post("/questions/search",
    #                              json={'searchTerm': 'xdt'})
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "resource not found")

    # def test_get_questions_by_category(self):
    #     """ The test_get_paginated_questions test uses the GET method to
    #     get all the avaliable questions from the test database.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True
    #         - that "questions" contains values
    #         - a total number of questions, and
    #         - that "current_cateogry" contains a value.
    #     """
    #     res = self.client().get("/categories/1/questions")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(len(data["questions"]))
    #     self.assertTrue(data["total_questions"])
    #     self.assertTrue(data["current_category"])

    # def test_404_no_questions_in_category(self):
    #     """ The test_404_no_questions_in_category test uses a category
    #     id that doesn't exist in the test database (1000) to validate
    #     that the expected HTTP exception is raised if no questions
    #     are found in the category.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 404
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "resource not found".
    #     """
    #     res = self.client().get("/categories/1000/questions")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 404)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "resource not found")

    # def test_play_quiz(self):
    #     """ The test_play_quiz test uses the POST method to
    #     qet a random question to play the quiz.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 200
    #     - a json object with: 
    #         - a "success" value of True, and
    #         - that "question" contains a value.
    #     """
    #     res = self.client().post('/quizzes', json={
    #         'quiz_category': {'type': 'Science', 'id': '1'},
    #         "previous_questions": [20, 21]
    #         })
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["question"])

    # def test_422_play_quiz_incomplete(self):
    #     """ The test_422_play_quiz_incomplete test uses an incomplete
    #     request body to validate that the expected HTTP exception is
    #     raised if incomplete json data is passed to the endpiont.

    #     The assert statements check that the endpoint returns:
    #     - a status code of 422
    #     - a json object with: 
    #         - a "success" value of False, and
    #         - a "message" of "unprocessable".
    #     """
    #     res = self.client().post('/quizzes', json={
    #         "previous_questions": [20, 21]})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "unprocessable")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
