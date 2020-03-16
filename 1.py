# coding=utf-8
# @Time : 2019/12/13 14:50
# @Author : 蒲发启
# @File : 1.py
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()


def get_news():
    """获取金山词霸每日一句，英文和翻译"""

    url = "http://open.iciba.com/dsapi/"
    data = requests.get(url)
    content = data.json()['content']
    note = data.json()['note']
    return content, note


def send_news():
    try:
        content, note = get_news()
        # 你朋友的微信名称，不是备注，也不是微信帐号。
        my_friend = bot.friends().search(u'脉动')[0]
        my_friend.send(content)
        my_friend.send(note)
        my_friend.send(u"Have a good one!")
        # 每86400秒（1天），发送1次
        i = 0
        t = Timer(1, send_news)
        print(i, content)
        i += 1
        t.start()
    except:
        # 你的微信名称，不是微信帐号。
        my_friend = bot.friends().search('小二丶上酒')[0]
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    send_news()