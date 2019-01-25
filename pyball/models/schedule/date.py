from dataclasses import dataclass
from typing import List, Union, Dict, Any

from .game import Game


@dataclass
class Date:
    date: str = None
    totalItems: int = None
    totalEvents: int = None
    totalGames: int = None
    totalGamesInProgress: int = None
    games: List[Union[Game, Dict[str, Any]]] = None
    events: List = None

    def __post_init__(self):
        self.games = [Game(**game) for game in self.games]
