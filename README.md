# Hangman Game

A classic Hangman game built with Python and Pygame. This project showcases a simple word-guessing game where players try to guess a hidden word within a limited number of attempts.

## Features
- **Random Word Selection:** Picks a random word from a `words.txt` file.
- **Visual Hangman Drawing:** Displays a progressively detailed hangman drawing for each incorrect guess.
- **Sound Effects:** Includes sound effects for correct guesses, wrong guesses, game wins, and game over.
- **Interactive Menu:** Features a start screen with a button to begin the game.
- **Dynamic UI:** Shows the current state of the game, including the guessed word, remaining tries, and hangman drawing.

## Requirements
- **Python 3.x**
- **Pygame:** Install via `pip install pygame`
- **Assets:**
  - **Sound Files:** `correct.mp3`, `wrong.mp3`, `gameOver.mp3`, `win.mp3`, `start.mp3`
  - **Images:** `home.png`, `start.png`, `game.png`, `won.png`, `gameOver.png`
  - **Words File:** `words.txt` containing one word per line

## Setup
1. **Install Pygame:** Run `pip install pygame` in your terminal or command prompt.
2. **Add Assets:**
   - Place the sound files in the same directory as the script.
   - Place the images in the same directory as the script.
3. **Prepare Words File:** Ensure `words.txt` is present in the same directory as the script, with each line containing a single word.

## How to Play
1. **Start the Game:** Click the start button on the menu screen to begin.
2. **Guess Letters:** Click on the letter buttons to make guesses. Correctly guessed letters will appear in the word, while incorrect guesses will contribute to the drawing of the hangman.
3. **Winning and Losing:** You win by guessing all the letters in the word before running out of tries. You lose if the hangman drawing is completed before you guess the word.

## Running the Game
Execute the script with Python to start playing!
