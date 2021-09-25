import os
import smtp
import tools


def main() -> None:
    credentials = tools.get_credentials("credentials/sample_credentials.json")
    signature = tools.get_signature("signature/signature.html")
    data = tools.read_csv("/dataset/sample.csv")

    for index, row in data.iterrows():
        headers = tools.generate_headers(row, "/package/sample_package.pdf")
        smtp.send_mail(credentials[0], credentials[1], headers, "test", signature)


if __name__ == "__main__":
    main()
