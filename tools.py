import os
import csv
import json
import pandas as pd

from pathlib import Path


def get_credentials(path: str) -> list:
    file = open(path)
    data = json.load(file)
    user, password = data["user"], data["password"]
    file.close()
    return [user, password]


def get_signature(path: str) -> str:
    txt = Path(path).read_text()
    return txt.replace("\n", "")


def read_csv(path: str) -> str:
    return pd.read_csv(os.getcwd() + path)


def generate_headers(row: list, path: str) -> dict:
    headers = {
        "email": row[0],
        "recipient name": row[1],
        "company name": row[2],
        "contact name": row[3],
        "package path": os.getcwd() + path,
    }
    return headers
