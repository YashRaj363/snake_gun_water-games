# Snake Water Gun Game

A simple command-line implementation of the classic "Snake Water Gun" game, similar to "Rock Paper Scissors", written in Python.

## How to Play

- The game is played between a user and the computer.
- Each round, both the user and the computer choose one from: `snake`, `water`, or `gun`.
- The rules are:
    - **Snake drinks Water**: Snake wins.
    - **Water douses Gun**: Water wins.
    - **Gun kills Snake**: Gun wins.
    - If both select the same, it's a tie.

## Gameplay Instructions

1. Run the script:
    ```bash
    python game.py
    ```
2. Enter your choice when prompted: `snake`, `water`, or `gun`. Input is **case-sensitive**.
3. The computer will also choose randomly.
4. The winner for that round will be displayed.
5. After each round, you will be asked if you want to play again (`y` for yes, `n` for no).
6. After you choose not to play, a summary will be displayed showing:
    - Total games played
    - User wins
    - Computer wins
    - Number of ties
    - Overall winner

## Example Session

```
Enter your choice from Snake,Water,Gun: snake
Computer chose: water
User Wins
Do U want to play Again: (y or n)y
Enter your choice from Snake,Water,Gun: gun
Computer chose: snake
Computer Wins
Do U want to play Again: (y or n)n
==================Game Summary==================
Game Played: 2
User Wins: 1
Computer Wiins: 1
Game Tie: 0
Game Draw
===============================================
```

## Features

- Command-line interface for quick play.
- Tracks and displays game statistics.
- Can be played multiple rounds in one session.

## Code Overview

- Uses Python's `random` module for computer choice.
- Game logic is implemented with conditional statements to check all possible outcomes.
- Results are stored in a dictionary and displayed at the end.

## Requirements

- Python 3.x

## Customization

- You can easily change the choices or logic to expand the game.
- Improve input handling for case-insensitivity or invalid inputs.

## License

This project is open source and free to use.
