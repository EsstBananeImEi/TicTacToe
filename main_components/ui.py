from typing import Protocol

from main_components.player import Player


class UI(Protocol):
    def display_board(self, markers: list) -> None:
        raise NotImplementedError()

    def display_score(self, scores: dict[str, int]) -> None:
        raise NotImplementedError()

    def read_player_name(self) -> str:
        raise NotImplementedError()

    def display_choose_marker(self, current_player: Player) -> int:
        raise NotImplementedError()

    def display_final_score(self, scores: dict[str, int]) -> None:
        raise NotImplementedError()
