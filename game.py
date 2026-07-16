"""
A basic text-based game with a 5x5 grid.
"""

import os
import random

# Grid size
GRID_SIZE = 5

# Win condition
WIN_SCORE = 10

# Player starting position (row, column)
player_row = 0
player_col = 0

# Collectible position (row, column)
collect_row = 0
collect_col = 0

# Hazard position (row, column)
hazard_row = 0
hazard_col = 0

# Score
score = 0


def reset_game() -> None:
    """Reset all game state to defaults."""
    global player_row, player_col, score
    player_row = 0
    player_col = 0
    score = 0
    spawn_collectible()
    spawn_hazard()


def spawn_collectible() -> None:
    """Place the collectible at a random position that is not the player."""
    global collect_row, collect_col

    while True:
        collect_row = random.randint(0, GRID_SIZE - 1)
        collect_col = random.randint(0, GRID_SIZE - 1)
        if (collect_row, collect_col) != (player_row, player_col):
            break


def spawn_hazard() -> None:
    """Place the hazard at a random position that is not the player or collectible."""
    global hazard_row, hazard_col

    while True:
        hazard_row = random.randint(0, GRID_SIZE - 1)
        hazard_col = random.randint(0, GRID_SIZE - 1)
        if (hazard_row, hazard_col) != (player_row, player_col) and \
           (hazard_row, hazard_col) != (collect_row, collect_col):
            break


def draw_grid() -> None:
    """Draw the grid with the player, collectible, and hazard."""
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))

    # Print each row
    for row in range(GRID_SIZE):
        row_str = ""
        for col in range(GRID_SIZE):
            if row == player_row and col == player_col:
                row_str += "@ "
            elif row == collect_row and col == collect_col:
                row_str += "$ "
            elif row == hazard_row and col == hazard_col:
                row_str += "X "
            else:
                row_str += ". "
        print(f"{row} {row_str}")


def move(direction: str) -> None:
    """Move the player in the given direction, if within bounds."""
    global player_row, player_col

    if direction == "w" and player_row > 0:
        player_row -= 1
    elif direction == "s" and player_row < GRID_SIZE - 1:
        player_row += 1
    elif direction == "a" and player_col > 0:
        player_col -= 1
    elif direction == "d" and player_col < GRID_SIZE - 1:
        player_col += 1


def check_collect() -> None:
    """Check if the player is on the collectible and handle scoring."""
    global score

    if player_row == collect_row and player_col == collect_col:
        score += 1
        spawn_collectible()


def check_hazard() -> bool:
    """Check if the player is on the hazard."""
    return player_row == hazard_row and player_col == hazard_col


def play_round() -> str | None:
    """Run a single round of the game. Returns 'win', 'lose', or None (quit)."""
    reset_game()

    while True:
        # Clear the screen
        os.system("clear")

        draw_grid()
        print()
        print(f"Score: {score} / {WIN_SCORE}")
        print()
        print("WASD to move, Q to quit")

        # Wait for user input
        command = input(">> ")

        if command == "q":
            return None
        elif command in ("w", "a", "s", "d"):
            move(command)

            if check_hazard():
                os.system("clear")
                draw_grid()
                print()
                print("Game Over!")
                return "lose"

            check_collect()

            if score == WIN_SCORE:
                os.system("clear")
                draw_grid()
                print()
                print(f"Score: {score} / {WIN_SCORE}")
                print()
                print("You win! All collectibles gathered!")
                return "win"


def main() -> None:
    """Main game loop with play again support."""
    print("Welcome! You are @ on the grid.")
    print("Collect all the $ to win! Avoid the X hazards!")
    print()

    while True:
        result = play_round()

        if result is None:
            print("Thanks for playing!")
            break

        # Ask to play again
        print()
        answer = input("Play again? (y/n) ")

        if answer != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
