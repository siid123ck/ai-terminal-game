"""
A basic text-based game with a 5x5 grid.
"""

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


def main() -> None:
    """Main game loop."""
    print("Welcome! You are @ on the grid.")

    while True:
        print()
        draw_grid()
        print()

        # Wait for user input
        command = input("Enter 'q' to quit: ")

        if command == "q":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
