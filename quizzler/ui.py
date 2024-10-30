from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizzInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quizz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, text="Test", font=("Aril", 25, "italic"),
                                                     fill=THEME_COLOR, width=280)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        true_logo = PhotoImage(file="quizzler/images/true.png")
        self.true_button = Button(image=true_logo, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_logo = PhotoImage(file="quizzler/images/false.png")
        self.false_button = Button(image=false_logo, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz.still_has_questions():
            self.label.config(text=f"Score: {self.quizz.score}")
            q_text = self.quizz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You´ve reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quizz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quizz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
