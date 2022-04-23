from dataclasses import dataclass


@dataclass
class HumanPlayer:
    name: str

    def make_move(self, board_values: dict[str, list[int]], sign: str) -> int:
        print(f"{self.name}'s' ({sign}) turn. Which box? : ", end="")
        return int(input())

    def make_choice(self) -> int:
        print(f"{self.name} choose your sign:")
        print("Information: 'X' begins the game")
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 to Quit")
        return int(input())
