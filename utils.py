import json


def load_json_operations(file_path: str) -> list[dict]:
    """This function loads financial operations from a json file"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            operations = json.load(file)

            if isinstance(operations, list):
                return operations
            return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == "__main__":
    print(load_json_operations("C:\PythonProjects\les_12.1_homework\data\operations.json"))
