from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import Quiz_Interface
import random

parameters = {
    "amount": 10,
    "type": "boolean"
}
problems = requests.get("https://opentdb.com/api.php", params=parameters)
problems.raise_for_status()
data = problems.json()
question_data = data['results']


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
ui = Quiz_Interface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
