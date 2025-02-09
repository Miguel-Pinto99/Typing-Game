# Typing-Game
## Description
Typing-Game is a fun and interactive game designed to improve your typing speed and accuracy. Challenge yourself and see how fast you can type!

## Features
- Multiple difficulty levels
- Real-time typing feedback
- Score tracking

## Pre-commit Hook Setup
To ensure code quality and consistency, we use pre-commit hooks. Follow these steps to set them up:

1. Install pre-commit:
    ```bash
    pip install pre-commit
    ```
2. Navigate to the project directory and install the hooks:
    ```bash
    pre-commit install
    ```
3. Run the hooks on all files:
    ```bash
    pre-commit run --all-files
    ```

## UV Python Integration
This project uses UV for running the application. Make sure you have UV installed:

1. Install UV:
    ```bash
    pip install uv
    ```

## Installation
1. Clone the repository:

2. Navigate to the project directory:
    ```bash
    cd Typing-Game
    ```
3. To start the app, use:
    ```bash
    uvx reflex run
    ```

## Usage
1. Enter the number of letters you want to type.
2. Enter the duration for the game (in seconds).
3. Click 'Start Game' to begin.
4. Type the displayed word as quickly and accurately as possible.
5. The game will end when the time is up.
6. Your performance will be displayed at the end of the game.
