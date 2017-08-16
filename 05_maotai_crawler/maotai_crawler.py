
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

# 1.茅台商城爬虫https://www.emaotai.cn
# 
# 包含商品名、品牌、价格、浏览数、已销售数、库存信息等

# In[178]:

import requests
import time
from bs4 import BeautifulSoup
import csv, codecs
from tqdm import tqdm


# In[179]:

base_url = 'https://www.emaotai.cn/'
base_urls = ['https://www.emaotai.cn/browse/category-60.htm?flavortype=&pageindex=' + str(i) for i in range(1, 5)]
data_date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

headers = {
    'User-Agent': 'Mozilla/5.0'
}


# In[180]:

def get_page(url):
    r = requests.get(url, headers=headers)
    # soup = BeautifulSoup(r.text, 'lxml') #需要lxml模块
    soup = BeautifulSoup(r.text, 'html5lib') #html5lib为pythonista上的解析器
    content = soup.find('div', {'class':'category_pro_list'})
    urls = set()
    for i in content.find_all('a'):
        if 'href' in i.attrs:
            urls.add(base_url + i.attrs['href'])
    return urls


# In[181]:

def get_product_info(url):
    r = requests.get(url, headers=headers)
    # soup = BeautifulSoup(r.text, 'lxml')
    soup = BeautifulSoup(r.text, 'html5lib')
    content = soup.find('div', class_="product_parameter")

    title = content.find('span').get_text()  #商品名
    item = content.find('tr', class_="product_para2")
    item_2 = item.find_all('span')
    list_1 = []
    for i in item_2:
        list_1.append(i.get_text())
    product_id = list_1[0]  #商品编号
    brand = list_1[1]  #品牌
    price = list_1[2]  #价格
    view_count = list_1[6][:-2]  #浏览次数
    sell_count = list_1[9]  #已售出量

    item_3 = content.find('div', class_="product_para_num")
    s_1 = item_3.get_text().strip()
    if '真品保证' in s_1:
        store_count = '仅供展示'
    else:
        store_count = s_1.split()[-1][4:][:-1]  #库存数
    
    product_info = (data_date, title, product_id, brand, price, view_count, sell_count, store_count)
    return product_info


# In[182]:

product_urls = set()
for i in tqdm(base_urls):
    urls = get_page(i)
    product_urls = product_urls | urls


# In[183]:

data = []
for url in tqdm(product_urls):
    prooduct_info = get_product_info(url)
    data.append(prooduct_info)


# In[184]:

with codecs.open('maotai_info.csv', 'a', encoding='utf_8_sig') as f:
    csv_file = csv.writer(f, dialect='excel')
    for i in tqdm(data):
        csv_file.writerow(i)


# In[ ]:



