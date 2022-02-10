class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def still_has_questions(self):
        # returns True if less and false if not:
        return self.question_number < len(self.question_list)
            
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q-{self.question_number}: {current_question.question}. True or False?: ")
        self.check_answer(users_answer, current_question.answer)
        
    def check_answer(self, users_answer, correct_answer):
        if users_answer.lower() == correct_answer.lower():
            print(f"\nThe answer is {correct_answer.lower()}. You are correct.")
            self.score += 1
            print(f"Your score is: {self.score} of {self.question_number}\n")
        else:
            print(f"The answer is {correct_answer.lower()}. You're answer was incorrect")
            print(f"Your score is: {self.score} of {self.question_number}\n")
        