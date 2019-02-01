import pytest
from pyball import PyBall
from pyball.models.schedule import Date


@pytest.fixture(scope='module')
def schedule_today():
    pyball = PyBall()
    return pyball.get_schedule_by_id_today(12)


@pytest.fixture(scope='module')
def schedule_by_date():
    pyball = PyBall()
    return pyball.get_schedule_by_id_dates(12, '2019-01-01', '2019-01-01')


@pytest.fixture(scope='module')
def schedule_by_dates():
    pyball = PyBall()
    return pyball.get_schedule_by_id_dates(12, '2019-01-01', '2020-01-01')


def test_get_schedule_by_today_returns_date(schedule_today):
    assert isinstance(schedule_today, list)
    assert len(schedule_today) == 1
    assert isinstance(schedule_today[0], Date)


def test_get_schedule_by_day_returns_date(schedule_by_date):
    assert isinstance(schedule_by_date, list)
    assert len(schedule_by_date) == 1
    assert isinstance(schedule_by_date[0], Date)


def test_get_schedules_by_dates_returns_list_of_schedules(schedule_by_dates):
    assert isinstance(schedule_by_dates, list)
    assert len(schedule_by_dates) > 1
    assert isinstance(schedule_by_dates[0], Date)
