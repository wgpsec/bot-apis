import re
import json
import time
import requests
from bs4 import BeautifulSoup


def notice(name, title, notice_time):
    requests.get(
        "https://bot.wgpsec.org/push/40bba192738e928c401a3490188fea21?txt=%s %s 有新公告：%s" % (notice_time, name, title))


def print_color(name, notice_time, title):
    grep_list = ['活动', '周岁', '周年', '双倍', '三倍', '端午', '七夕', '双11安全保卫战']
    num = 1
    for i in grep_list:
        if (i in title) and (num == 1) and ('2022' in notice_time or notice_time == '' or '22-' in notice_time) and (
                '公示' not in title and '公告' not in title):
            print('\033[0;33m| \033[0m\033[0;31m%s\t%s\033[0m' % (notice_time, title))
            num = num + 1
    if num == 1:
        print('\033[0;33m| \033[0m' + notice_time + '\t' + title)

    current_day = time.strftime("%Y-%m-%d", time.localtime())
    if current_day == notice_time.strip():
        notice(name, title, notice_time)


def src_360(number):
    print('\n\033[0;33m-----------------------360 SRC------------------------\033[0m')
    url = 'https://security.360.cn/News/news?type=-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.news-content')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 4].select('.new-list-time')[0].text.strip()
        title = notice_list[i + 4].select('a')[0].text
        print_color('360', time, title)


def src_58(number):
    print('\n\033[0;33m-----------------------58 SRC------------------------\033[0m')
    url = 'https://security.58.com/notice/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.time')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.box')[0].select('a')[i].text
        print_color('58', time, title)


def alibaba(number):
    print('\n\033[0;33m-----------------------阿里SRC------------------------\033[0m')
    url = 'https://security.alibaba.com/api/asrc/pub/announcements/list.json?&page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['lastModify'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('阿里', time, title)


def iqiyi(number):
    print('\n\033[0;33m-----------------------爱奇艺SRC----------------------\033[0m')
    url = 'https://security.iqiyi.com/api/publish/notice/list?sign=6ce5b4f7ad460b2ae3046422f61f905e4e3ecd03'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time_str']
        title = notice_list[i]['title']
        print_color('爱奇艺', time, title)


def baidu(number):
    print('\n\033[0;33m-----------------------百度SRC------------------------\033[0m')
    url = 'https://bsrc.baidu.com/v2/api/announcement?type=&page=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['retdata']['announcements']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('百度', time, title)


def ke(number):
    print('\n\033[0;33m-----------------------贝壳SRC------------------------\033[0m')
    url = 'https://security.ke.com/api/notices/list'
    headers = {
        'Referer': 'https://security.ke.com/notices',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data={"page": 1})
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('贝壳', time, title)


def bilibili(number):
    print('\n\033[0;33m-----------------------哔哩哔哩SRC---------------------\033[0m')
    url = 'https://security.bilibili.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    number = number * 2 + 1
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(2, number, 2):
        time = notice_list[i].text.replace('\n', '')
        title = notice_list[i + 1].text.replace('\n', '')
        print_color('哔哩哔哩', time, title)


def cainiao(number):
    print('\n\033[0;33m-----------------------菜鸟SRC------------------------\033[0m')
    url = 'https://sec.cainiao.com/announcement.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text.split('\n')[0].strip().split('][')[0].replace('[', '')
        title = notice_list[i].text.split('\n')[1].strip()
        print_color('菜鸟', time, title)


def didichuxing(number):
    print('\n\033[0;33m-----------------------滴滴出行SRC---------------------\033[0m')
    url = 'http://sec.didichuxing.com/rest/article/list?page=1&size=5&option=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['time']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('滴滴出行', time_format, title)


def ly(number):
    print('\n\033[0;33m-----------------------同程旅行SRC---------------------\033[0m')
    url = 'https://sec.ly.com/index.php?m=&c=page&a=index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.list_title')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.list_date')[0].text.replace('/', '-')
        title = notice_list[i].text
        print_color('同程旅行', time, title)


def duxiaoman(number):
    print('\n\033[0;33m-----------------------度小满SRC----------------------\033[0m')
    url = 'https://security.duxiaoman.com/index.php?v2api/announcelist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='page=1&type=0&token=null')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['time']
        title = notice_list[i]['title']
        print_color('度小满', time, title)


def eastmoney(number):
    print('\n\033[0;33m-----------------------东方财富SRC---------------------\033[0m')
    url = 'https://security.eastmoney.com/news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.anno-lst-date')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.anno-lst-cons')[i].text.split('\xa0')[1].split('\n')[0]
        print_color('东方财富', time, title)


