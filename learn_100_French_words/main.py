from tkinter import *
import pandas as pd
import random
import os

BACKGROUND_COLOR = "#B1DDC6"

# -------------------------PANDAS-------------------------#

to_learn = {}

try:
    pd_data = pd.read_csv("learn_100_French_words/data/french_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("learn_100_French_words/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = pd_data.to_dict(orient="records")

# -------------------------RANDOM CHOICE-------------------------#
random_word = {}


def random_choice():
    global random_word, flip_timer
    if len(to_learn) == 0:
        right_button.grid_forget()
        wrong_button.grid_forget()
        canvas.itemconfig(language_text, text="Congratulations!", fill="black")
        canvas.itemconfig(words_text, text="You learned all the words!", fill="black")
        canvas.itemconfig(words_to_learn, text="😁😁😁😁😁😁😁😁")
        window.after_cancel(flip_timer)
        if os.path.exists("learn_100_French_words/data/words_to_learn.csv"):
            os.remove("learn_100_French_words/data/words_to_learn.csv")
        window.after(10000, window.quit)

    else:
        window.after_cancel(flip_timer)
        random_word = random.choice(to_learn)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(words_text, text=random_word["French"], fill="black")
        canvas.itemconfig(can_image, image=fr_image)
        canvas.itemconfig(words_to_learn, text=f"{len(to_learn)} other words to go")
        flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global random_word
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(words_text, text=random_word["English"], fill="white")
    canvas.itemconfig(can_image, image=eng_image)


def known_word():
    to_learn.remove(random_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("learn_100_French_words/data/words_to_learn.csv", index=False)
    random_choice()


# -------------------------UI-------------------------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
fr_image = PhotoImage(file="learn_100_French_words/images/card_front.png")
eng_image = PhotoImage(file="learn_100_French_words/images/card_back.png")
can_image = canvas.create_image(400, 263, image=fr_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
words_to_learn = canvas.create_text(400, 30, text=f"{len(to_learn)} other words to go", font=("Ariel", 20, "italic"),
                                    fill="blue")
language_text = canvas.create_text(400, 180, text="French", font=("Ariel", 40, "italic"), fill="black")
words_text = canvas.create_text(400, 285, text="Text", font=("Ariel", 60, "bold"), fill="black")

right_button_image = PhotoImage(
    file="learn_100_French_words/images/right.png")
right_button = Button(image=right_button_image, highlightthickness=0, command=known_word)
right_button.grid(column=0, row=1)

wrong_button_image = PhotoImage(
    file="learn_100_French_words/images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=random_choice)
wrong_button.grid(column=1, row=1)

random_choice()

window.mainloop()
