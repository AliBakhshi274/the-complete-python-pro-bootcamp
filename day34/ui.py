import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(text= "Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.text_on_canvas = self.canvas.create_text(150, 125, width=280, text='Some Text', font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=3, pady=50)

        false_image = tkinter.PhotoImage(file="images/false.png")
        self.false_btn = tkinter.Button(image=false_image, highlightthickness=0, command=lambda : self.check_answer("False"))
        self.false_btn.grid(row=2, column=2)

        true_image = tkinter.PhotoImage(file="images/true.png")
        self.true_btn = tkinter.Button(image=true_image, highlightthickness=0, command=lambda : self.check_answer("True"))
        self.true_btn.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.text_on_canvas, text=f"{self.quiz.next_question()}")
        else:
            self.true_btn.config(state=tkinter.DISABLED)
            self.false_btn.config(state=tkinter.DISABLED)

    def check_answer(self, user_answer):
        (score, is_correct) = self.quiz.check_answer(user_answer)
        self.score_label.config(text=f"Score: {score}")
        self.give_feedback(is_correct)
        # if self.quiz.still_has_questions():
        #     self.get_next_question()
        # else:
        #     self.true_btn.config(state=tkinter.DISABLED)
        #     self.false_btn.config(state=tkinter.DISABLED)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)















