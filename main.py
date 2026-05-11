import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from board import Board
from game import Game
from ui import UI


def main():
    board = Board()
    game = Game(board)
    ui = UI()
    
    while not game.game_over():
        ui.display_board(board.get_board_state())
        column = ui.get_column_input(game.get_current_player())
        result = game.play_turn(column)
        if not result["success"]:
            ui.announce_invalid_move()
            continue
        if result["winner"] is not None:
            ui.display_board(board.get_board_state())
            ui.announce_winner(result["winner"])
            break
        if result["draw"]:
            ui.display_board(board.get_board_state())
            ui.announce_draw()
            break
        game.switch_player()


if __name__ == "__main__":
    main()
