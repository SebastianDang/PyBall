import pytest
from pyball import PyBall
from pyball.models.config import EventType


@pytest.fixture(scope='module')
def test_event_types():
    pyball = PyBall()
    return pyball.get_event_types()


def test_get_event_types_returns_event_types(test_event_types):
    assert isinstance(test_event_types, list)
    assert isinstance(test_event_types[0], EventType)
