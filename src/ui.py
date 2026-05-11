class UI:
    def __init__(self):
        self.player_names = {1: "Player 1", 2: "Player 2"}
        self.current_player = 1

    def display_board(self, board_state: list[list[int]]) -> None:
        print()
        for row in board_state:
            print("|" + "|".join(str(cell) if cell != 0 else " " for cell in row) + "|")
        print("-" * 15)
        print(" 1 2 3 4 5 6 7 ")
        print()

    def get_column_input(self, current_player: int | None = None) -> int:
        if current_player is not None:
            self.current_player = current_player
        while True:
            try:
                choice = int(input(f"{self.player_names[self.current_player]}, choose column (1-7): "))
                if 1 <= choice <= 7:
                    return choice - 1
                print("Invalid column. Choose 1-7.")
            except ValueError:
                print("Invalid input. Enter a number.")

    def announce_winner(self, player: int) -> None:
        print(f"{self.player_names[player]} wins!")

    def announce_draw(self) -> None:
        print("It's a draw!")

    def announce_invalid_move(self) -> None:
        print("Invalid move. Column is full.")
