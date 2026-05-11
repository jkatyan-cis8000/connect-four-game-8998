import sys
sys.path.insert(0, 'src')

from board import Board
from game import Game


def test_game_init():
    board = Board()
    game = Game(board)
    assert game.get_current_player() == 1


def test_play_turn_success():
    board = Board()
    game = Game(board)
    result = game.play_turn(3)
    assert result["success"] is True
    assert result["row"] == 5
    assert result["winner"] is None
    assert result["draw"] is False


def test_play_turn_invalid():
    board = Board()
    game = Game(board)
    for _ in range(6):
        game.play_turn(3)
    result = game.play_turn(3)
    assert result["success"] is False
    assert result["row"] is None


def test_switch_player():
    board = Board()
    game = Game(board)
    assert game.get_current_player() == 1
    game.switch_player()
    assert game.get_current_player() == 2
    game.switch_player()
    assert game.get_current_player() == 1


def test_game_over_after_win():
    board = Board()
    game = Game(board)
    for i in range(4):
        game.play_turn(i)
    game.switch_player()
    for i in range(4):
        game.play_turn(i)
    game.switch_player()
    game.play_turn(4)
    assert game.game_over() is True


def test_game_over_after_draw():
    board = Board()
    game = Game(board)
    while not game.game_over():
        for col in range(7):
            if not game.game_over():
                game.play_turn(col)
        game.switch_player()
    assert game.game_over() is True


if __name__ == "__main__":
    test_game_init()
    test_play_turn_success()
    test_play_turn_invalid()
    test_switch_player()
    test_game_over_after_win()
    test_game_over_after_draw()
    print("All tests passed!")
