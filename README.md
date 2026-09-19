# Hangman Game

A desktop Hangman game written in **Python** with a **Tkinter** graphical interface. The computer picks a secret word, and the player tries to guess it one letter at a time before the hangman is fully drawn.

---

## Features

- Graphical window built with Tkinter (labels, entry box, buttons, canvas)
- Random secret word chosen from a text file each round
- The hangman is drawn on a canvas, one body part per wrong guess
- Input validation (single letters only, no repeated guesses)
- Pop-up messages for win, loss and invalid input
- Reset button and automatic reset after each round

---

## Requirements

- Python 3.8 or newer
- Tkinter (included with the standard Python installer on Windows and macOS; on some Linux systems install it with `sudo apt install python3-tk`)

No external packages are needed.

---

## Project Structure

```
hangman/
├── hangman.py    # the game (rename to match your file name)
├── words.txt     # list of words the game picks from
└── README.md
```

`words.txt` **must be in the same folder as the Python file**, otherwise the game will not start.

### Format of `words.txt`

Words separated by spaces or new lines, letters only, for example:

```
python
computer
keyboard
network
```

Use plain letters (no spaces, hyphens or numbers inside a word), because the game only accepts letters as guesses.

---

## How to Run

1. Put `hangman.py` and `words.txt` in the same folder.
2. Open a terminal in that folder.
3. Run:

```bash
python hangman.py
```

(On some systems use `python3 hangman.py`.)

---

## How to Play

1. The game shows the secret word as blanks, for example `_ _ _ _ _ _`.
2. Type **one letter** in the box and click **Guess**.
3. If the letter is in the word, it appears in every matching position.
4. If it is not, you lose one attempt and a new body part is drawn.
5. You **win** when all the letters are revealed.
6. You **lose** after **6 wrong guesses**, and the word is revealed.
7. Click **Reset** at any time to start a new round with a new word.

| Wrong guesses | Body part drawn |
|:---:|---|
| 1 | Head |
| 2 | Body |
| 3 | Left arm |
| 4 | Right arm |
| 5 | Left leg |
| 6 | Right leg (game over) |

The game also warns you if you enter something that is not a single letter, or a letter you already tried.

---

## How the Code Works

Everything lives inside the `main()` function, and the game starts only when the file is run directly (`if __name__ == "__main__"`).

### Setup

1. **Load the words:** `words.txt` is opened with `with open(...)`, and `read().split()` turns its content into a list. If the list is empty, a `ValueError` is raised.
2. **Create the window:** a Tkinter root window (500x600) is created.
3. **Game state variables:**

| Variable | Type | Purpose |
|---|---|---|
| `word_to_guess` | string | The secret word (lowercase), chosen with `random.choice()` |
| `guessed_letters` | list | All letters the player has tried |
| `MAX_ATTEMPTS` | constant (6) | Maximum number of wrong guesses |
| `attempts` | integer | Wrong guesses left |

4. **Widgets:** a word label, an attempts label, an entry box, **Guess** and **Reset** buttons, and a canvas. The gallows is drawn once on the canvas at the start.

### Functions

| Function | What it does |
|---|---|
| `check_win()` | Returns `True` if every letter of the word is in `guessed_letters` (uses `all()`) |
| `check_loss()` | Returns `True` when `attempts == 0` |
| `guess_letter()` | Reads and validates the input, then handles a correct or wrong guess, and checks for win/loss |
| `reset_game()` | Picks a new word, clears guessed letters, restores attempts, refreshes the screen |
| `update_word_display()` | Rebuilds the text such as `_ a _ _`: shows guessed letters and `_` for the rest |
| `update_attempts_display()` | Updates the "Attempts left" label |
| `draw_hangman()` | Clears the old drawing and draws body parts according to the number of wrong guesses |

### Flow of `guess_letter()`

1. Read the letter with `get()`, then apply `lower()` and `strip()`.
2. If it is not a single letter, show a warning and stop.
3. If it was already guessed, show a message.
4. If it is in the word, add it to the list, update the display, and check for a win.
5. Otherwise, add it to the list, subtract one attempt, update the label, draw the next body part, and check for a loss.
6. Clear the entry box.

`nonlocal` is used inside the nested functions so they can change variables that belong to `main()`.

---

## Python Concepts Used

- Variables, constants, strings, lists
- Functions and nested functions (`nonlocal`)
- Conditions: `if / elif / else`
- Loops and generator expressions (`all(...)`)
- File handling (`open`, `read`)
- Exception handling (`raise ValueError`)
- Random selection (`random.choice`)
- GUI programming and events (Tkinter widgets, button `command=`, `mainloop()`)

---

## Possible Improvements

- Word categories and difficulty levels
- Score system with a saved high score (JSON file)
- Press **Enter** to submit a guess
- Show the list of wrong letters already used
- Hints

---

## Author

Made by Gasser as a Python course project.

