import pandas as pd

def read_csv(file_path: str) -> list[dict]:
    """The function reads a csv file"""
    if not isinstance(file_path, str):
        raise ValueError("The file path must be a string")
    if not file_path.endswith(".csv"):
        raise ValueError("The file path must end with .csv")

    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        return []

    return df.to_dict(orient="records")

def read_excel(file_path: str) -> list[dict]:
    """The function reads an excel file"""
    if not isinstance(file_path, str):
        raise ValueError("The file path must be a string")
    if not file_path.endswith(".xlsx"):
        raise ValueError("The file path must end with .xlsx")

    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        return []
    return df.to_dict(orient="records")
