import os
import random
from dataclasses import dataclass, field

from main_components.board import Board
from main_components.npc_player import NPCPlayer
from main_components.player import Player
from main_components.scoreboard import Scoreboard
from main_components.ui import UI


@dataclass
class Game:
    ui: UI
    board: Board
    scoreboard: Scoreboard
    players: list[Player]
    player_choice: dict[str, Player] = field(init=False)

    def __post_init__(self) -> None:
        self.player_choice = {}

    def single_game(self) -> str:
        # Represents the Tic Tac Toe

        # Stores the positions occupied by X and O
        player_pos = {"X": [], "O": []}
        cur_player = ("X", self.player_choice["X"])
        # Game Loop for a single game of Tic Tac Toe
        while True:
            self.ui.display_board(self.board.values)

            try:
                move = cur_player[1].make_move(player_pos, cur_player[0])

            except ValueError:
                print("Wrong Input!!! Try Again")
                continue

            # Sanity check for MOVE inout
            if move < 1 or move > 9:
                print("Wrong Input!!! Try Again")
                continue

            # Check if the box is not occupied already
            if self.board.values[move - 1] != " ":
                print("Place already filled. Try again!!")
                continue

            # Updating grid status
            self.board.values[move - 1] = cur_player[0]

            # Updating player positions
            player_pos[cur_player[0]].append(move)

            # Function call for checking win
            if self.board.get_winner(player_pos, cur_player[0]):
                self.ui.display_board(self.board.values)
                print("Player ", cur_player[1].name, " has won the game!!")
                print("\n")
                return cur_player[0]

            # Function call for checking draw game
            if self.board.check_draw(player_pos):
                self.ui.display_board(self.board.values)
                print("Game Drawn")
                print("\n")
                return "D"

            # Switch player moves
            if cur_player == ("X", self.player_choice["X"]):
                cur_player = ("O", self.player_choice["O"])
            else:
                cur_player = ("X", self.player_choice["X"])

    def set_player_choice(
        self, player_one: Player, player_one_choice: int, player_two: Player
    ) -> None:
        if player_one_choice == 1:
            self.player_choice["X"] = player_one
            self.player_choice["O"] = player_two
            return
        elif player_one_choice == 2:
            self.player_choice["X"] = player_two
            self.player_choice["O"] = player_one
        else:
            print("Wrong Choice!!!! Try Again\n")

    def turn(self) -> None:
        while True:

            cur_player, player_two = random.sample(self.players, 2)
            player_one_choice = None
            try:
                player_one_choice = self.ui.display_choose_marker(cur_player)
            except ValueError:
                print("Wrong Input!!! Try Again\n")
                continue

            if player_one_choice == 3:
                self.ui.display_final_score(self.scoreboard.scores)
                break

            if player_one_choice is None:
                continue

            self.set_player_choice(cur_player, player_one_choice, player_two)

            print(f"{self.player_choice['X'].name} starts the game")

            winner = self.single_game()

            # Edits the scoreboard according to the winner
            if winner != "D":
                player_won = self.player_choice[winner]
                self.scoreboard.update_score(player_won.name, 1)

                self.board.clear_board()

            self.scoreboard.display_score(self.ui)
            # Switch player who chooses X or O
            if cur_player == cur_player:
                cur_player = player_two
            else:
                cur_player = cur_player

    def play(self) -> None:
        for player in self.players:
            self.scoreboard.register_player(player.name)
        self.scoreboard.display_score(self.ui)
        self.turn()
