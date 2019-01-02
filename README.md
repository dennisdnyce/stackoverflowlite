[![Build Status](https://travis-ci.org/dennisdnyce/stackoverflowlite.svg?branch=develop)](https://travis-ci.org/dennisdnyce/stackoverflowlite)[![Coverage Status](https://coveralls.io/repos/github/dennisdnyce/stackoverflowlite/badge.svg?branch=develop&kill_cache=1)](https://coveralls.io/github/dennisdnyce/stackoverflowlite?branch=develop)[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)[![MIT license](http://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

# StackOverflow-Lite-API
StackOverflow-Lite is a mock platform of the main site http://stackoverflow.com where any user is allowed to register for an account and ask questions or provide answers to the relevant topics based on his/her knowledge base.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Watch out for the deployment notes on how to deploy the project on a live system.

### Implemented Endpoints
- [POST /auth/signup]
- [POST /questions]
- [GET /questions]
- [GET /questions/< int:questionId >]
- [DELETE /questions/< int:questionId >]
- [POST /questions/< int:questionId >/answers]
- [GET /questions/< int:questionId >/answers]
- [GET /questions/< int:questionId >/answers/< int:answerId >]

### Prerequisites
The things you need to setup the project and its relevant configuration.
```
Firstly, visit the link > https://dennisdnyce.github.io/stackoverflowlite/UI to preview the design of the project's user interface as projected on github-pages(gh-pages)
```
```
git clone http://github.com/dennisdnyce/stackoverflowlite.git
```
```
cd stackoverflowlite
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
* Endless Motivation from friends and family 
