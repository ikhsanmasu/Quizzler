from tkinter import *
from quiz_brain import QuizBrain

import os
import sys

# use this directory when generating exe file
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

TRUE_IMAGE_DIR = application_path + "\\images\\true.png"
FALSE_IMAGE_DIR = application_path + "\\images\\false.png"

THEME_COLOR = "#375362"
# TRUE_IMAGE_DIR = "images/true.png"
# FALSE_IMAGE_DIR = "images/false.png"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR, font=("Ariel", 10, "bold"), fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Click to start", font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_button_img = PhotoImage(file=TRUE_IMAGE_DIR)
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, background=THEME_COLOR, command=self.true_passed)
        self.true_button.grid(column=0, row=2)

        self.false_button_img = PhotoImage(file=FALSE_IMAGE_DIR)
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, background=THEME_COLOR, command=self.false_passed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            data = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=data)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_passed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_passed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)



