# Cyber Chase

A terminal-based grid adventure built with Python. You are a dragon navigating a 5x5 neon grid, hunting for lost coins while dodging deadly viruses. Collect all the coins to win — but step on a virus and it's game over.

## Features

- **WASD Movement** — Navigate the grid using `w` (up), `a` (left), `s` (down), and `d` (right)
- **Collectible Scoring** — Pick up coins to increase your score toward the win condition
- **Hazard Tiles** — Viruses spawn at random positions; stepping on one ends the game immediately
- **Win Condition** — Collect 10 coins to defeat the grid and win
- **Lose Condition** — Step on a virus and the grid reclaims your soul
- **Play Again** — After winning or losing, choose to play another round or quit
- **Randomised Spawning** — Coins and viruses respawn at random empty positions each round

## How to Run

### Start the Game

```bash
python game.py
```

Use `WASD` to move and `Q` to quit at any time.

### Run the Tests

```bash
pytest
```

To run with verbose output showing each test name:

```bash
pytest -v
```

## Project Structure

```
ai-terminal-game/
  game.py          # Core game logic and main loop
  test_game.py     # Pytest test suite
  README.md        # This file
```

## What I Learned

- **Iterative Development** — Building the game in small, testable chunks (grid, movement, collectibles, hazards) made each feature easy to reason about and verify before moving on to the next.
- **Engineering Prompts to Prevent Regression** — When adding new features like hazard tiles, it was important to think about how they interact with existing code (e.g., making sure hazards don't spawn on the player or collectibles). Writing clear requirements upfront prevented bugs from sneaking in.
- **Automated Testing with Pytest** — Automated tests caught edge cases I wouldn't have thought to check manually, like boundary collisions and spawn overlaps. Running `pytest` after every change gave confidence that nothing broke along the way.

## License

This project was built as a learning exercise.
