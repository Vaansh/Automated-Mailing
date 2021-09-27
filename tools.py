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
        "EMAIL": row[0],
        "RECIPIENT_NAME": row[1],
        "COMPANY_NAME": row[2],
        "CONTACT_NAME": row[3],
        "PACKAGE_PATH": os.getcwd() + path,
    }
    return headers


def get_subject(path: str) -> str:
    with open(os.getcwd() + path, "rt") as f:
        subject = f.read()
    return subject


def generate_body(path: str, headers: list) -> str:
    with open(os.getcwd() + path, "r") as f:
        body = f.read()
        body = (
            body.replace("Hello RECIPIENT_NAME", "Hello")
            if not isinstance(headers["RECIPIENT_NAME"], str)
            else body.replace("RECIPIENT_NAME", headers["RECIPIENT_NAME"])
        )
        body = body.replace("COMPANY_NAME", headers["COMPANY_NAME"])
        body = body.replace("CONTACT_NAME", headers["CONTACT_NAME"])
        body = body + "\n\n"
    return body
