class Board:
    """Connect Four board - 7 columns x 6 rows."""

    def __init__(self) -> None:
        """Initialize 7x6 empty grid (0=empty, 1=Player 1, 2=Player 2)."""
        self._rows = 6
        self._cols = 7
        self._grid = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

    def is_valid_move(self, column: int) -> bool:
        """Check if column has space."""
        if column < 0 or column >= self._cols:
            return False
        return self._grid[0][column] == 0

    def get_next_open_row(self, column: int) -> int | None:
        """Return lowest empty row in column."""
        if column < 0 or column >= self._cols:
            return None
        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][column] == 0:
                return row
        return None

    def apply_move(self, column: int, player: int) -> bool:
        """Place disc, return success."""
        if not self.is_valid_move(column):
            return False
        row = self.get_next_open_row(column)
        if row is not None:
            self._grid[row][column] = player
            return True
        return False

    def check_winner(self) -> int | None:
        """Return winning player (1 or 2) or None."""
        directions = [
            (0, 1),   # horizontal
            (1, 0),   # vertical
            (1, 1),   # diagonal down-right
            (1, -1),  # diagonal down-left
        ]

        for row in range(self._rows):
            for col in range(self._cols):
                if self._grid[row][col] == 0:
                    continue
                player = self._grid[row][col]
                for dr, dc in directions:
                    if self._check_line(row, col, dr, dc, player):
                        return player
        return None

    def _check_line(self, row: int, col: int, dr: int, dc: int, player: int) -> bool:
        """Check for 4 in a line starting from (row, col) in direction (dr, dc)."""
        for i in range(4):
            r, c = row + i * dr, col + i * dc
            if r < 0 or r >= self._rows or c < 0 or c >= self._cols:
                return False
            if self._grid[r][c] != player:
                return False
        return True

    def is_full(self) -> bool:
        """Check if board is completely filled."""
        return all(self._grid[0][col] != 0 for col in range(self._cols))

    def get_board_state(self) -> list[list[int]]:
        """Return copy of grid."""
        return [row[:] for row in self._grid]
