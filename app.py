from iKuuuVPN import signer as ik_signer
import Mail
import os

from dotenv import load_dotenv

load_dotenv(".env")


def exec_sign_task():
    res = []

    res.append({"name": "iKuuu VPN", "resText": ik_signer.sign()})

    main_text = "Below is sign detail:\n\n"

    for i in res:
        main_text += (
            "**"
            + str(i["name"])
            + "**\n\n"
            + str(i["resText"])
            + "\n\n-----------------"
        )

    return main_text


Mail.send_email(
    "Sign Notifications",
    exec_sign_task(),
    os.environ.get("FROM_MAIL_ADDR"),
    os.environ.get("TO_MAIL_ADDR"),
    os.environ.get("STMP_SERVER"),
    os.environ.get("FROM_MAIL_PASSWORD"),
)
