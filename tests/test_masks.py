import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("5694782358912486", "5694 78** **** 2486"),
        ("24  896  5713 8269  478", "2489 65** **** 9478"),
    ],
)
def test_get_mask_card_number_success(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_value_error():
    with pytest.raises(ValueError):
        get_mask_card_number(7000792289606361152)
    with pytest.raises(ValueError):
        get_mask_card_number(0)
    with pytest.raises(ValueError):
        get_mask_card_number("")


@pytest.mark.parametrize(
    "account_number, expected",
    [(73654108430135874305, "**4305"), ("15963487695823641958", "**1958"), ("485 968  74896   32154 687 9", "**6879")],
)
def test_get_mask_account_success(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_value_error():
    with pytest.raises(ValueError):
        get_mask_account(736541084634586)
    with pytest.raises(ValueError):
        get_mask_account(0)
    with pytest.raises(ValueError):
        get_mask_account("")
