# Tic Tac Toe Game (Player vs Computer)

Welcome to the classic **Tic Tac Toe** game where you can play against a computer! The board is a 3x3 grid, and you need to place your mark (either X or O) to form a line horizontally, vertically, or diagonally.

## Features:
- **Player vs Computer**: You will play against the computer, which makes random moves.
- **Classic 3x3 Grid**: A simple grid layout based on the positions of the number pad (1-9).
- **Interactive Gameplay**: Enter the position (1-9) to place your mark and enjoy the game.

## How to Play:
1. **Start the Game**: You will be prompted to enter your name and choose whether you want to be X or O.
2. **Game Mechanics**: 
   - The game alternates between the player and the computer, starting with either the player or the computer based on a random selection.
   - The player selects a position on the grid (1-9) to place their mark.
   - The computer will select a random position for its move.
3. **Winning Condition**: The first player (or computer) to line up three marks horizontally, vertically, or diagonally wins the game. If the grid fills up without a winner, the game ends in a draw.
4. **Replay Option**: After each game, you can choose to play again or exit.

## Installation:
This game is written in Python, so you need Python 3.x installed to play.

## 1. Clone the repository:
   git clone https://github.com/your-username/tic-tac-toe.git
   cd tic-tac-toe
Run the game:
python tic_tac_toe.py
How to Play:
The game will prompt for your name and whether you want to play as X or O.
The game will show the board in the following format:
markdown
Copy
Edit
7 | 8 | 9
-----------
4 | 5 | 6
-----------
1 | 2 | 3
You enter a number between 1-9 to select your move.
The computer will randomly pick an available spot for its move.
The game will display the updated board after each turn and announce the winner if there is one or declare a draw if the board fills up.
