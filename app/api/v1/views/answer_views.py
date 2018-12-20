from flask import Flask, request, jsonify, Blueprint
from datetime import datetime


myanswers = Blueprint('an1', __name__, url_prefix='/api/v1')
#local imports
from ..models.answer_models import AnswerQuestions
from ..models.question_models import UserQuestions
from ..utils.validators import validate_answer

question = UserQuestions('qntitle', 'qntags', 'qnbody')
answer = AnswerQuestions('ansbody')

@myanswers.route('/questions/<int:questionId>/answers', methods=['POST'])
def post_answer(questionId):
    questionId = question.get_a_question(questionId)

    return jsonify({"Status": "Ok", "Question": questionId}), 200

@myanswers.route('/questions/<int:questionId>/answers/<int:answerId>', methods=['GET'])
def get_answer(questionId, answerId):
    for i in question.All_Questions:
        if i['questionId'] == questionId:
            j = answer.get_an_answer(answerId)
            if j:
                return jsonify({"Status": "Ok", "Answer": j}), 200
            return jsonify({"Message" : "Answer not found", "Status" : "Error"}), 404
        return jsonify({"Message" : "Question not found", "Status" : "Error"}), 404
