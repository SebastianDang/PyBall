from dataclasses import dataclass
from typing import Dict, Any
from collections import namedtuple


@dataclass
class Team:
    leagueRecord: Dict[str, Any] = None
    score: int = None
    team: Dict[str, Any] = None
    isWinner: bool = None
    splitSquad: bool = None
    seriesNumber: int = None

    def __post_init__(self):
      self.leagueRecord = namedtuple('LeagueRecord', self.leagueRecord.keys())(*self.leagueRecord.values()) if self.leagueRecord else None
      self.team = namedtuple('Team', self.team.keys())(*self.team.values()) if self.team else None
