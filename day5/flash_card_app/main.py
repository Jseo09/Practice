from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#b1ddc6"
FLIP_DELAY_MS = 3000
WORDS_TO_LEARN_PATH = "data/words_to_learn.csv"
SOURCE_WORDS_PATH = "data/french_words.csv"

window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = None
current_card = None

# --- Data loading (load once) ---
try:
    data = pd.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    data = pd.read_csv(SOURCE_WORDS_PATH)

words = data.to_dict(orient="records")


def pick_new_card():
    """Show a new French word and schedule flip to English."""
    global current_card, flip_timer

    if flip_timer is not None:
        window.after_cancel(flip_timer)

    if not words:
        canvas.itemconfig(title_text, text="Done!")
        canvas.itemconfig(word_text, text="All words learned 🎉")
        canvas.itemconfig(card_image, image=card_front_img)
        return

    current_card = random.choice(words)

    canvas.itemconfig(card_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French")
    canvas.itemconfig(word_text, text=current_card["French"])

    flip_timer = window.after(FLIP_DELAY_MS, flip_card)


def flip_card():
    """Flip the card to show English."""
    if current_card is None:
        return
    canvas.itemconfig(card_image, image=card_back_img)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_card["English"])


def mark_known():
    """Remove current word from list and save progress."""
    global current_card
    if current_card is None:
        return

    words.remove(current_card)
    pd.DataFrame(words).to_csv(WORDS_TO_LEARN_PATH, index=False)
    current_card = None
    pick_new_card()


# --- UI ---
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

card_image = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_img, highlightthickness=0, command=pick_new_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, command=mark_known)
right_button.grid(column=1, row=1)

pick_new_card()
window.mainloop()
