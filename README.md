# Galaxians Python

A classic arcade-style space shooter game built with Python and Pygame. Defend the galaxy against waves of alien invaders!

## Features

- **Classic Gameplay**: Familiar arcade mechanics with smooth controls.
- **Enemy AI**: Formations, diving attacks, and random shooting patterns.
- **Scoring System**: Earn points for destroying enemies.
- **Progressive Difficulty**: Enemies attack more aggressively as you play.
- **Assets**: Custom sprites for player and enemies (with fallback placeholders).

## Requirements

- Python 3.x
- Pygame

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/ogaldos/galaxians.git
    cd galaxians
    ```

2.  Install the required dependencies:
    ```bash
    pip install pygame
    ```

## How to Play

Run the game using Python:

```bash
python main.py
```

### Controls

- **Left Arrow**: Move Left
- **Right Arrow**: Move Right
- **Space**: Shoot
- **R**: Restart Game (when Game Over)

## Project Structure

- `main.py`: Entry point of the game, handles the game loop and initialization.
- `game.py`: Core game logic, managing entities, collisions, and states.
- `player.py`: Player class handling movement and shooting.
- `enemy.py`: Enemy class defining behaviors like diving and formation movement.
- `bullet.py`: Projectile logic for both player and enemies.
- `utils.py`: Utility functions (e.g., image processing).

## License

This project is open source.
