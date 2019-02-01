from dataclasses import dataclass
from typing import Union, Dict, Any
from collections import namedtuple

from .status import Status
from .teams import Teams
from .venue import Venue


@dataclass
class Game:
    gamePk: int = None
    link: str = None
    gameType: str = None
    season: str = None
    gameDate: str = None
    resumedFrom: str = None
    resumeDate: str = None
    rescheduledFrom: str = None
    rescheduleDate: str = None
    status: Union[Status, Dict[str, Any]] = None
    teams: Union[Teams, Dict[str, Any]] = None
    venue: Union[Venue, Dict[str, Any]] = None
    content: Dict[str, Any] = None
    isTie: bool = None
    gameNumber: int = None
    doubleHeader: str = None
    gamedayType: str = None
    tiebreaker: str = None
    calendarEventID: str = None
    seasonDisplay: str = None
    dayNight: str = None
    description: str = None
    scheduledInnings: int = None
    gamesInSeries: int = None
    seriesGameNumber: int = None
    seriesDescription: str = None
    recordSource: str = None
    ifNecessary: str = None
    ifNecessaryDescription: str = None

    def __post_init__(self):
        self.status = Status(**self.status) if self.status else None
        self.teams = Teams(**self.teams) if self.teams else None
        self.venue = Venue(**self.venue) if self.venue else None
        self.content = namedtuple('Content', self.content.keys())(*self.content.values()) if self.content else None
