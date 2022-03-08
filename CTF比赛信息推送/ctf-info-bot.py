import requests
import json
import time

CTF_INFO = "https://api.ctfhub.com/User_API/Event/getInfo"

CTF_UPCOMING = "https://api.ctfhub.com/User_API/Event/getUpcoming"

bot_api = "https://api.bot.wgpsec.org/push/0f8114e60fc750df0870da0bd81732fc?txt="

Header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

ctfs = []

def TransTime():
    global ctfs
    for ctf in ctfs:
        ctf['start_time'] = time.strftime('%Y-%m-%d', time.localtime(ctf['start_time']))


def GetUpcoming():
    global ctfs

    res = requests.post(url=CTF_UPCOMING, headers=Header, json={
        "offset": 0,
        "limit": 5
    })
    ctfs = res.json()['data']['items']


def PostBot():
    global ctfs

    Str1 = '''
    // @Gungnir
    // 【CTF比赛推送】
    
    接下来的5场CTF比赛:
    1.[{start_time}] {title}
    '''.format(**ctfs[0])

    Str2 = '''2.[{start_time}] {title}
    '''.format(**ctfs[1])

    Str3 = '''3.[{start_time}] {title}
    '''.format(**ctfs[2])

    Str4 = '''4.[{start_time}] {title}
    '''.format(**ctfs[3])

    Str5 = '''5.[{start_time}] {title}
    【信息来源CTFHub】
    '''.format(**ctfs[4])

    Str = Str1+Str2+Str3+Str4+Str5

    requests.get(url=bot_api+Str)


if __name__ == '__main__':
    GetUpcoming()
    TransTime()
    PostBot()