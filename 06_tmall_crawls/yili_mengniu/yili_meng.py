# coding: utf-8
import requests
from bs4 import BeautifulSoup
import time
import csv, codecs
from tqdm import tqdm


yili_tmall_url = 'https://yili.tmall.com/i/asynSearch.htm?_ksTS=1502629222912_430&callback=jsonp431&mid=w-15521111965-0&wid=15521111965&path=/search.htm&search=y&spm=a1z10.1-b-s.w14191084-15521286924.2.35554cfcU32gQM&scene=taobao_shop'
mengniu_tmall_url = 'https://mengniusp.tmall.com/i/asynSearch.htm?_ksTS=1502632364116_364&callback=jsonp365&mid=w-14719154061-0&wid=14719154061&path=/search.htm&search=y&spm=a1z10.1-b-s.w10195673-14719154007.6.tpgREO&orderType=null&viewType=grid&keyword=null&lowPrice=null&highPrice=null'
headers = {
    'User-Agent': 'Mozilla/5.0'
}
data_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))


def get_page(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html5lib')
    contents = soup.find_all('dd')
    data = set()
    for i in tqdm(contents):
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

        
def save_data(name, data):
    with open('%s_tmall.csv' % (name), 'a', encoding='utf_8_sig') as f:
        csv_file = csv.writer(f, dialect='excel')
        for i in tqdm(data):
            csv_file.writerow(i)
    return   
    
        
if __name__ == '__main__':
    data = get_page(yili_tmall_url)
    save_data('yili', data)
    data = get_page(mengniu_tmall_url)
    save_data('mengniu', data)
    
