from flask import Flask, request, jsonify, Blueprint
from datetime import datetime

myapi = Blueprint('qn1', __name__, url_prefix='/api/v1')
#local imports
from ..models.models import UserQuestions, AnswerQuestions
from ..utils.validators import validate_question, validate_answer

question = UserQuestions('qntitle', 'qntags', 'qnbody')
answer = AnswerQuestions('ansbody')

@myapi.route('/questions', methods=['POST'])
def post_question():
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
