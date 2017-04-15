# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/2/28 16:34'

from bs4 import BeautifulSoup
import jieba.analyse
from collections import Counter
from functools import wraps
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import os
from time import sleep
from random import randint

# 伪造请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko)'
                  ' Chrome/56.0.2924.87 Safari/537.36'
}

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 获取文件路径
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


# 缓存首次请求数据
def cache_result(func):
    cache = {}

    @wraps(func)
    def wrapper(uri):
        if uri not in cache:
            cache[uri] = func(uri)
        return cache[uri]

    return wrapper


# 提取网页内容
@cache_result
def extract_text(uri):
    try:
        r = requests.get(uri, verify=False, headers=headers)
    except Exception as e:
        print(e)
        return None
    else:
        if r.status_code == 200:
            print(u'{}:请求成功'.format(uri))
            soup = BeautifulSoup(r.text, 'html.parser')
            return soup
        else:
            print("{}:网页不存在".format(uri))
            print('**********************************************')
            return None


# 提取文章标题
def extract_title(soup):
    try:
        title = soup.find('title').get_text()
    except:
        return None
    else:
        return title


# 提取文章创建时间
def extract_time_age(soup):
    try:
        time_age = soup.find('abbr').get_text()
    except Exception as e:
        print(e)
        return None
    else:
        return time_age


# 判断创建时间，存储到对应txt
def save_txt(time_age, article, filepath):
    if time_age:
        try:
            with open(filepath, 'a+', encoding='utf-8') as fp:
                fp.write(article + '\n')
        except Exception as e:
            print(e)
            return None
        else:
            print(u'保存成功')


# 提取文章正文
def extract_article(soup):
    try:
        article = soup.find('article').get_text()
    except Exception as e:
        print(e)
        return None
    else:
        return article


# 计算词频
def word_frequency(text):
    words = (word for word in jieba.cut(text, cut_all=False) if len(word) >= 2)
    c = Counter(words)

    for name, numb in c.most_common(30):
        print(name, numb)


# 计算词语权重
def word_weight(text):
    tags = jieba.analyse.extract_tags(text, topK=30, withWeight=True)

    for item in tags:
        print(item[0] + '\t' + str(int(item[1] * 1000)))


# 保存文章内容
def save_text(article, filepath):
    try:
        with open(filepath, 'a+', encoding='utf-8') as fp:
            fp.write(article + '\n')
    except Exception as e:
        print(e)
        return None
    else:
        print(u'保存成功')


# 读取数据
def read_text(filepath):
    try:
        with open(filepath, encoding='utf-8') as fp:
            return fp.read()
    except Exception as e:
        print(e)
        return None


# 爬取数据
def spider(start, stop):
    print(u'开始爬取网页' + '\n')

    for page in range(start, stop):
        tm = randint(3, 8)
        url = 'https://testerhome.com/topics/{}'.format(page)
        soup = extract_text(url)
        if soup:
            article = extract_article(soup)
            save_text(article, './/2017_article.txt')
            print(u'休眠{}秒'.format(tm))
            sleep(tm)
            print('__________________________________________')
        else:
            pass


# 爬取数据
def spider_tsh(start, stop):
    print(u'开始爬取网页' + '\n')

    while start < stop:
        url = 'https://testerhome.com/topics/{}'.format(start)
        soup = extract_text(url)
        if soup:
            article = extract_article(soup)
            save_text(article, './/2017_article.txt')
            start += 1
        else:
            pass


if __name__ == '__main__':
    # print(extract_title(extract_text(url)))
    # print(extract_time_age(extract_text(url)))
    # print(type(extract_article(extract_text(url))))
    # 获取权重
    # word_weight(read_text(PATH('./2017_article.txt')))
    # 获取词频
    # word_frequency(read_text(PATH('./2017_article.txt')))
    # 读取数据
    # with open('.//2017_article.txt') as fp:
    #     text = fp.read()
    #     word_weight(text)
    # print(PATH('2017_article.txt'))
    # 爬取数据
    for page in range(5005, 7000):
        url = 'https://testerhome.com/topics/{}'.format(page)
        save_text(extract_article(extract_text(url)))
    spider_tsh(start=4554, stop=4557)
    spider(4554, 5000)
    # 获取文章创建时间
    # print(extract_time_age(extract_text('https://testerhome.com/topics/7756')))