def fadada(number):
    print('\n\033[0;33m-----------------------法大大SRC----------------------\033[0m')
    url = 'https://sec.fadada.com/api/notice/page?pageNum=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('法大大', time, title)


def fuiou(number):
    print('\n\033[0;33m-----------------------富友SRC------------------------\033[0m')
    url = 'https://fsrc.fuiou.com/notice/getNoticeData.action'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="page=1&rows=10")
    r_json = json.loads(r.text)
    notice_list = r_json['data']['results']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTimeStr']
        title = notice_list[i]['title']
        print_color('富友', time, title)


def guazi(number):
    print('\n\033[0;33m-----------------------瓜子SRC------------------------\033[0m')
    url = 'https://security.guazi.com/gzsrc/notice/queryNoticesList'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="pageNo=1")
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publishDate'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('瓜子', time, title)


def tal_100(number):
    print('\n\033[0;33m-----------------------好未来SRC----------------------\033[0m')
    url = 'https://src.100tal.com/index.php?m=&c=page&a=index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = ''
        title = notice_list[i].text
        print_color('好未来', time, title)


def yy(number):
    print('\n\033[0;33m-----------------------欢聚时代SRC--------------------\033[0m')
    url = 'https://security.yy.com/center/announcement/list.jsp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    number = number * 2
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number, 2):
        time = notice_list[i].text.split(' ')[0]
        title = notice_list[i + 1].text
        print_color('欢聚时代', time, title)


def focuschina(number):
    print('\n\033[0;33m-----------------------焦点SRC------------------------\033[0m')
    url = 'https://security.focuschina.com/home/announcement.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.anno-lst-date')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.anno-lst-cons')[i].select("a")
        # print(title)
        if len(title) == 2:
            title = title[1].text.strip().replace("置顶", "")
        elif len(title) == 1:
            title = title[0].text.strip().replace("置顶", "")
        print_color('焦点', time, title)


def wps(number):
    print('\n\033[0;33m-----------------------金山办公SRC----------------------\033[0m')
    url = 'https://security.wps.cn/api/src/notices?page=1&size=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['notices']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['ctime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(timeStamp))
        title = notice_list[i]['title']
        print_color('金山办公', time_format, title)


def jd(number):
    print('\n\033[0;33m-----------------------京东SRC------------------------\033[0m')
    url = 'https://security.jd.com/notice/list?parent_type=2&child_type=0&offset=0&limit=12'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['notices']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['CreateTime'].split(' ')[0]
        title = notice_list[i]['Title']
        print_color('京东', time, title)


def jj(number):
    print('\n\033[0;33m-----------------------竞技世界SRC---------------------\033[0m')
    url = 'https://security.jj.cn/notice/notice_list1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    number = number * 2
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number, 2):
        time = notice_list[i + 1].text
        title = notice_list[i].text
        print_color('竞技世界', time, title)


def kuaishou(number):
    print('\n\033[0;33m-----------------------快手SRC------------------------\033[0m')
    url = 'https://security.kuaishou.com/api/user/notice/list'
    headers = {
        'Referer': 'https://security.kuaishou.com/notice',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time'].split(' ')[0]
        title = notice_list[i]['notice_title']
        print_color('快手', time, title)


def alipay(number):
    print('\n\033[0;33m-----------------------蚂蚁金服SRC---------------------\033[0m')
    url = 'https://security.alipay.com/sc/afsrc/notice/noticeList.json?_input_charset=utf-8&_output_charset=utf-8'
    headers = {
        'Referer': 'https://security.alipay.com/home.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['resultAfsrc']['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['noticeTime']
        title = notice_list[i]['title']
        print_color('蚂蚁金服', time, title)


def mogu(number):
    print('\n\033[0;33m-----------------------美丽联合SRC---------------------\033[0m')
    url = 'https://security.mogu.com/bulletin/list?pageNo=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['result']['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['created']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['bulletintitle']
        print_color('美丽联合', time_format, title)


def meituan(number):
    print('\n\033[0;33m-----------------------美团SRC------------------------\033[0m')
    url = 'https://security.meituan.com/api/announce/list?typeId=0&curPage=1&perPage=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['items']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['name']
        print_color('美团', time_format, title)


def meizu(number):
    print('\n\033[0;33m-----------------------魅族SRC------------------------\033[0m')
    url = 'https://sec.meizu.com/announcement/announcement_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.col-md-12')[1].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text.strip().split('\xa0')[0].replace('【', '').replace('】', '')
        title = notice_list[i].text.strip().split('\xa0')[-1]
        print_color('魅族', time, title)


def immomo(number):
    print('\n\033[0;33m-----------------------陌陌SRC------------------------\033[0m')
    url = 'https://security.immomo.com/api/news/blog/?page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = "utf-8"
    r_json = json.loads(r.text)
    notice_list = r_json["results"]
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]["created_at"]
        title = notice_list[i]["title"]
        # title = bs.select('.blog-list')[0].select('h2')[i]
        print_color('陌陌', time, title)


