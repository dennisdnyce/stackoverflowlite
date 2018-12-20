from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

myquestions = Blueprint('qn1', __name__, url_prefix='/api/v1')
#local imports
from ..models.question_models import UserQuestions
from ..utils.validators import validate_question

question = UserQuestions('qntitle', 'qntags', 'qnbody')

@myquestions.route('/questions', methods=['GET'])
def get_questions():
    return jsonify({"All_Questions": question.All_Questions}), 200

@myquestions.route('/questions', methods=['POST'])
def post_question():
    data = request.get_json()
    if not data:
        return jsonify({"Message": "All fields cannot be empty!"}), 400
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

@myquestions.route('/questions/<int:questionId>', methods=['GET'])
def get_question(questionId):
    i = question.get_a_question(questionId)
    if i:
        return jsonify({"Status": "Ok", "Question": i}), 200
    return jsonify({"Message": "Question not found!", "Status": "error"}), 404

@myquestions.route('/questions/<int:questionId>', methods=['DELETE'])
def delete_question(questionId):
    k = question.delete_a_question(questionId)
    if k:
        question.All_Questions.remove(k)
        return jsonify({"Message": "Question deleted successfully", "status": "ok"}), 200
    return jsonify({"Message": "Question does not exist!", "status": "error"}), 404
