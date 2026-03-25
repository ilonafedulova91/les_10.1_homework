from unittest.mock import patch

import pandas as pd
import pytest

from src.data_loader import read_csv, read_excel


@patch("pandas.read_csv")
def test_read_csv_success(mock_read_csv):
    mock_df = pd.DataFrame(
        [
            {"amount": 100, "type": "income"},
            {"amount": 50, "type": "expense"},
        ]
    )
    mock_read_csv.return_value = mock_df

    result = read_csv("test.csv")

    assert result == mock_df.to_dict(orient="records")

    mock_read_csv.assert_called_once_with("test.csv", sep=";")


@patch("pandas.read_csv")
def test_read_csv_file_not_found(mock_read_csv):
    mock_read_csv.side_effect = FileNotFoundError

    result = read_csv("missing.csv")

    assert result == []


def test_read_csv_invalid_extension():
    with pytest.raises(ValueError):
        read_csv("test.txt")


def test_read_csv_invalid_file_path():
    with pytest.raises(ValueError):
        read_csv(123)


@patch("pandas.read_excel")
def test_read_excel_success(mock_read_excel):
    mock_df = pd.DataFrame(
        [
            {"amount": 100, "type": "income"},
            {"amount": 50, "type": "expense"},
        ]
    )
    mock_read_excel.return_value = mock_df

    result = read_excel("test.xlsx")

    assert result == mock_df.to_dict(orient="records")
    mock_read_excel.assert_called_once_with("test.xlsx")


@patch("pandas.read_excel")
def test_read_excel_file_not_found(mock_read_excel):
    mock_read_excel.side_effect = FileNotFoundError

    result = read_excel("missing.xlsx")

    assert result == []


def test_read_excel_invalid_extension():
    with pytest.raises(ValueError):
        read_excel("test.txt")


def test_read_excel_invalid_file_path():
    with pytest.raises(ValueError):
        read_excel(123)
