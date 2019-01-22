[![Build Status](https://travis-ci.org/dennisdnyce/stackoverflowlite.svg?branch=develop)](https://travis-ci.org/dennisdnyce/stackoverflowlite)[![Coverage Status](https://coveralls.io/repos/github/dennisdnyce/stackoverflowlite/badge.svg?branch=develop&kill_cache=1)](https://coveralls.io/github/dennisdnyce/stackoverflowlite?branch=develop)[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

# StackOverflow-Lite-API
StackOverflow-Lite is a mock platform of the main site <a href="http://stackoverflow.com" target="_blank">http://stackoverflow.com</a>where any user is allowed to register for an account and ask questions or provide answers to the relevant topics based on his/her knowledge base.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Watch out for the deployment notes on how to deploy the project on a live system.

### NOTE
- The project is managed by the PivotalTracker software management platform <a href="https://www.pivotaltracker.com/n/projects/2231122" target="_blank">follow link to preview</a>
- The project documentation is not yet created
- The app is not yet hosted on heroku

### Implemented Endpoints
| Endpoint       | Prefix     | Description     |
| :------------- | :----------: | -----------: |
|  **[POST /auth/signup]** | `/api/v1`   | _Signs up a user_    |
|**[POST /questions]**   | `/api/v1` | _Posts a question_  |
| **[GET /questions]**   | `/api/v1` | _Gets all questions_ |
| **[GET /questions/< int:questionId >]**   | `/api/v1` | _Retrieves a question_ |
| **[DELETE /questions/< int:questionId >]**   | `/api/v1` | _Deletes a question_ |
| **[POST /questions/< int:questionId >/answers]**   | `/api/v1` | _Posts an answer to a question_ |

### Prerequisites
The things you need to setup the project and its relevant configuration.

```
1. Python3
2. Flask Microframework
3. Postman for testing the API endpoints

```
### Installation

```
- Firstly, visit the link > <a href="https://dennisdnyce.github.io/stackoverflowlite/UI" target="_blank"> https://dennisdnyce.github.io/stackoverflowlite/UI </a> to preview the design of the project's user interface as projected on github-pages(gh-pages)
- git clone http://github.com/dennisdnyce/stackoverflowlite.git
- cd stackoverflowlite
- install dependencies :~$ sudo apt install python-pip
- install virtualenv :~$ sudo pip install virtualenv
- create a virtual environment :~$ virtualenv myvenv
- activate the virtual environment :~$ source myvenv/bin/activate
- install project dependencies :~$(myenv) pip install -r requirements.txt
- set up the project running environment :~$(myenv)export FLASK_ENV = development
                                         :~$(myenv)export FLASK_DEBUG = 1
                                         :~$(myenv)export FLASK_APP = run.py
- run the project :~$(myenv)flask run                                          
```
## Running Tests
```
- pytest :~$(myenv)py.test --cov app/ tests/

- checking test coverage :~$(myenv)coverage report -m 
```
## Testing on Postman
### User Endpoints
```
-To Register a user [POST /auth/signup] use the url 127.0.0.1:5000/api/v1/auth/signup

```
### Question Endpoints
```
-To Post Questions [POST /questions] use the url 127.0.0.1:5000/api/v1/auth/signup
-To Get posted questions [GET /questions] use the url 127.0.0.1:5000/api/v1/questions
-To Get specific posted question [GET /questions/< int:questionId >] use the url 127.0.0.1:5000/api/v1/questions/questionId
-To Delete user posted question [DELETE /questions/< int:questionId >] use the url 127.0.0.1:5000/api/v1/questions/questionId
```
### Answer Endpoints
```
-To Post answers to a question [POST /questions/< int:questionId >/answers] use the url 127.0.0.1:5000/api/v1/questions/questionId/answers
-To Get posted answers to a question [GET /questions/< int:questionId >/answers] use the url 127.0.0.1:5000/api/v1/questions/questionId/answers
-To Get single answer to a single question [GET /questions/< int:questionId >/answers/< int:answerId >] use the url 127.0.0.1:5000/api/v1/questions/questionId/answers/answerId
```

## Contributing
> To get Started...

### Step 1
- **Option 1**

      - 🍴 Fork this repo!
      
- **Option 2**   

      - 👯 Clone this repo to your local machine using `https://github.com/dennisdnyce/stackoverflowlite.git`
      
### Step 2
- **Hack away with one of your branches or you can use one of my many branches.**

### Step 3
- 🔃 Create a new pull request using <a href="https://github.com/dennisdnyce/stackoverflowlite/compare/" target="_blank">`https://github.com/dennisdnyce/stackoverflowlite/compare/`</a>.

## Authors

* **Dennis Juma** - *Initial Project* - (http://stackoverflow.com)

## Acknowledgments

* Andela-Nairobi Cycle-36 Cohorts
* Hat tip to anyone whose code was referenced
* Endless Motivation from family and friends 

## Licence
The stackoverflowlite project is licenced under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT</a> licence
