import requests
import json
from bs4 import BeautifulSoup
import schedule
import time
import csv
from xlutils.copy import copy
url = 'https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6'
with open('1.csv', 'a+', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['时间', '排名', '热度', '内容'])
def run():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
    }
    cookie = {
        'Cookie':'SINAGLOBAL=1274470012772.2551.1638794389785; _s_tentry=-; Apache=42164598483.33409.1645500325306; ULV=1645500325315:2:1:1:42164598483.33409.1645500325306:1638794389794; login_sid_t=5c62e5b3e913a8539fa1bdd87eed56e0; cross_origin_proto=SSL; SUB=_2A25PELk4DeRhGeRJ7lYW-SvKzj-IHXVsZ63wrDV8PUNbmtAKLWL5kW9NUkP2jlDztR_Jf5or_vkd_ceiPeIWKWFO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFjjxSxM4-pj_zfb3EQk.Wn5JpX5o275NHD95QES0-XS0.fSo-0Ws4DqcjVi--ciKn4iKyFi--ciKLhi-iWi--NiK.Xi-2Ri--ciKnRi-zNeoMfShM4SKqfe7tt; ALF=1646134248; SSOLoginState=1645529448; wvr=6; webim_unReadCount=%7B%22time%22%3A1645529470137%2C%22dm_pub_total%22%3A64%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A1%2C%22allcountNum%22%3A108%2C%22msgbox%22%3A0%7D; WBStorage=09a9c7be|undefined'
    }
    response = requests.get(url, headers=header, cookies=cookie)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('td', class_='td-02')
    time_stamp = time.strftime('%Y/%m/%d %H:%M', time.localtime(time.time()))  # 时间戳

    for i, item in enumerate(items[1:11]):
        result = []
        rank = '第{0}名'.format(i+1)     # 微博排名
        num = str(item.find('span')).replace('<span>', '').replace('</span>', '')  # 微博热度
        title = item.find('a').text  # 微博内容
        result.append(time_stamp)
        result.append(rank)
        result.append(num)
        result.append(title)
        print(result)
        with open('1.csv', 'a+',newline='') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(result)
    print(time_stamp)
run()
schedule.every(1).minutes.do(run)
while True:
    schedule.run_pending()
