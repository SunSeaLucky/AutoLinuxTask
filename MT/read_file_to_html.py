# -*- coding:utf-8 -*-
from datetime import datetime, timedelta, timezone


def read_to_html(dic):
    with open("MT/index.html", "r", encoding="utf-8") as f:
        html = f.read()
    SHA_TZ = timezone(
        timedelta(hours=8),
        name="Asia/Shanghai",
    )
    if not dic:
        content = f"""
        <li>签到失败</li>
        <li><br></li>
        <li>运行时间: <span>{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(SHA_TZ).strftime('%Y-%m-%d %H:%M:%S')}</span></li>
        """.replace(
            "\t", ""
        )
    else:
        content = f"""\
        <li>欢迎: <span>{dic.get('name')}</span></li>
        <li><br></li>
        <li>连续签到天数: <span>{dic.get('continue')}</span></li>
        <li>签到等级: <span>{dic.get('class')}</span></li>
        <li>积分奖励: <span>{dic.get('award')}</span></li>
        <li>签到总天数: <span>{dic.get('all_day')}</span></li>
        <li>签到排名: <span>{dic.get('num')}</span></li>
        <li><br></li>
        <li>签到时间: <span>{datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(SHA_TZ).strftime('%Y-%m-%d %H:%M:%S')}</span></li>
        """.replace(
            "\t", ""
        )
    _dic = {"content": content, "title": "自动签到成功" if dic else "自动签到失败"}
    return html.format(**_dic)

    # return html


if __name__ == "__main__":
    # dic= {
    #     'continue':'0',
    #     'class':'0',
    #     'award':'0',
    #     'all_day':'0',
    #     'num':'0',
    #     'name':'name',
    # }
    dic = None
    print(read_to_html(dic))
    with open("a.html", "w", encoding="utf-8") as f:
        f.write(read_to_html(dic))
