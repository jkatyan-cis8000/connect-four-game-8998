# Game Module Design

## Overview

The `game.py` module implements the `Game` class that manages turn-based gameplay for Connect Four. It coordinates with the `Board` class to execute moves, track game state, and determine when the game ends.

## Architecture

### Game State

- **Board reference**: Holds reference to Board instance managing the grid
- **Current player**: Tracks whose turn it is (1 or 2)
- **Move result**: Standardized dictionary format returned by `play_turn()`

### Data Structures

```python
# Move result format
result = {
    "success": bool,    # Whether move was valid
    "row": int | None,  # Row where disc landed (None if invalid)
    "winner": int | None,  # Winning player (1 or 2) or None
    "draw": bool        # True if board is full with no winner
}
```

## Methods

### `__init__(board: Board)`

Initializes the game with:
- Reference to the Board instance
- `current_player` set to 1 (Player 1 starts)

### `play_turn(column: int) -> dict`

Executes a single turn:

1. **Validation**: Checks if column move is valid via `board.is_valid_move()`
2. **Move execution**: Applies move via `board.apply_move()`
3. **Win check**: Queries `board.check_winner()` for winner
4. **Draw check**: Queries `board.is_full()` for draw condition
5. **Return**: Dict with success status, row landed, winner, draw flag

**Returns**:
- `{"success": False, "row": None, "winner": None, "draw": False}` for invalid moves
- `{"success": True, "row": row, "winner": None, "draw": False}` for valid non-ending moves
- `{"success": True, "row": row, "winner": player, "draw": False}` for win
- `{"success": True, "row": row, "winner": None, "draw": True}` for draw

### `switch_player()`

Toggles current player between 1 and 2:
```python
self.current_player = 3 - self.current_player
```

### `get_current_player() -> int`

Returns the current player number (1 or 2).

### `game_over() -> bool`

Checks if game has ended:
- Returns `True` if winner exists OR board is full
- Returns `False` if game continues

## Flow

```
Game Start
    ↓
play_turn(column) → Validate → Apply Move
    ↓
Check Winner? → Yes → End Game (winner)
    ↓ No
Check Draw? → Yes → End Game (draw)
    ↓ No
switch_player() → Next Turn
```

## Constraints

- Uses only Python standard library
- Delegates grid state and win detection to Board class
- No input validation in Game class (only board validity checked)
- Player IDs must be 1 or 2 (enforced by caller)
- Turn alternation is manual via `switch_player()` (UI layer responsibility)

## Integration with UI

The UI layer handles:
- Displaying board state
- Getting column input from player
- Validating input range (1-7)
- Announcing results (winner/draw/invalid)

The Game class focuses solely on state management and move execution.
