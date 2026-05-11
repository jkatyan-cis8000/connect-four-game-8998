from board import Board


class Game:
    def __init__(self, board: Board):
        self.board = board
        self.current_player = 1

    def play_turn(self, column: int) -> dict:
        if not self.board.is_valid_move(column):
            return {"success": False, "row": None, "winner": None, "draw": False}
        row = self.board.get_next_open_row(column)
        self.board.apply_move(column, self.current_player)
        winner = self.board.check_winner()
        draw = self.board.is_full()
        if winner is not None or draw:
            return {"success": True, "row": row, "winner": winner, "draw": draw}
        return {"success": True, "row": row, "winner": None, "draw": False}

    def switch_player(self):
        self.current_player = 3 - self.current_player

    def get_current_player(self) -> int:
        return self.current_player

    def game_over(self) -> bool:
        return self.board.check_winner() is not None or self.board.is_full()
