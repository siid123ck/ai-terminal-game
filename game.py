"""
A basic text-based game with a 5x5 grid.
"""

import os

# Grid size
GRID_SIZE = 5

# Player starting position (row, column)
player_row = 0
player_col = 0


def draw_grid() -> None:
    """Draw the grid with the player marked as @."""
    # Print column numbers
    print("  " + " ".join(str(i) for i in range(GRID_SIZE)))

    # Print each row
    for row in range(GRID_SIZE):
        row_str = ""
        for col in range(GRID_SIZE):
            if row == player_row and col == player_col:
                row_str += "@ "
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


def main() -> None:
    """Main game loop."""
    print("Welcome! You are @ on the grid.")

    while True:
        # Clear the screen
        os.system("clear")

        draw_grid()
        print()
        print("WASD to move, Q to quit")

        # Wait for user input
        command = input(">> ")

        if command == "q":
            print("Thanks for playing!")
            break
        elif command in ("w", "a", "s", "d"):
            move(command)


if __name__ == "__main__":
    main()
