from dataclasses import dataclass
from typing import Optional, Protocol


@dataclass
class Player(Protocol):
    name: str

    def make_move(self, board_values: dict[str, list[int]], sign: str) -> int:
        raise NotImplementedError()

    def make_choice(self) -> int:
        raise NotImplementedError()