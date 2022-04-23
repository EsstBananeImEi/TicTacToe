import random
import time

from main_components.player import Player


class CLI:
    def display_board(self, markers: list) -> None:
        print()
        print("     |     |")
        print(f"  {markers[0]}  |  {markers[1]}  |  {markers[2]}")
        print("_____|_____|_____")
        print("     |     |")
        print(f"  {markers[3]}  |  {markers[4]}  |  {markers[5]}")
        print("_____|_____|_____")
        print("     |     |")
        print(f"  {markers[6]}  |  {markers[7]}  |  {markers[8]}")
        print("     |     |")
        print()

    def display_score(self, scores: dict[str, int]) -> None:
        print("--------------------------------")
        print("           SCOREBOARD       ")
        print("--------------------------------")

        for player, score in scores.items():
            print(f"{player}\t{score}")

        print("--------------------------------")

    def read_player_name(self) -> str:
        print("Bitte geben Sie Ihren Namen ein:", end="\t")
        return input().strip()

    def display_choose_marker(self, current_player: Player) -> int:
        return current_player.make_choice()
        

    def display_final_score(self, scores: dict[str, int]) -> None:
        print("--------------------------------")
        print("        FINAL SCOREBOARD       ")
        print("--------------------------------")

        for player, score in scores.items():
            print(f"{player}\t\t{score}")

        print("--------------------------------")

    def display_single_game(self) -> int:
        print("Choose your game mode:")
        print("Enter 1 for Single Player")
        print("Enter 2 for Two Player")
        print("Enter 3 to Quit")
        return int(input())
