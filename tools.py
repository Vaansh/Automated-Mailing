import json


def get_credentials() -> list:
    file = open(
        "credentials/credentials.json",
    )
    data = json.load(file)
    email, password = data["email"], data["password"]
    file.close()
    return [email, password]
