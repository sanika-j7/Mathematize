from data import qdata
from ques import Question
from brain import QB
question_bank = []
for question in qdata:
    qtext = question["question"]
    qans = question["correct_answer"]
    newq = Question(qtext, qans)
    question_bank.append(newq)
quiz = QB(question_bank)
while quiz.still_has_questions():
    quiz.nextq()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.qno}")