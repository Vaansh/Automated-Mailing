import os
import tools
import smtp


def main() -> None:
    credentials = tools.get_credentials()
    signature = tools.get_signature()

    headers = {
        "email": "sample@sample.com",
        "recipient name": "recruiter",
        "contact name": "teammate",
        "package path": os.getcwd() + "/package/sample-package.pdf",
    }

    smtp.send_mail(credentials[0], credentials[1], headers, "test", signature)


if __name__ == "__main__":
    main()
