# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/board.py: 7x6 grid state, column-based move validation, disc drop simulation, win detection for horizontal/vertical/diagonal lines of 4 (**implemented**)
- src/game.py: turn management (Player 1/Player 2), game state tracking, input validation, game loop coordination (**implemented**)
- src/ui.py: terminal rendering of board, column selection input (1-7), move feedback, win/draw announcements (**implemented**)
- tests/test_game.py: unit tests for board operations, move validation, win detection (**implemented**)
- main.py: entry point that wires together board, game, and UI components (**implemented**)

## Interfaces

### board.py
- Board class:
  - `__init__()`: initialize 7x6 empty grid (0 = empty, 1 = Player 1, 2 = Player 2)
  - `is_valid_move(column: int) -> bool`: check if column has space
  - `get_next_open_row(column: int) -> int | None`: return lowest empty row in column
  - `apply_move(column: int, player: int) -> bool`: place disc, return success
  - `check_winner() -> int | None`: return winning player (1 or 2) or None
  - `is_full() -> bool`: check if board is completely filled
  - `get_board_state() -> list[list[int]]`: return copy of grid

### game.py
- Game class:
  - `__init__(board: Board)`: initialize with board, current_player=1
  - `play_turn(column: int) -> dict`: execute move, return result with keys: success, row, winner (int|None), draw (bool)
  - `switch_player()`: toggle current_player between 1 and 2
  - `get_current_player() -> int`: return current player number
  - `game_over() -> bool`: check if game ended (win or draw)

### ui.py
- UI class:
  - `display_board(board_state: list[list[int]]) -> None`: print 7x6 grid to terminal
  - `get_column_input() -> int`: prompt "Player X, choose column (1-7): ", validate 1-7
  - `announce_winner(player: int)`: print winning message
  - `announce_draw()`: print draw message
  - `announce_invalid_move()`: print error for invalid column

## Shared Data Structures

- Board grid: `list[list[int]]` with dimensions 6 rows x 7 columns
  - Row 0 is top, Row 5 is bottom
  - Values: 0 = empty, 1 = Player 1 disc, 2 = Player 2 disc
- Move result dictionary: `{"success": bool, "row": int|None, "winner": int|None, "draw": bool}`

## External Dependencies

- None. Standard library only (no external packages required).
