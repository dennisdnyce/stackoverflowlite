import pytest
import unittest
import json
import os
from app import create_app


from app.api.v1.models.models import UserQuestions, AnswerQuestions
from app.api.v1.views.views import question, answer
from app.api.v1.utils.validators import validate_question, validate_answer

class TestUserQuestions(unittest.TestCase):
    ''' This class represents the User Questions test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()

        self.question ={
            'qntitle': 'Computing is a Science',
            'qntags': 'This is the description',
            'qnbody': 'I am the question body',
            }

        self.answer = {
            'ansbody': 'this is an answer'
        }

    def tearDown(self):
        del question.All_Questions[:]
        del answer.All_Answers[:]

    def test_post_answer_to_non_existing_question(self):
        ''' tests that a user cannot post an answer to a non-existing question '''
        response = self.client.post("/api/v1/questions/3/answers", data=json.dumps(dict(questionId=5, ansbody="my answer")), content_type="application/json")
        self.assertEqual(response.status_code, 404)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question not found!", response_msg["Message"])

    def test_post_answer_to_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)

    def test_get_single_answer_to_single_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)
        resp = self.client.get("api/v1/questions/1/answers/1", content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_non_existing_answer_to_single_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)
        resp = self.client.get("api/v1/questions/1/answers/3", content_type='application/json')
        self.assertEqual(resp.status_code, 404)

    def test_non_existing_question_to_single_answer(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)
        resp = self.client.get("api/v1/questions/3/answers/1", content_type='application/json')
        self.assertEqual(resp.status_code, 404)

    def test_get_all_answers_to_single_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)
        resp = self.client.get("api/v1/questions/1/answers", content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_get_all_answers_to_non_existing_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.post("api/v1/questions/1/answers", content_type='application/json', data=json.dumps(self.answer))
        self.assertEqual(res.status_code, 201)
        resp = self.client.get("api/v1/questions/3/answers", content_type='application/json')
        self.assertEqual(resp.status_code, 404)

''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
