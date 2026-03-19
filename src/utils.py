import json
import logging
from pathlib import Path

PROJECT_DIR = Path(__file__).parent.parent
LOGS_DIR = PROJECT_DIR / "logs"

LOGS_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(LOGS_DIR / "utils.log", "w", "utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def load_json_operations(file_path: str) -> list[dict]:
    """This function loads financial operations from a json file"""

    logger.info(f"Loading operations from {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            operations = json.load(file)

            if isinstance(operations, list):
                logger.info("Operations successfully loaded")
                return operations
            logger.warning("JSON content is not a list")
            return []

    except FileNotFoundError:
        logging.error("File not found")
        return []
    except json.JSONDecodeError:
        logging.error("JSON decoding error")
        return []
