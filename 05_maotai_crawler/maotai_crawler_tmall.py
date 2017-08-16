# coding: utf-8

# 茅台网上销售渠道（http://www.china-moutai.com/xinwen/2014/658.html）：
#
#     1、茅台商城　https://www.emaotai.cn;
#
# 　　2、天猫茅台官方旗舰店　http://maotai.tmall.com;
#
# 　　3、国酒茅台阿里巴巴旗舰店　http://emaotai.1688.com;
#
# 　　4、工行融e购:　茅台商城官方旗舰店 ;
#
# 　　5、建行善融商城:　茅台商城官方旗舰店 ;
#
# 　　6、国美在线:　茅台商城官方旗舰店 ;
#
# 　　7、苏宁易购:　茅台商城官方旗舰店 ;
#
# 　　8、京东商城:　茅台商城官方旗舰店 ;
#
# 　　另外，我公司授权"京东商城"在其官网 www.jd.com 销售贵州茅台酒股份有限公司产品。

# 茅台天猫爬虫https://maotai.tmall.com
#
# 包含商品名、价格、销量

import requests
import time
from bs4 import BeautifulSoup
import csv, codecs
from tqdm import tqdm
import re


tmall_url = 'https://maotai.tmall.com/i/asynSearch.htm?_ksTS=1502379704428_364&callback=jsonp365&mid=w-15656860787-0&wid=15656860787&path=/search.htm&search=y&spm=a1z10.1-b-s.w5003-15656860766.41.4c03279NWdbir&scene=taobao_shop'
data_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

headers = {
    'User-Agent': 'Mozilla/5.0'
}


def get_data(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    print(soup)
    contents = soup.find_all('dd')
    data = set()
    for i in contents:
        try:
            title = i.find('a').string.strip()
            prices = i.find('div')
            price_ = prices.find_all('span')
            price = price_[1].string.strip()
            sell_count = price_[2].string.strip()
            product_info = (data_date, title, price, sell_count)
            data.add(product_info)
        except:
            pass
    return data


def save_data(data):
    with codecs.open('maotai_tmall.csv', 'a', newline='', encoding='utf_8_sig') as f:
        csv_file = csv.writer(f, dialect='excel')
        for i in tqdm(data):
            csv_file.writerow(i)
    return 


if __name__ == '__main__':
    data = get_data(tmall_url)
    save_data(data)

