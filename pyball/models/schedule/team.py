from dataclasses import dataclass
from typing import Union, Dict, Any


@dataclass
class Team:
    leagueRecord: Dict = None
    score: int = None
    team: Dict[str, Any] = None
    id: int = None
    name: str = None
    link: str = None
    isWinner: bool = None
    splitSquad: bool = None
    seriesNumber: int = None
