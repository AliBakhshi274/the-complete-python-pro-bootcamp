import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
DEUTSCH = "Deutsch"
ENGLISH = "English"
current_word = {}
#-------------------------------------- CSV --------------------------------------#
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("deutsch_words.csv")
data_list = pandas.DataFrame(data).to_dict(orient="records")

#------------------------------------ Functions ----------------------------------#
def is_known():
    data_list.remove(current_word)
    print(len(data_list))
    next_card()
    d = pandas.DataFrame(data_list)
    d.to_csv("words_to_learn.csv")

def next_card():
    global current_word
    current_word = random.choice(data_list)
    front_card(current_word.get(DEUTSCH))
    window.after(3000, back_card, current_word.get(ENGLISH))

def front_card(word):
    disable_buttons()
    canvas.itemconfig(image_on_canvas, image=card_front_image)
    canvas.itemconfig(title_text, text=DEUTSCH)
    canvas.itemconfig(word_text, text=word)

def back_card(word):
    canvas.itemconfig(image_on_canvas, image=card_back_image)
    canvas.itemconfig(title_text, text=ENGLISH)
    canvas.itemconfig(word_text, text=word)
    enable_buttons()

def disable_buttons():
    wrong_button.config(state=tkinter.DISABLED)
    right_button.config(state=tkinter.DISABLED)
def enable_buttons():
    wrong_button.config(state=tkinter.NORMAL)
    right_button.config(state=tkinter.NORMAL)

#------------------------------------ Graphical Design ---------------------------#
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=600, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file="card_front.png")
card_back_image = tkinter.PhotoImage(file="card_back.png")
image_on_canvas = canvas.create_image(400, 300, image=card_front_image)
title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

wrong_image = tkinter.PhotoImage(file="wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = tkinter.PhotoImage(file="right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=2, row=1)

next_card()


























tkinter.mainloop()