import requests
import os
import codecs

from dotenv import load_dotenv

load_dotenv(".env")


username = os.environ.get("IKUUU_USERNAME")
password = os.environ.get("IKUUU_PASSWORD")


def sign():
    session = requests.Session()

    session.post(
        url="https://ikuuu.pw/auth/login",
        data={
            "host": "ikuuu.pw",
            "email": username,
            "passwd": password,
            "code": "",
        },
    )

    res = session.post("https://ikuuu.pw/user/checkin")

    return codecs.unicode_escape_decode(res.text)


if __name__ == "__main__":
    print(sign())