def oppo(number):
    print('\n\033[0;33m-----------------------OPPO SRC-----------------------\033[0m')
    url = 'https://security.oppo.com/cn/be/cn/osrc/FEnotice/findAllNotice'
    headers = {
        'Host': 'security.oppo.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10,"noticeType":""}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['notice_online_time'].split(' ')[0]
        title = notice_list[i]['notice_name']
        print_color('OPPO', time, title)


def pingan(number):
    print('\n\033[0;33m-----------------------平安SRC------------------------\033[0m')
    url = 'https://security.pingan.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('#News_List')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 1].select('span')[0].text.strip().replace('【', '').replace('】', '')
        title = notice_list[i + 1].select('a')[0].text.strip()
        print_color('平安', time, title)


def qianmi(number):
    print('\n\033[0;33m-----------------------千米SRC------------------------\033[0m')
    url = 'http://security.qianmi.com/post'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    number = number * 2
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number, 2):
        time = notice_list[i + 1].text.strip().split(' ')[0]
        title = notice_list[i].text.strip()
        print_color('千米', time, title)


def qunar(number):
    print('\n\033[0;33m-----------------------去哪儿SRC---------------------\033[0m')
    url = 'https://security.qunar.com/notice.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(re.search(r'var jsoncode=(.*);', r.text).group(1))
    notice_list = r_json
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['pubtime'].split(' ')[0]
        title = notice_list[i]['name']
        print_color('去哪儿', time, title)


def rong360(number):
    print('\n\033[0;33m-----------------------融360 SRC---------------------\033[0m')
    url = 'https://security.rong360.com/announce/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='page=1')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['date'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('融360', time, title)


def shuidihuzhu(number):
    print('\n\033[0;33m-----------------------水滴SRC------------------------\033[0m')
    url = 'https://api.shuidihuzhu.com/api/wide/announce/getAnnouncePageList'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['updateTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('水滴', time_format, title)


def sf_express(number):
    print('\n\033[0;33m-----------------------顺丰SRC------------------------\033[0m')
    url = 'http://sfsrc.sf-express.com/notice/getLatestNotices'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="limit=10&offset=0")
    r_json = json.loads(r.text)
    notice_list = r_json['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['modifyTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['noticeTitle']
        print_color('顺丰', time_format, title)


def suning(number):
    print('\n\033[0;33m-----------------------苏宁SRC------------------------\033[0m')
    url = 'https://security.suning.com/ssrc-web/index.jsp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.mod')[2].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text
        title = notice_list[i].select('a')[0].text.strip()
        print_color('苏宁', time, title)


def tencent(number):
    print('\n\033[0;33m-----------------------腾讯SRC------------------------\033[0m')
    url = 'https://security.tencent.com/index.php/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.section-announcement')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.replace('/', '-')
        title = notice_list[i].select('a')[0].text
        print_color('腾讯', time, title)


def tuniu(number):
    print('\n\033[0;33m-----------------------途牛SRC------------------------\033[0m')
    url = 'https://sec.tuniu.com/notice'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    number = number * 2
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number, 2):
        time = notice_list[i + 1].text.strip().split(' ')[0]
        title = notice_list[i].text.strip()
        print_color('途牛', time, title)


def vipkid(number):
    print('\n\033[0;33m-----------------------vipkid SRC----------------------\033[0m')
    url = 'https://security.vipkid.com.cn/notice/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.encoding = r.apparent_encoding
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.page-body-block')[0].select('h3')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.page-body-block')[0].select('p')[i * 2].text.split(' ')[0].replace('年', '-').replace('月',
                                                                                                                '-').replace(
            '日', '')
        title = notice_list[i].text
        print_color('vipkid', time, title)


def vivo(number):
    print('\n\033[0;33m-----------------------vivo SRC-----------------------\033[0m')
    url = 'https://security.vivo.com.cn/api/front/notice/noticeListByPage.do'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNo":1,"pageSize":10,"pageOrder":"","pageSort":""}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updateTime']
        title = notice_list[i]['noticeTitle']
        print_color('vivo', time, title)


def wacai(number):
    print('\n\033[0;33m-----------------------挖财SRC------------------------\033[0m')
    url = 'https://sec.wacai.com/index.php?m=&c=page&a=index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.col-sm-4')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('p')[1].text.split(':')[1].replace('/', '-')
        title = notice_list[i].select('.g-font-size-36--md')[0].text
        print_color('挖财', time, title)


def wanmei(number):
    print('\n\033[0;33m-----------------------完美世界SRC--------------------\033[0m')
    url = 'http://security.wanmei.com/board'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.ovf')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.time')[i].text
        title = bs.select('.ovf')[i].text
        print_color('完美世界', time, title)


def src_163(number):
    print('\n\033[0;33m-----------------------网易SRC------------------------\033[0m')
    url = 'https://aq.163.com/api/p/article/getNoticeList.json'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"offset":0,"limit":20,"childCategory":1}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('网易', time_format, title)


def weibo(number):
    print('\n\033[0;33m-----------------------微博SRC------------------------\033[0m')
    url = 'http://wsrc.weibo.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.lirig')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.lirig')[i].text.split(' ')[0]
        title = bs.select('.lile')[i].text
        print_color('微博', time, title)


def vip(number):
    print('\n\033[0;33m-----------------------唯品会SRC----------------------\033[0m')
    url = 'https://sec.vip.com/notice'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.vsrc-news-nameLink')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.news-date')[0].text
        title = notice_list[i].text
        print_color('唯品会', time, title)


def webank(number):
    print('\n\033[0;33m-----------------------微众银行SRC--------------------\033[0m')
    url = 'https://security.webank.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.list_title')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.list_date')[i].text.replace('/', '-')
        title = notice_list[i].text
        print_color('微众银行', time, title)


def wifi(number):
    print('\n\033[0;33m-----------------------WiFi万能钥匙SRC-----------------\033[0m')
    url = 'https://sec.wifi.com/api/announce'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='pageNo=0&limit=10')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('WiFi万能钥匙', time, title)


def ximalaya(number):
    print('\n\033[0;33m-----------------------喜马拉雅SRC--------------------\033[0m')
    url = 'https://security.ximalaya.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.list_title')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.list_date')[i].text.replace('/', '-')
        title = notice_list[i].text
        print_color('喜马拉雅', time, title)


def xiaomi(number):
    print('\n\033[0;33m-----------------------小米SRC------------------------\033[0m')
    url = 'https://sec.xiaomi.com/api/v1/posts?pageNum=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    notice_list = json.loads(r.text)["data"]["result"]
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]["createTime"]
        title = notice_list[i]["title"]
        print_color('小米', time, title)


def ctrip(number):
    print('\n\033[0;33m-----------------------携程SRC------------------------\033[0m')
    url = 'https://sec.ctrip.com/bulletin/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.csrc-det-body')[0].select('.clearfix')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('.right')[0].text
        title = notice_list[i].select('a')[0].text
        print_color('携程', time, title)


def sina(number):
    print('\n\033[0;33m-----------------------新浪SRC------------------------\033[0m')
    url = 'http://sec.sina.com.cn/Announce/index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.date')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.W_mT20')[0].select('a')[i].text
        print_color('新浪', time, title)


def creditease(number):
    print('\n\033[0;33m-----------------------宜信SRC------------------------\033[0m')
    url = 'http://security.creditease.cn/api/web/announcement/queryList.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='pageNum=1&pageSize=16')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['releaseTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('宜信', time, title)


def unionpay(number):
    print('\n\033[0;33m-----------------------银联SRC------------------------\033[0m')
    url = 'https://security.unionpay.com/notice/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.clear')[0].select('li')
    if number > len(notice_list) - 5:
        number = len(notice_list) - 5
    for i in range(0, number):
        time = '20' + notice_list[i + 5].select('span')[0].text
        title = notice_list[i + 5].select('a')[0].text
        print_color('银联', time, title)


def zto(number):
    print('\n\033[0;33m-----------------------中通SRC------------------------\033[0m')
    url = 'https://sec.zto.com/api/notice/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updated_at'].split('.')[0].replace('T', ' ').split(' ')[0]
        title = notice_list[i]['title']
        print_color('中通', time, title)


def zhaopin(number):
    print('\n\033[0;33m-----------------------智联招聘SRC---------------------\033[0m')
    url = 'https://src.zhaopin.com/page'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.list_title')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.list_date')[i].text.split(' ')[0]
        title = notice_list[i].text
        print_color('智联招聘', time, title)


def zbj(number):
    print('\n\033[0;33m-----------------------猪八戒SRC-----------------------\033[0m')
    url = 'https://security.zbj.com/news/index.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.news-list')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('p')[1].text
        title = notice_list[i].select('h1')[0].text
        print_color('猪八戒', time, title)


if __name__ == '__main__':
    print('''\033[0;33m
   _____ ____  ______   _   __      __  _         
  / ___// __ \/ ____/  / | / /___  / /_(_)_______ 
  \__ \/ /_/ / /      /  |/ / __ \/ __/ / ___/ _ \\
 ___/ / _, _/ /___   / /|  / /_/ / /_/ / /__/  __/
/____/_/ |_|\____/  /_/ |_/\____/\__/_/\___/\___/ 

✔ 爬取各个SRC平台的公告通知
✔ 对2020年发布的活动通知进行红色高亮显示
✔ 【进阶版】将当天发布的公告推送到微信上，结合系统定时任务可实现SRC平台公告监测
✔ 支持的SRC平台[当前共计 55 家]：
360、58、阿里、爱奇艺、百度、贝壳、哔哩哔哩、菜鸟裹裹、滴滴出行、同程旅行、度小满、东方财富、
法大大、富友、瓜子、好未来、欢聚时代、焦点、金山办公、京东、竞技世界、快手、蚂蚁金服、美丽联合、美团、
魅族、陌陌、OPPO、平安、千米、去哪儿、融360、水滴互助、顺丰、苏宁、腾讯、途牛、vipkid、vivo、挖财、完美世界、
网易、微博、唯品会、微众银行、WIFI万能钥匙、喜马拉雅、小米、携程、新浪、宜信、银联、中通、智联招聘、猪八戒

Version：0.3              date: 2020-11-17
Author: TeamsSix          微信公众号：TeamsSix
Blog: teamssix.com        Github: github.com/teamssix
\033[0m''')

    number = 3
    print('当前时间：%s' % time.strftime("%Y-%m-%d", time.localtime()))
    src_360(number)  # 360
    src_58(number)  # 58
    alibaba(number)  # 阿里
    iqiyi(number)  # 爱奇艺
    baidu(number)  # 百度
    ke(number)  # 贝壳
    bilibili(number)  # 哔哩哔哩
    cainiao(number)  # 菜鸟裹裹
    didichuxing(number)  # 滴滴出行
    ly(number)  # 同程旅行
    duxiaoman(number)  # 度小满
    eastmoney(number)  # 东方财富
    fadada(number)  # 法大大
    fuiou(number)  # 富友
    guazi(number)  # 瓜子
    tal_100(number)  # 好未来
    yy(number)  # 欢聚时代
    focuschina(number)  # 焦点
    wps(number)  # 金山办公
    jd(number)  # 京东
    jj(number)  # 竞技世界
    kuaishou(number)  # 快手
    alipay(number)  # 蚂蚁金服
    mogu(number)  # 美丽联合
    meituan(number)  # 美团
    meizu(number)  # 魅族
    immomo(number)  # 陌陌
    oppo(number)  # OPPO
    pingan(number)  # 平安
    qianmi(number)  # 千米
    qunar(number)  # 去哪儿
    rong360(number)  # 融360
    shuidihuzhu(number)  # 水滴互助
    sf_express(number)  # 顺丰
    suning(number)  # 苏宁
    tencent(number)  # 腾讯
    tuniu(number)  # 途牛
    vipkid(number)  # vipkid
    vivo(number)  # vivo
    wacai(number)  # 挖财
    wanmei(number)  # 完美世界
    src_163(number)  # 网易
    try:
        weibo(number)  # 微博
    except:
        pass
    vip(number)  # 唯品会
    webank(number)  # 微众银行
    wifi(number)  # WIFI万能钥匙
    ximalaya(number)  # 喜马拉雅
    xiaomi(number)  # 小米
    ctrip(number)  # 携程
    sina(number)  # 新浪
    creditease(number)  # 宜信
    unionpay(number)  # 银联
    zto(number)  # 中通
    zhaopin(number)  # 智联招聘
    zbj(number)  # 猪八戒
