from dataclasses import dataclass
from main_components.grid import Grid
from main_components.ui import UI
import names


@dataclass
class Game:
    grid: Grid
    ui: UI
    player_name: str
    npc_name: str = names.get_first_name()
