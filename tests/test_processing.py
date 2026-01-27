import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_of_dicts():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_executed(list_of_dicts):
    assert filter_by_state(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(list_of_dicts):
    assert filter_by_state(list_of_dicts, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_no_match(list_of_dicts):
    assert filter_by_state(list_of_dicts, "FAILED") == []


def test_filter_by_state_errors():
    with pytest.raises(ValueError):
        filter_by_state([])
    with pytest.raises(ValueError):
        filter_by_state([{"id": 41428829, "state": "", "date": "2019-07-03T18:35:29.512364"}])


def test_sort_by_date_descending(list_of_dicts):
    assert sort_by_date(list_of_dicts) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_ascending(list_of_dicts):
    assert sort_by_date(list_of_dicts, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_same_dates():
    data = [
        {"id": 1, "date": "2019-01-01T10:00:00.000000"},
        {"id": 2, "date": "2019-01-01T10:00:00.000000"},
        {"id": 3, "date": "2018-12-31T23:59:59.000000"},
    ]

    assert [item["id"] for item in (sort_by_date(data))] == [1, 2, 3]


def test_sort_by_date_errors():
    with pytest.raises(ValueError):
        sort_by_date([])
    with pytest.raises(ValueError):
        sort_by_date([{"id": 41428829, "state": "EXECUTED", "date": ""}])
