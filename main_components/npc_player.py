import random
import time
from dataclasses import dataclass, field

import names


def create_npc_opponent() -> str:
    return f"{names.get_first_name()}"


@dataclass
class NPCPlayer:
    name: str = field(default_factory=create_npc_opponent)

    def make_move(self, board_values: dict[str, list[int]], sign: str) -> int:
        print(f"{self.name}'s' ({sign}) turn. Which Box will he choose? : ", end="")
        print(f"{self.name} is thinking...")
        time.sleep(2)
        chained_lists = board_values["X"] + board_values["O"]
        allowed_moves = list(filter(lambda x: x not in chained_lists, range(1, 10)))
        return random.choice(allowed_moves)

    def make_choice(self) -> int:
        choice = random.choice([(1, "X"), (2, "O")])
        print(f"{self.name} is choosing sign...")
        time.sleep(2)
        print(f"{self.name} choose {choice[1]}")
        return choice[0]
