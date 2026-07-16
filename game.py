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

# Score
score = 0


def spawn_collectible() -> None:
    """Place the collectible at a random position that is not the player."""
    global collect_row, collect_col

    while True:
        collect_row = random.randint(0, GRID_SIZE - 1)
        collect_col = random.randint(0, GRID_SIZE - 1)
        if collect_row != player_row or collect_col != player_col:
            break


def draw_grid() -> None:
    """Draw the grid with the player marked as @ and collectible as $."""
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
            else:
                row_str += ". "
        print(f"{row} {row_str}")


def move(direction: str) -> bool:
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


def main() -> None:
    """Main game loop."""
    print("Welcome! You are @ on the grid.")
    print("Collect all the $ to win!")

    # Spawn the first collectible
    spawn_collectible()

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
            print("Thanks for playing!")
            break
        elif command in ("w", "a", "s", "d"):
            move(command)
            check_collect()

            if score == WIN_SCORE:
                os.system("clear")
                draw_grid()
                print()
                print(f"Score: {score} / {WIN_SCORE}")
                print()
                print("You win! All collectibles gathered!")
                break


if __name__ == "__main__":
    main()
