import logging
from pathlib import Path
from typing import Union

PROJECT_DIR = Path(__file__).parent.parent
LOGS_DIR = PROJECT_DIR / "logs"

LOGS_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOGS_DIR / "masks.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """This function returns a hidden card number"""

    logger.info('The function "Mask card number" has started')

    if card_number == 0 or card_number == "" or card_number is None:
        logger.error("Card number is empty")
        raise ValueError("Card number is empty")

    number_str = str(card_number).replace(" ", "")

    if len(number_str) != 16:
        logger.error("Card number is invalid")
        raise ValueError("Card number is invalid")

    card_masked = number_str[:4] + " " + number_str[4:6] + "*" * 2 + " " + "*" * 4 + " " + number_str[12:]
    logger.debug(f"Masked card number: {card_masked}")
    logger.info('The function "Mask card number" has finished')
    return card_masked


def get_mask_account(account_number: Union[int, str]) -> str:
    """This function returns a hidden account number"""

    logger.info('The function "Mask account number" has started')

    if account_number == 0 or account_number == "" or account_number is None:
        logging.error("Account number is empty")
        raise ValueError("Account number is empty")

    number_str = str(account_number).replace(" ", "")

    if len(number_str) != 20:
        logging.error("Account number is invalid")
        raise ValueError("Account number is invalid")

    account_masked = "*" * 2 + number_str[-4:]
    logger.debug(f"Masked account number: {account_masked}")
    logger.info('The function "Mask account number" has finished')
    return account_masked
