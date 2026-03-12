import json
from io import StringIO
from unittest.mock import mock_open, patch

from src.utils import load_json_operations


def test_load_json_operations_success():
    expected_data = [{"id": 1}, {"id": 2}]
    mocked_file = mock_open(read_data=json.dumps(expected_data))

    with patch("builtins.open", mocked_file):
        result = load_json_operations("fake_path.json")

    assert result == expected_data


def test_load_json_operations_file_not_found_error():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = load_json_operations("fake_path.json")

    assert result == []


def test_load_json_operations_not_list():
    data = {"id": 1}
    mocked_file = mock_open(read_data=json.dumps(data))

    with patch("builtins.open", mocked_file):
        result = load_json_operations("fake_path.json")

    assert result == []


def test_load_json_operations_empty_file():
    empty_file = StringIO()

    with patch("builtins.open", return_value=empty_file):
        result = load_json_operations("fake_path.json")

    assert result == []
