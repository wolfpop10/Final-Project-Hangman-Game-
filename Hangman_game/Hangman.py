import os
import random
from tkinter import messagebox
import tkinter as tk




def main():
    # list of words for the game
    wordlist_path = os.path.join(os.path.dirname(__file__), "words.txt")

    with open(wordlist_path, "r", encoding="utf-8") as file:
        words = file.read().split()

    if not words:
        raise ValueError("words.txt is empty.")
    
    # create the root
    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("500x600")

    # initialize variables
    word_to_guess = random.choice(words).lower()
    guessed_letters = []
    MAX_ATTEMPTS = 6
    attempts = MAX_ATTEMPTS

    def check_win():    # Function to check if the player has won
        return all(letter in guessed_letters for letter in word_to_guess)

    def check_loss():  # Function to check if the player has lost 
        return attempts == 0

    def guess_letter(): # Function to handle a letter guess
        nonlocal attempts

        letter = letter_entry.get().lower().strip()

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showinfo("Hangman", "Please enter a single letter.")
            letter_entry.delete(0, tk.END)
            return

        if letter in guessed_letters:
            messagebox.showinfo("Hangman", f"You've already guessed '{letter}'")
        elif letter in word_to_guess:
            guessed_letters.append(letter)
            update_word_display()

            if check_win():
                messagebox.showinfo("Hangman", "Congratulations! You win!")
                reset_game()
        else:
            guessed_letters.append(letter)
            attempts -= 1
            update_attempts_display()
            draw_hangman()

            if check_loss():
                messagebox.showinfo("Hangman", f"You lose! The word was: {word_to_guess}")
                reset_game()

        letter_entry.delete(0, tk.END)

    def reset_game():   # Function that reset the game
        nonlocal word_to_guess, attempts

        word_to_guess = random.choice(words).lower()
        guessed_letters.clear()
        attempts = MAX_ATTEMPTS
        update_word_display()
        update_attempts_display()
        draw_hangman()
        letter_entry.delete(0, tk.END)

    def update_word_display():
        display_word = " ".join(letter if letter in guessed_letters else "_" for letter in word_to_guess)
        word_label.config(text=display_word)

    def update_attempts_display():
        attempts_label.config(text=f"Attempts left: {attempts}")

    def draw_hangman(): # Draw the fixed gallows
        canvas.delete("hangman")
        wrong_guesses = MAX_ATTEMPTS - attempts

        if wrong_guesses >= 1:
            canvas.create_oval(125, 125, 175, 175, width=4, tags="hangman")  # Head
        if wrong_guesses >= 2:
            canvas.create_line(150, 175, 150, 225, width=4, tags="hangman")  # Body
        if wrong_guesses >= 3:
            canvas.create_line(150, 200, 125, 175, width=4, tags="hangman")  # Left arm
        if wrong_guesses >= 4:
            canvas.create_line(150, 200, 175, 175, width=4, tags="hangman")  # Right arm
        if wrong_guesses >= 5:
            canvas.create_line(150, 225, 125, 250, width=4, tags="hangman")  # Left leg
        if wrong_guesses >= 6:
            canvas.create_line(150, 225, 175, 250, width=4, tags="hangman")  # Right leg

    word_label = tk.Label(root, text="", font=("Arial", 24))
    attempts_label = tk.Label(root, text="", font=("Arial", 16))
    letter_entry = tk.Entry(root, width=5, font=("Arial", 16))
    guess_button = tk.Button(root, text="Guess", command=guess_letter)
    reset_button = tk.Button(root, text="Reset", command=reset_game)
    canvas = tk.Canvas(root, width=300, height=300)

    canvas.create_line(50, 250, 250, 250, width=4)  # Base line
    canvas.create_line(200, 250, 200, 100, width=4)
    canvas.create_line(100, 100, 200, 100, width=4)
    canvas.create_line(150, 100, 150, 120, width=4)
    
    canvas.pack()   # Place the GUI elements in the window
    word_label.pack()
    attempts_label.pack()
    letter_entry.pack()
    guess_button.pack()
    reset_button.pack()

    update_word_display()
    update_attempts_display()
    draw_hangman()

    root.mainloop()


if __name__ == "__main__":  # Start the game only when this file is run directly
    main()
