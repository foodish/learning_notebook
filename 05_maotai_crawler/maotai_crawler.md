1. 所需的python库：requests, BeautifulSoup, lxml(或html5lib), tqdm
2. maotao_info数据来自茅台商城，对应的程序为maotai_crawler.py

2.1 csv文件各列依次是：时间，商品名，商品编号，品牌，价格，浏览量，销量

2.2 时间格式默认精确到秒，精确到日时改为data_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))

3. maotao_tmall数据来自天猫旗舰店，对应的程序为maotai_crawler_tmall.py

2.1 csv文件各列依次是：时间，商品名，价格，销量

2.2 时间格式默认精确到日

4.emaotai_analysis.ipynb;tmall_analysis.ipynb分别为茅台商城和天猫数据的分析

5.jd_comments.ipynb是抓取京东茅台旗舰店53度飞天的评论数据进行分析

6.查询数据.ipynb用于查询茅台商城每天的53度茅台和生肖茅台酒数据
