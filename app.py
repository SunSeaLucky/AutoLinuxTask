from iKuuuVPN import signer as ik_signer
import Mail
import ENV


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
    ENV.FROM_MAIL_ADDR,
    ENV.TO_MAIL_ADDR,
    ENV.STMP_SERVER,
    ENV.FROM_MAIL_PASSWORD,
)
