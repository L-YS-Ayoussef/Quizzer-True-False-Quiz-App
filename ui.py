from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # note 2
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.resizable(False, False)
        self.icon_image = PhotoImage(file="true.png")
        self.window.iconphoto(False, self.icon_image)

        self.score_label = Label(
            text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 30, "bold")
        )
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(
            150,
            125,
            text="Start the quiz!",
            width=280,
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR,
        )

        image_true = PhotoImage(file="true.png")
        image_false = PhotoImage(file="false.png")

        self.button_true = Button(
            image=image_true,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.true_pressed,
        )
        self.button_true.grid(row=2, column=0)
        self.button_false = Button(
            image=image_false,
            bg=THEME_COLOR,
            highlightthickness=0,
            command=self.false_pressed,
        )
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # when you type [self.quiz.next_question] to call the method (next_question) from the object (self.quiz), there
        # will be an error that the file doesn't know the datatype of the object (self.quiz)
        # to add the datatype of the object (self.quiz) --> in the init function ->[quiz_brain: QuizBrain]as an argument

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
            self.canvas.config(bg="white")
        else:
            self.canvas.itemconfig(self.question, text="You have finished the quiz.")
            self.canvas.config(bg="blue")
            # disable the true and false buttons, you can use the parameter (state) and give it the argument("disabled")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        if self.quiz.check_answer("True"):
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def false_pressed(self):
        if self.quiz.check_answer("False"):
            self.canvas.config(bg="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
