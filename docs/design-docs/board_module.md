# Board Module Design

## Overview

The `board.py` module implements the `Board` class that manages the Connect Four game state. The board is a 7×6 grid where players drop discs that fall to the lowest available row in the selected column.

## Architecture

### Grid Structure

- **Dimensions**: 6 rows × 7 columns
- **Row indexing**: Row 0 is top, Row 5 is bottom
- **Column indexing**: Columns 0-6 (left to right)
- **Cell values**: 0 = empty, 1 = Player 1 disc, 2 = Player 2 disc

```python
self._grid = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
```

## Methods

### `__init__()`
Initializes the empty 7×6 grid. All cells start at 0 (empty).

### `is_valid_move(column: int) -> bool`
Returns `True` if the column has space (top cell is empty) and the column index is valid (0-6). Returns `False` otherwise.

### `get_next_open_row(column: int) -> int | None`
Scans from bottom (row 5) to top (row 0) to find the first empty cell in the specified column. Returns the row index or `None` if column is full or invalid.

### `apply_move(column: int, player: int) -> bool`
1. Validates the move using `is_valid_move()`
2. Gets the open row using `get_next_open_row()`
3. Places the player's disc (1 or 2) in that position
4. Returns `True` on success, `False` if move is invalid

### `check_winner() -> int | None`
Checks for four consecutive discs in any direction:
- **Horizontal**: Same row, adjacent columns
- **Vertical**: Same column, adjacent rows
- **Diagonal down-right**: Row+1, Col+1
- **Diagonal down-left**: Row+1, Col-1

For each non-empty cell, checks all four directions. Returns the winning player (1 or 2) or `None` if no winner.

### `is_full() -> bool`
Returns `True` if the top row (row 0) has no empty cells, indicating the board is completely filled.

### `get_board_state() -> list[list[int]]`
Returns a deep copy of the grid to prevent external modification of internal state.

## Win Detection Algorithm

The `_check_line()` helper method verifies 4 consecutive cells in a given direction:

```python
def _check_line(self, row, col, dr, dc, player):
    for i in range(4):
        r, c = row + i * dr, col + i * dc
        if r < 0 or r >= self._rows or c < 0 or c >= self._cols:
            return False
        if self._grid[r][c] != player:
            return False
    return True
```

This ensures boundary checks and value matching for all 4 positions.

## Constraints

- Uses only Python standard library (no external dependencies)
- Grid dimensions are fixed (7×6) per Connect Four rules
- Column-based insertion ( discs fall to lowest empty row )
- No player validation in `apply_move()` - caller must ensure valid player ID (1 or 2)
