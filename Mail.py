import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


def send_email(subject, message, from_addr, to_addr, smtp_server, password, port=465):
    # 创建一个MIMEText邮件对象，这里是文本内容
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = Header(from_addr)
    msg["To"] = Header(to_addr)
    msg["Subject"] = Header(subject, "utf-8")

    # 连接到SMTP服务器使用SSL
    server = smtplib.SMTP_SSL(smtp_server, port)  # 注意使用SMTP_SSL而不是SMTP
    server.login(from_addr, password)  # 登录SMTP服务器
    server.sendmail(from_addr, [to_addr], msg.as_string())  # 发送邮件
    server.quit()


if __name__ == "__main__":
    # 邮件内容
    subject = "AutoLinuxTasksAlert"
    message = "这是一封来自Python脚本的测试邮件。"

    from_addr = os.environ.get("FROM_MAIL_ADDR")
    to_addr = os.environ.get("TO_MAIL_ADDR")
    smtp_server = os.environ.get("STMP_SERVER")
    password = os.environ.get("FROM_MAIL_PASSWORD")

    send_email(subject, message, from_addr, to_addr, smtp_server, password)
