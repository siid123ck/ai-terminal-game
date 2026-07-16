"""
Basic tests for the game grid.
"""

from game import GRID_SIZE, player_row, player_col


def test_grid_size_is_five() -> None:
    """Verify the grid is 5x5."""
    assert GRID_SIZE == 5


def test_player_starts_at_row_zero() -> None:
    """Player should start at row 0."""
    assert player_row == 0


def test_player_starts_at_col_zero() -> None:
    """Player should start at column 0."""
    assert player_col == 0
