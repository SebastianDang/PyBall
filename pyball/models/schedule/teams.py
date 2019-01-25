from dataclasses import dataclass
from typing import Union, Dict, Any

from .team import Team


@dataclass
class Teams:
    away: Union[Team, Dict[str, Any]] = None
    home: Union[Team, Dict[str, Any]] = None

    def __post_init__(self):
        self.away = Team(**self.away)
        self.home = Team(**self.home)
