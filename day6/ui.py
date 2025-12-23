from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain
import time

class Quiz_Interface:
    def __init__(self, quiz_data: QuizBrain):
        self.score = 0
        self.quiz_data = quiz_data
        self.window = Tk()
        self.window.title("Quiz App")

        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2)


        # Image Import
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1,row=0, padx=20, pady=20)
        self.question = self.canvas.create_text(150,125, width =300, text="Something", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.true_button.grid(column=0, row=2, padx=20, pady=20)
        self.false_button.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz_data.still_has_questions():
            q_text =self.quiz_data.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"You have reached the end of the quiz!\nThe final result is: {self.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true(self):
        self.give_feedback(self.quiz_data.check_answer("True"))
    def false(self) -> None:
        self.give_feedback(self.quiz_data.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





