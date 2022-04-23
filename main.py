from main_components.board import Board
from main_components.cli import CLI
from main_components.game import Game
from main_components.human_player import HumanPlayer
from main_components.npc_player import NPCPlayer
from main_components.player import Player
from main_components.scoreboard import Scoreboard


def main() -> None:
    cli = CLI()
    scoreboard = Scoreboard()
    board = Board()
    game_mode = cli.display_single_game()

    player_list: list[Player] = []
    if game_mode == 1:
        player_list.append(HumanPlayer(cli.read_player_name()))
        player_list.append(NPCPlayer())
    elif game_mode == 2:
        player_list.append(HumanPlayer(cli.read_player_name()))
        player_list.append(HumanPlayer(cli.read_player_name()))
    elif game_mode == 3:
        print("Thank you for playing Tic Tac Toe")
        return

    game = Game(cli, board, scoreboard, player_list)
    game.play()


if __name__ == "__main__":
    main()
