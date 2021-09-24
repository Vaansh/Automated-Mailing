import json

def get_credentials() -> list:
    file = open('credentials/credentials.json',)
    data = json.load(file)
    email, password = data['email'], data['password']
    file.close()
    return [email, password]

def main() -> None:
    print(get_credentials())

if __name__ == "__main__":
    main()
