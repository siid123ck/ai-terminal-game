"""
Tests for the game grid and movement.
"""

import game
from game import GRID_SIZE, move


def reset_player() -> None:
    """Reset player to starting position."""
    game.player_row = 0
    game.player_col = 0


def test_grid_size_is_five() -> None:
    """Verify the grid is 5x5."""
    assert GRID_SIZE == 5


def test_player_starts_at_row_zero() -> None:
    """Player should start at row 0."""
    reset_player()
    assert game.player_row == 0


def test_player_starts_at_col_zero() -> None:
    """Player should start at column 0."""
    reset_player()
    assert game.player_col == 0


def test_move_right() -> None:
    """Pressing d should move the player one column to the right."""
    reset_player()
    move("d")
    assert game.player_col == 1


def test_move_left() -> None:
    """Pressing a should move the player one column to the left."""
    reset_player()
    game.player_col = 2
    move("a")
    assert game.player_col == 1


def test_move_down() -> None:
    """Pressing s should move the player one row down."""
    reset_player()
    move("s")
    assert game.player_row == 1


def test_move_up() -> None:
    """Pressing w should move the player one row up."""
    reset_player()
    game.player_row = 2
    move("w")
    assert game.player_row == 1


def test_cannot_move_above_top_edge() -> None:
    """Player should not move above row 0."""
    reset_player()
    move("w")
    assert game.player_row == 0


def test_cannot_move_below_bottom_edge() -> None:
    """Player should not move below the last row."""
    reset_player()
    game.player_row = GRID_SIZE - 1
    move("s")
    assert game.player_row == GRID_SIZE - 1


def test_cannot_move_left_of_left_edge() -> None:
    """Player should not move left of column 0."""
    reset_player()
    move("a")
    assert game.player_col == 0


def test_cannot_move_right_of_right_edge() -> None:
    """Player should not move right of the last column."""
    reset_player()
    game.player_col = GRID_SIZE - 1
    move("d")
    assert game.player_col == GRID_SIZE - 1
