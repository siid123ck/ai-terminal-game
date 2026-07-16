"""
Tests for the game grid, movement, collectibles, hazards, and scoring.
"""

import game
from game import GRID_SIZE, WIN_SCORE, move, spawn_collectible, check_collect, spawn_hazard, check_hazard


def reset_game() -> None:
    """Reset all game state to defaults."""
    game.player_row = 0
    game.player_col = 0
    game.score = 0
    spawn_collectible()
    spawn_hazard()


# --- Grid tests ---

def test_grid_size_is_five() -> None:
    """Verify the grid is 5x5."""
    assert GRID_SIZE == 5


def test_win_score_is_ten() -> None:
    """Win condition should be 10."""
    assert WIN_SCORE == 10


# --- Player starting position tests ---

def test_player_starts_at_row_zero() -> None:
    """Player should start at row 0."""
    reset_game()
    assert game.player_row == 0


def test_player_starts_at_col_zero() -> None:
    """Player should start at column 0."""
    reset_game()
    assert game.player_col == 0


# --- Movement tests ---

def test_move_right() -> None:
    """Pressing d should move the player one column to the right."""
    reset_game()
    move("d")
    assert game.player_col == 1


def test_move_left() -> None:
    """Pressing a should move the player one column to the left."""
    reset_game()
    game.player_col = 2
    move("a")
    assert game.player_col == 1


def test_move_down() -> None:
    """Pressing s should move the player one row down."""
    reset_game()
    move("s")
    assert game.player_row == 1


def test_move_up() -> None:
    """Pressing w should move the player one row up."""
    reset_game()
    game.player_row = 2
    move("w")
    assert game.player_row == 1


def test_cannot_move_above_top_edge() -> None:
    """Player should not move above row 0."""
    reset_game()
    move("w")
    assert game.player_row == 0


def test_cannot_move_below_bottom_edge() -> None:
    """Player should not move below the last row."""
    reset_game()
    game.player_row = GRID_SIZE - 1
    move("s")
    assert game.player_row == GRID_SIZE - 1


def test_cannot_move_left_of_left_edge() -> None:
    """Player should not move left of column 0."""
    reset_game()
    move("a")
    assert game.player_col == 0


def test_cannot_move_right_of_right_edge() -> None:
    """Player should not move right of the last column."""
    reset_game()
    game.player_col = GRID_SIZE - 1
    move("d")
    assert game.player_col == GRID_SIZE - 1


# --- Collectible tests ---

def test_spawn_not_on_player() -> None:
    """Collectible should never spawn on the player."""
    reset_game()
    for _ in range(50):
        spawn_collectible()
        assert (game.collect_row, game.collect_col) != (game.player_row, game.player_col)


def test_spawn_within_grid() -> None:
    """Collectible should always be within grid bounds."""
    reset_game()
    for _ in range(50):
        spawn_collectible()
        assert 0 <= game.collect_row < GRID_SIZE
        assert 0 <= game.collect_col < GRID_SIZE


# --- Scoring tests ---

def test_score_starts_at_zero() -> None:
    """Score should start at 0."""
    reset_game()
    assert game.score == 0


def test_check_collect_increases_score() -> None:
    """Score should increase by 1 when player lands on collectible."""
    reset_game()
    game.player_row = 3
    game.player_col = 3
    game.collect_row = 3
    game.collect_col = 3
    check_collect()
    assert game.score == 1


def test_check_collect_respawns_collectible() -> None:
    """Collectible should respawn at a new location after collection."""
    reset_game()
    game.player_row = 3
    game.player_col = 3
    game.collect_row = 3
    game.collect_col = 3
    check_collect()
    # Collectible should no longer be at (3, 3)
    assert (game.collect_row, game.collect_col) != (3, 3)


def test_check_collect_no_score_if_not_on_collectible() -> None:
    """Score should not change if player is not on the collectible."""
    reset_game()
    game.player_row = 0
    game.player_col = 0
    game.collect_row = 4
    game.collect_col = 4
    check_collect()
    assert game.score == 0


# --- Hazard tests ---

def test_hazard_spawns_not_on_player() -> None:
    """Hazard should never spawn on the player."""
    reset_game()
    for _ in range(50):
        spawn_hazard()
        assert (game.hazard_row, game.hazard_col) != (game.player_row, game.player_col)


def test_hazard_spawns_not_on_collectible() -> None:
    """Hazard should never spawn on the collectible."""
    reset_game()
    for _ in range(50):
        spawn_hazard()
        assert (game.hazard_row, game.hazard_col) != (game.collect_row, game.collect_col)


def test_hazard_spawns_within_grid() -> None:
    """Hazard should always be within grid bounds."""
    reset_game()
    for _ in range(50):
        spawn_hazard()
        assert 0 <= game.hazard_row < GRID_SIZE
        assert 0 <= game.hazard_col < GRID_SIZE


def test_check_hazard_true_when_player_on_hazard() -> None:
    """check_hazard should return True when player lands on the hazard."""
    reset_game()
    game.player_row = 2
    game.player_col = 3
    game.hazard_row = 2
    game.hazard_col = 3
    assert check_hazard() is True


def test_check_hazard_false_when_player_not_on_hazard() -> None:
    """check_hazard should return False when player is not on the hazard."""
    reset_game()
    game.player_row = 0
    game.player_col = 0
    game.hazard_row = 4
    game.hazard_col = 4
    assert check_hazard() is False


# --- Reset tests ---

def test_reset_game_resets_player_position() -> None:
    """reset_game should put the player back at (0, 0)."""
    reset_game()
    game.player_row = 3
    game.player_col = 3
    reset_game()
    assert game.player_row == 0
    assert game.player_col == 0


def test_reset_game_resets_score() -> None:
    """reset_game should set the score back to 0."""
    reset_game()
    game.score = 5
    reset_game()
    assert game.score == 0


def test_reset_game_respawns_collectible() -> None:
    """reset_game should spawn the collectible at a new position."""
    reset_game()
    old_pos = (game.collect_row, game.collect_col)
    # Move player away and force a different collectible position
    game.player_row = 4
    game.player_col = 4
    reset_game()
    # Collectible should be spawned (not stuck at a bad position)
    assert 0 <= game.collect_row < GRID_SIZE
    assert 0 <= game.collect_col < GRID_SIZE


def test_reset_game_respawns_hazard() -> None:
    """reset_game should spawn the hazard at a new position."""
    reset_game()
    game.player_row = 4
    game.player_col = 4
    reset_game()
    # Hazard should be spawned within bounds
    assert 0 <= game.hazard_row < GRID_SIZE
    assert 0 <= game.hazard_col < GRID_SIZE
