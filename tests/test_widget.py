import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счёт 35383033474447895560", "Счёт **5560"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card_success(number, expected):
    assert mask_account_card(number) == expected


def test_mask_account_card_errors():
    with pytest.raises(ValueError):
        mask_account_card("")
    with pytest.raises(TypeError):
        mask_account_card(1596837868705199)
    with pytest.raises(TypeError):
        mask_account_card("1548 1596837868705199")
    with pytest.raises(ValueError):
        mask_account_card("Maestro 1548")
    with pytest.raises(ValueError):
        mask_account_card("Счет 646864736788947795891546798326154879")


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-12-05T14:45:09.123456", "05.12.2023"),
        ("2014-02-18T19:54:31.555666", "18.02.2014"),
    ],
)
def test_get_date_success(date, expected):
    assert get_date(date) == expected


def test_get_date_errors():
    with pytest.raises(ValueError):
        get_date("")
    with pytest.raises(ValueError):
        get_date("2014-02-18T19:54:31.555666_biba")
    with pytest.raises(TypeError):
        get_date("boba-09-14T21:27:25.241689")
