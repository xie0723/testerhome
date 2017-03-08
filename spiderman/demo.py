# coding=utf-8
import requests
from bs4 import BeautifulSoup
import jieba.analyse
from collections import Counter

# 请求获取网页内容
html = requests.get('https://testerhome.com/topics/7659')

# bs4 解析内容
soup = BeautifulSoup(html.text, 'html.parser')

# 获取title标签下的内容
title = soup.find('title').get_text()
print(title)

# 文章发布时间
timeago = soup.find('abbr').get_text()
print(timeago)

# 获取article标签内的所有内容
article = soup.find('article').get_text()

# print article

# 过滤词
jieba.analyse.set_stop_words('D:\coding\study_python\stop_words.txt')

# 开始分词， 统计权重
# tags = jieba.analyse.extract_tags(article, topK=50, withWeight=True)
#
# for item in tags:
# 	print(item[0] + '\t' + str(int(item[1] * 1000)))

# 统计次数
seg_list = jieba.cut(article, cut_all=False)
words = [word for word in seg_list if len(word) >= 2]
c = Counter(words)
for item, numb in c.most_common(30):
	print(item, numb)
