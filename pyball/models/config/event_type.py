from dataclasses import dataclass


@dataclass
class EventType:
    code: str = None
    description: str = None
