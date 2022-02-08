from tkinter import *
from turtle import back, bgcolor
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
APP_TITLE = "Quizzler"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        # --- Construct the main window:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title(APP_TITLE)
        self.window.minsize(width=340, height=410)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)        
        
        # --- Create a label for the score:
        self.title = Label(text=APP_TITLE, fg="WHITE", bg=THEME_COLOR, font=("Ariel", 30, "bold"))
        self.title.grid(row=0, column=0, columnspan=2)
        
        # --- Create a label for the score:
        self.score = Label(text=f"Your Score: {self.quiz.score}", pady=30, fg="WHITE", bg=THEME_COLOR, font=("Ariel", 16, "bold"))
        self.score.grid(row=1, column=1, sticky="NE")
        
        # --- Create the canvas to  place the question:
        self.canvas = Canvas(width=300, height=250, bg="WHITE", highlightthickness=0, bd=0)
        
        # --- Create a label for the question:
        self.question_text = self.canvas.create_text(150,125, text="Question", fill="BLACK", font=("Ariel", 16, "bold"),width=280)
        
        # --- Create a button for true:
        self.tick_button_image = PhotoImage(file="./images/true.png")
        self.tick_button = Button(image=self.tick_button_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.answer_true)
        self.tick_button.grid(row=3, column=0, sticky="SW", pady=50)

        # --- Create a button for false:
        self.cross_button_image = PhotoImage(file="./images/false.png")
        self.cross_button = Button(image=self.cross_button_image, highlightthickness=0, bd=0, bg=THEME_COLOR, command=self.answer_false)
        self.cross_button.grid(row=3, column=1, sticky="SE", pady=50)
        
        # --- Display the canvas:
        self.canvas.grid(column=0, row=2, columnspan=2)
        self.get_next_question()
        # --- Keep the window active and checking for updates:
        self.window.mainloop()
        
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="WHITE")
            self.score.config(text=f"Your Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.config(text="Game Over!")
            self.canvas.itemconfig(self.question_text, text=f"Game Over!\nYour score was {self.quiz.score} / {len(self.quiz.question_list)}")  
            self.canvas.config(bg="WHITE")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")
            
    def answer_true(self):
        self.answer_response(self.quiz.check_answer(user_answer="True"))
            
    def answer_false(self):
        self.answer_response(self.quiz.check_answer(user_answer="False"))
        
    def answer_response(self, is_right):
        if is_right is True:
            self.canvas.config(background="GREEN") 
        else:
            self.canvas.config(background="RED")
        self.window.after(1000, self.get_next_question)