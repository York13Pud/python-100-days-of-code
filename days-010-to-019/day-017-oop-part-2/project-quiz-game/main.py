from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# --- Create a blank list:
question_bank = []

# --- Loop through the dictionaries in the list, create a question and answer variable
# pass the variables to the Question class to create a new object and then add the object to the question_bank list:
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question = question_text,answer = question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_list = question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.\n")
print(f"Your score was: {quiz.score} out of {quiz.question_number}")