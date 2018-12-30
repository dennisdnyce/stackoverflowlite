from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

myapi = Blueprint('qn1', __name__, url_prefix='/api/v1')
#local imports
from ..models.models import UserQuestions, AnswerQuestions, UserRegistration
from ..utils.validators import validate_users, validate_question, validate_answer

question = UserQuestions('qntitle', 'qntags', 'qnbody')
answer = AnswerQuestions('ansbody')
user = UserRegistration('username', 'email', 'password', 'confirm')

@myapi.route('/auth/signup', methods=['POST'])
def register_user():
    ''' method to register a user on the application '''
    data = request.get_json()
    userId = len(user.All_Users) + 1
    username = data['username']
    email = data['email']
    password = data['password']
    confirm = data['confirm']
    usrtimeposted = user.usrtimeposted
    user.post_a_user(userId, username, email, password, confirm, usrtimeposted)
    user_validator = validate_users(data)

    if (user_validator != True):
        return user_validator
    return jsonify({"Message": "Registration Successful", "Welcome": username, "User Since": usrtimeposted, "id": userId}), 201

@myapi.route('/users/<int:userId>', methods=['GET'])
def get_registered_user(userId):
    ''' method to get a registered user '''
    usr = user.get_a_user(userId)
    if usr:
        return jsonify({"Status": "Ok", "ID": userId}), 200
    return jsonify({"Message": "User not found!", "Status": "error"}), 404

@myapi.route('/users', methods=['GET'])
def get_all_registered_users():
    ''' method to get all the registered users '''
    return jsonify({"All_Users": user.All_Users}), 200

@myapi.route('/questions', methods=['POST'])
def post_question():
    ''' method to post a single question '''
    data = request.get_json()
    questionId = len(question.All_Questions) + 1
    qntitle = data['qntitle']
    qntags = data['qntags']
    qnbody = data['qnbody']
    qntimeposted = question.qntimeposted
    question.post_a_question(questionId, qntitle, qntags, qnbody, qntimeposted)
    question_validator = validate_question(data)

    if (question_validator != True):
        return question_validator
    return jsonify({"Message": "You have successfully posted a question", "Question_Post": data}), 201

@myapi.route('/questions', methods=['GET'])
def get_questions():
    ''' method to get all the posted questions '''
    return jsonify({"All_Questions": question.All_Questions}), 200

@myapi.route('/questions/<int:questionId>', methods=['GET'])
def get_question(questionId):
    ''' method to get a single posted question '''
    i = question.get_a_question(questionId)
    if i:
        return jsonify({"Status": "Ok", "Question": i}), 200
    return jsonify({"Message": "Question not found!", "Status": "error"}), 404

@myapi.route('/questions/<int:questionId>', methods=['DELETE'])
def delete_question(questionId):
    ''' method to delete a single posted question '''
    k = question.delete_a_question(questionId)
    if k:
        question.All_Questions.remove(k)
        return jsonify({"Message": "Question deleted successfully", "status": "ok"}), 200
    return jsonify({"Message": "Question does not exist!", "status": "error"}), 404

@myapi.route('/questions/<int:questionId>/answers', methods=['POST'])
def post_answer(questionId):
    ''' method to post answers to a posted question '''
    i = question.get_a_question(questionId)
    if i:
        data = request.get_json()
        answerId = len(answer.All_Answers) + 1
        ansbody = data['ansbody']
        anstimeposted = answer.anstimeposted
        answer.post_an_answer(answerId, ansbody, anstimeposted)
        answer_validator = validate_answer(data)

        if (answer_validator != True):
            return answer_validator
        return jsonify({"Message": "Answer posted successfully", "Status": "Ok"}), 201
    return jsonify({"Message": "Question not found!"}), 404

@myapi.route('/questions/<int:questionId>/answers', methods=['GET'])
def get_answers(questionId):
    ''' method to get all the posted answers to a single question '''
    for qn in question.All_Questions:
        if qn['questionId'] == questionId:
            return jsonify({"Message": answer.All_Answers}), 200
        return jsonify({"Message": "Question related to answers query not found", "Status": "Error"}), 404

@myapi.route('/questions/<int:questionId>/answers/<int:answerId>', methods=['GET'])
def get_answer(questionId, answerId):
    ''' method to get a single answer to a single posted question '''
    for i in question.All_Questions:
        if i['questionId'] == questionId:
            ans = answer.get_an_answer(answerId)
            if ans:
                return jsonify({"Status": "Ok", "Answer": ans}), 200
            return jsonify({"Message" : "Answer not found", "Status" : "Error"}), 404
        return jsonify({"Message" : "Question not found", "Status" : "Error"}), 404
