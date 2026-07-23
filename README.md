# Music Player

A simple Python-based MP3 player built with Pygame. It lets you choose a song from the Music folder and control playback using basic commands in the terminal.

## Features

- Play MP3 files from the Music folder
- Pause, resume, and stop playback
- Simple command-line interface
- Easy to run and customize

## What I learned

- How to work with Python functions and organize code into smaller reusable blocks
- How to use the os module to work with files and folders
- How to use Pygame for basic audio playback
- How to handle user input and create simple interactive programs

## Main Python concepts used

- `os.path.exists()` and `os.path.join()`
- `os.listdir()` to read files from a folder
- `input()` to take user commands
- Loops and conditionals for controlling the player

## Library used

- `pygame` for music playback

## How to run

1. Install the dependency:
   ```bash
   pip install pygame
   ```
2. Put your `.mp3` files inside the Music folder.
3. Run the program:
   ```bash
   python main.py
   ```

## Commands

- `P` → Pause
- `R` → Resume
- `S` → Stop
- `Q` → Quit
