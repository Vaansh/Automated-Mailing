import os
import smtp
import time
import tools


def main() -> None:
    credentials = tools.get_credentials("credentials/sample_credentials.json")
    signature = tools.get_signature("signature/signature.html")
    data = tools.read_csv("/dataset/sample.csv")

    for index, row in data.iterrows():
        headers = tools.generate_headers(row, "/package/sample_package.pdf")
        smtp.send_mail(
            credentials[0],
            credentials[1],
            headers,
            tools.get_subject("/template/sample_subject.txt"),
            "/template/sample_body.txt",
            signature,
        )

        # artificial delay
        time.sleep(15)


if __name__ == "__main__":
    main()
