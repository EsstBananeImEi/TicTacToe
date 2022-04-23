from dataclasses import dataclass, field

POSSIBLE_WINNING_COMBINATIONS = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]


class Board:
    def __init__(self) -> None:
        self.values: list = [" " for x in range(9)]

    def update_board(self, player, position) -> None:
        self.values[position - 1] = player

    def get_winner(self, player_positions, player_name) -> bool:

        for x in POSSIBLE_WINNING_COMBINATIONS:
            if all(y in player_positions[player_name] for y in x):
                return True
        return False

    def check_draw(self, player_positions) -> bool:
        if len(player_positions["X"]) + len(player_positions["O"]) == 9:
            return True
        return False

    def clear_board(self) -> None:
        self.values = [" " for x in range(9)]
