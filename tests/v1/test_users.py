import pytest
import unittest
import json
import os
from app import create_app


from app.api.v1.models.models import UserRegistration
from app.api.v1.views.views import user
from app.api.v1.utils.validators import validate_users


class TestUserRegistration(unittest.TestCase):
    ''' This class represents the User Registration test case '''
    def setUp(self):
        ''' define test variables and initialize the app '''
        self.app = create_app(config='testing')
        self.client = self.app.test_client()

        self.user ={
            'username': 'dennisdnyce',
            'email': 'jumaspay@gmail.com',
            'password': 'thisispass',
            'confirm': 'thisispass',
            }

    def tearDown(self):
        del user.All_Users[:]

    def test_user_registration(self):
        ''' tests that a user can sign up for an account '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(self.user), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response_msg = json.loads(response.data.decode('UTF-8'))
        self.assertIn("Registration Successful", response_msg["Message"])

    def test_user_registration_no_username(self):
        ''' tests that a user cannot signup without a username '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="",
        email="jumaspay@gmail.com", password="thisispass", confirm="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Username is required", response_msg["Message"])

    def test_user_registration_no_password(self):
        ''' tests that a user cannot signup without a password '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="", confirm="")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password is required", response_msg["Message"])

    def test_user_registration_no_password_confirmation(self):
        ''' tests that a user cannot signup without password confirmation '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="thisispass", confirm="")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password confirmation is required", response_msg["Message"])

    def test_user_registration_password_mismatch(self):
        ''' tests that a user cannot signup without confirming registered password '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="thisispass", confirm="thispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password mismatch", response_msg["Message"])

    def test_user_registration_password_too_short(self):
        ''' tests that a user cannot signup with password length less than 8 characters '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="thisisp", confirm="thisisp")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["Message"])

    def test_user_registration_password_too_long(self):
        ''' tests that a user cannot signup with password length more than 12 characters '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="thisispasswordlong", confirm="thisispasswordlong")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Password length should be atleast 8 characters long and atmost 12 characters long", response_msg["Message"])

    def test_user_registration_no_email(self):
        ''' tests that a user cannot signup without an email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="", password="thisispass", confirm="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Email is required", response_msg["Message"])

    def test_user_registration_invalid_email1(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay", password="thisispass", confirm="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["Message"])

    def test_user_registration_invalid_email2(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail", password="thisispass", confirm="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["Message"])

    def test_user_registration_invalid_email3(self):
        ''' tests that a user cannot signup with an invalid email address '''
        response = self.client.post("/api/v1/auth/signup", data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.", password="thisispass", confirm="thisispass")), content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Invalid email", response_msg["Message"])

    def test_get_all_registered_users(self):
        ''' tests that a a registered user can query all other registered users '''
        response = self.client.post("/api/v1/auth/signup", content_type='application/json', data=json.dumps(self.user))
        self.assertEqual(response.status_code, 201)
        res = self.client.get("/api/v1/users", content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_get_a_registered_user(self):
        ''' tests that a registered user can query another registered user '''
        response = self.client.post("/api/v1/auth/signup", content_type='application/json', data=json.dumps(dict(username="dnyce",
        email="jumaspay@gmail.com", password="thisispass", confirm="thisispass")))
        response = self.client.get("/api/v1/users/1", data=json.dumps(dict(userId=1)), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_a_non_registered_user(self):
        ''' tests that a registered user can query another registered user '''
        response = self.client.post("/api/v1/auth/signup", content_type='application/json', data=json.dumps(dict(username="ddnyce",
        email="jumaspay@gmail.com", password="thisispass", confirm="thisispass")))
        response = self.client.get("/api/v1/users/10", data=json.dumps(dict(userId=1)), content_type='application/json')
        self.assertEqual(response.status_code, 404)


''' make tests conveniently executable '''
if __name__ == '__main__':
    unittest.main()
