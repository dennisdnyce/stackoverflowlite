import pytest
import unittest
import json
import os
from app import create_app


from app.api.v1.models.models import UserQuestions
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

    def tearDown(self):
        del question.All_Questions[:]

    def test_post_question(self):
        ''' tests that a user can post a question '''
        response = self.client.post("/api/v1/questions", data=json.dumps(self.question), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("You have successfully posted a question", response_msg["Message"])

    def test_question_empty_title(self):
        ''' tests that a user cannot post a question without a question title '''
        response = self.client.post("/api/v1/questions", data=json.dumps(dict(qntitle="",
        qntags="tag me please", qnbody="no body here")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question title is required", response_msg["Message"])

    def test_question_empty_tags(self):
        ''' tests that a user cannot post a question without a question tag '''
        response = self.client.post("/api/v1/questions", data=json.dumps(dict(qntitle="title",
        qntags="", qnbody="no body here")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question tag(s) is required", response_msg["Message"])

    def test_question_empty_body(self):
        ''' tests that a user cannot post a question without a question body '''
        response = self.client.post("/api/v1/questions", data=json.dumps(dict(qntitle="title",
        qntags="i am a tag", qnbody="")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question body is required", response_msg["Message"])

    def test_fetch_all_questions(self):
        ''' tests that a user can fetch all the posted questions '''
        response = self.client.get("/api/v1/questions", data=json.dumps(dict()), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        res = json.loads(response.data.decode("UTF-8"))

    def test_delete_question(self):
        ''' tests that a user should be able to delete his/her posted questions '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.delete("/api/v1/questions/1", content_type='application/json')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client.get("/api/v1/questions/1")
        self.assertEqual(result.status_code, 404)

    def test_delete_non_existing_question(self):
        ''' tests that a user cannot delete a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.delete("api/v1/questions/10", content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_get_a_single_question(self):
        ''' tests that a user should be able to get a single posted questions '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.get("/api/v1/questions/1", content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_non_existing_question(self):
        ''' tests that a user should not be able to find a non-existing question '''
        response = self.client.post("/api/v1/questions", content_type='application/json', data=json.dumps(self.question))
        self.assertEqual(response.status_code, 201)
        res = self.client.get("/api/v1/questions/3", content_type='application/json')
        self.assertEqual(res.status_code, 404)


''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
