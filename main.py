from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import random

class FlashcardApp:
    def __init__(self):
        self.window = Tk()
        self.window.title("Flashcard Game")
        self.window.config(padx=50, pady=50, bg="#B1DDC6")

        self.df = pd.read_csv("data/french_words.csv")
        self.words = self.df.to_dict(orient="records")
        self.known_words = []
        self.current_word = None

        # Load images
        self.card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.png").resize((800, 526)))
        self.card_back_img = ImageTk.PhotoImage(Image.open("images/card_back.png").resize((800, 526)))
        self.right_img = ImageTk.PhotoImage(Image.open("images/right.png").resize((100, 100)))
        self.wrong_img = ImageTk.PhotoImage(Image.open("images/wrong.png").resize((100, 100)))

        # Create canvas
        self.canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
        self.canvas.grid(row=0, column=0, columnspan=2, pady=50)

        # Create buttons
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.flip_card, bd=0)
        self.wrong_button.grid(row=1, column=0)
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.next_card, bd=0)
        self.right_button.grid(row=1, column=1)

        self.next_card()

    def next_card(self):
        """Show the next card."""
        if len(self.known_words) == len(self.words):
            self.canvas.itemconfig(self.card_title, text="Done!", fill="black")
            self.canvas.itemconfig(self.card_word, text="All words learned!", fill="black")
            self.canvas.itemconfig(self.card_background, image=self.card_front_img)
            return

        while True:
            self.current_word = random.choice(self.words)
            if self.current_word not in self.known_words:
                break

        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(self.card_word, text=self.current_word["French"], fill="black")
        self.known_words.append(self.current_word)

    def flip_card(self):
        """Flip the current card."""
        if self.current_word:
            self.canvas.itemconfig(self.card_background, image=self.card_back_img)
            self.canvas.itemconfig(self.card_title, text="English", fill="white")
            self.canvas.itemconfig(self.card_word, text=self.current_word["English"], fill="white")

    def run(self):
        self.window.mainloop()

# Run the app
app = FlashcardApp()
app.run()
