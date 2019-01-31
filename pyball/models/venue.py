from dataclasses import dataclass, field
from typing import Dict, Any
from collections import namedtuple


@dataclass
class Venue:
    id: int = field(default=None)
    link: str = field(default=None)
    name: str = field(default=None)
    location: Dict[str, Any] = None

    def __post_init__(self):
        self.location = namedtuple('location', self.location.keys())(*self.location.values()) if self.location else None