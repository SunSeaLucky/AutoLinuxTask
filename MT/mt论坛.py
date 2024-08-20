import time
import requests
import re
import os
from dotenv import load_dotenv

load_dotenv(".env")
username = os.environ.get("MT_USERNAME")
password = os.environ.get("MT_PASSWORD")

dic = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def catch(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return False

    return wrapper


def get_more_data(text):
    def get_num(i):
        num = ""
        for i in re.findall('<span class="(.*?)"></span>', dates[i]):
            num += dic[i]
        return num

    # with open('a.html','w',encoding='utf-8')as f:
    #     f.write(text)
    dic_ = {}
    dates = re.findall(
        '<b class="pics J_numpic J_animation" style=".*?">(.*?)</b>', text, re.DOTALL
    )
    if dates != []:
        dic_["continue"] = get_num(0)  # 连续签到天数
        dic_["class"] = "LV." + get_num(1)  # 签到等级
        dic_["award"] = get_num(2)  # 积分奖励
        dic_["all_day"] = get_num(3)  # 签到总天数
    dates = re.findall('<div class="font">(.*?)</div>', text, re.DOTALL)
    if dates != []:
        dic_["num"] = dates[0].replace("\r\n", "").strip().split("：")[-1]  # 签到排名
    dates = re.findall(
        '<div id="comiis_key".*?<span>(.*?)</span>.*?</div>', text, re.DOTALL
    )
    if dates != []:
        dic_["name"] = dates[0]  # 获取名字
    return dic_


@catch
def start():
    session = requests.Session()
    push_text = "mt论坛："
    headers = {
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Pragma": "no-cache",
        "Sec-Fetch-Dest": "image",
        "Sec-Fetch-Mode": "no-cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-gpc": "1",
        "Referer": "https://bbs.binmt.cc/",
        "Content-Type": "application/json; charset=utf-8",
        "Origin": "https://bbs.binmt.cc",
        "Access-Control-Request-Headers": "content-type",
        "Access-Control-Request-Method": "POST",
    }
    cookies = {
        "cQWy_2132_saltkey": "di6I8Adv",
        "cQWy_2132_lastvisit": "1713785383",
        "cQWy_2132_client_created": "1714118646",
        "cQWy_2132_client_token": "80959163C8253AB37D01C100A4B3F13F",
        "cQWy_2132_auth": "73f1HMI88M%2FDX81EDf5cRUsNy%2BHuSL%2F6KRXO6jDkADekBS6R2f%2B8USVHMkNivdU3G%2B4studfAgJk1pAZRtJQLwqCOg",
        "cQWy_2132_connect_login": "1",
        "cQWy_2132_connect_is_bind": "1",
        "cQWy_2132_connect_uin": "80959163C8253AB37D01C100A4B3F13F",
        "cQWy_2132_nofavfid": "1",
        "cQWy_2132_visitedfid": "41",
        "cQWy_2132_ulastactivity": "f451UGOFYjP3Enky262dGQJOj2sq14nnmzv3jEZaDmCIS%2F7%2BrnO1",
        "cQWy_2132_smile": "5D1",
        "cQWy_2132_home_diymode": "1",
        "cQWy_2132_sid": "Numihh",
        "cQWy_2132_lip": "112.96.227.205%2C1715000989",
        "cQWy_2132_checkpm": "1",
        "cQWy_2132_lastcheckfeed": "70136%7C1715002748",
        "cQWy_2132_checkfollow": "1",
        "cQWy_2132_sendmail": "1",
        "cQWy_2132_lastact": "1715002761%09index.php%09",
    }
    # 获取登陆所需loginhash和formhash
    getHash_url = "https://bbs.binmt.cc/member.php?mod=logging&action=login&infloat=yes&handlekey=login&inajax=1&ajaxtarget=fwin_content_login"
    session.get(headers=headers, url=getHash_url, cookies=cookies)
    time.sleep(5)
    headers["referer"] = getHash_url
    page_text = session.get(headers=headers, url=getHash_url).text
    print(page_text)

    loginhash_ex = 'loginhash=(.*?)">'
    formhash_ex = 'formhash" value="(.*?)".*? />'

    loginhash = re.findall(loginhash_ex, page_text, re.S)[0]
    formhash = re.findall(formhash_ex, page_text, re.S)[0]
    # print(loginhash, formhash)
    # 模拟登陆
    login_url = (
        "https://bbs.binmt.cc/member.php?mod=logging&action=login&loginsubmit=yes&handlekey=login&loginhash="
        + loginhash
        + "&inajax=1"
    )
    data = {
        "formhash": formhash,
        "referer": "https://bbs.binmt.cc/index.php",
        "loginfield": "username",
        "username": username,
        "password": password,
        "questionid": "0",
        "answer": "",
    }
    print(data)
    page_text1 = session.post(headers=headers, url=login_url, data=data).text
    # print(page_text1)
    # 验证是否登陆成功
    check_ex = "root"
    check = re.findall(check_ex, page_text1, re.S)
    if len(check) != 0:
        print("登录成功")
        push_text = push_text + "登陆成功，"
        # 获取签到所需的formhash
        getHash_url1 = "https://bbs.binmt.cc/k_misign-sign.html"
        page_text = session.get(headers=headers, url=getHash_url1).text
        formhash1 = re.findall(formhash_ex, page_text, re.S)[0]
        # 模拟签到
        sign_url = (
            "https://bbs.binmt.cc/plugin.php?id=k_misign:sign&operation=qiandao&format=text&formhash="
            + formhash1
        )
        page_text2 = session.get(headers=headers, url=sign_url).text
        # 验证是否签到成功
        check = re.findall(check_ex, page_text2, re.S)
        if len(check) != 0:
            print("签到成功")
            push_text = push_text + "签到成功"
            print(push_text)
            return get_more_data(session.get(headers=headers, url=getHash_url1).text)
        else:
            print("签到失败")
            push_text = push_text + "签到失败"
    else:
        print("登陆失败")
        push_text = push_text + "登陆失败，"
    print(push_text)


if __name__ == "__main__":
    from read_file_to_html import read_to_html
    from mail_to import Mail

    if not username or not password:
        print("请设置环境变量 USERNAME PASSWORD")
        exit(1)
    data = start()
    html = read_to_html(data)
    mail = Mail()
    if mail.send(html):
        print("发送成功")
    else:
        print(html)
        print("发送失败")
