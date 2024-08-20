import requests
import codecs
import ENV

from dotenv import load_dotenv


def sign():
    session = requests.Session()

    session.post(
        url="https://ikuuu.pw/auth/login",
        data={
            "host": "ikuuu.pw",
            "email": ENV.IKUUU_USERNAME,
            "passwd": ENV.IKUUU_PASSWORD,
            "code": "",
        },
    )

    res = session.post("https://ikuuu.pw/user/checkin")

    return codecs.unicode_escape_decode(res.text)


if __name__ == "__main__":
    print(sign())
