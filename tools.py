import json

from pathlib import Path


def get_credentials() -> list:
    file = open(
        "credentials/credentials.json",
    )
    data = json.load(file)
    user, password = data["user"], data["password"]
    file.close()
    return [user, password]


def get_signature() -> str:
    txt = Path("signature/signature.html").read_text()
    return txt.replace("\n", "")
