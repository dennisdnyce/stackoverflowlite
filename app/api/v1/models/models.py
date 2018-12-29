from datetime import datetime

class UserQuestions():
    def __init__(self, qntitle, qntags, qnbody):
        self.qntitle = qntitle
        self.qntags = qntags
        self.qnbody = qnbody
        self.qntimeposted = datetime.now()
        self.All_Questions = []

    def post_a_question(self, questionId, qntitle, qntags, qnbody, qntimeposted):
        my_question = {
            "questionId": questionId,
            "qntitle": qntitle,
            "qntags": qntags,
            "qnbody": qnbody,
            "qntimeposted": qntimeposted
        }

        self.All_Questions.append(my_question)

    def get_a_question(self, questionId):
        for i in self.All_Questions:
            if i['questionId'] == questionId:
                return i

    def delete_a_question(self, questionId):
        for k in self.All_Questions:
            if k['questionId'] == questionId:
                return k

class AnswerQuestions():
    def __init__(self, ansbody):
        self.ansbody = ansbody
        self.anstimeposted = datetime.now()
        self.All_Answers = []

    def post_an_answer(self, answerId, ansbody, anstimeposted):
        my_answer = {
            "answerId": answerId,
            "ansbody": ansbody,
            "anstimeposted": anstimeposted
        }

        self.All_Answers.append(my_answer)

    def get_an_answer(self, answerId):
        for ans in self.All_Answers:
            if ans['answerId'] == answerId:
                return ans
