import requests
import json
import time

url = "https://api.ctfhub.com/User_API/Event/"
bot_token = "XXXX"


def get_info(actions, data):
    res = requests.post(url + actions, json=data).json()
    if res["status"]:
        return res["data"]
    else:
        print("ERR to get")
        print(res["msg"])
        return res["data"]


def get_ctf(item):
    ctf_infos = ""
    for items in item["items"]:
        c = get_info("getInfo", {"event_id": items["id"]})
        items["official_url"] = c["official_url"]
        items["class"] = c["class"]
        items["form"] = c["form"]
        items['start_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(items['start_time']))
        items['end_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(items['end_time']))
        ctf_infos += "{title}\n{class} {form}\n{start_time} ~ {end_time}\n{official_url}\n\n".format(**items)
    return ctf_infos


if __name__ == '__main__':
    send_str = "【CTF比赛通知】\n\n"
    c = get_info("getUpcoming", {"offset": 0, "limit": 5})
    r = get_info("getRunning", {"offset": 0, "limit": 5})

    send_str += "【进行中的比赛】\n" + get_ctf(r) + "【即将开始】\n" + get_ctf(c)
    requests.post("https://api.bot.wgpsec.org/push/" + bot_token, {"txt": send_str})
    print(send_str)
    pass
