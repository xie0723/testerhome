# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/9 11:29'

from testerhome.tscls.base import Base
from testerhome.tsclient.settings import ARTICLE_URL


class Article(Base):
    def __init__(self, data_id, session):
        super(__class__, self).__init__(session)
        self.data_id = data_id

    def build_url(self):
        return ARTICLE_URL.format(self.data_id)

    # 获取文章内容
    @property
    def topic_text(self):
        soup = self.get_soup
        txt = soup.find('div', {'class': "panel-body markdown markdown-toc"}).get_text()

        return '文章内容：{}'.format(txt)

    # 获取topic创建时间
    @property
    def topic_age(self):
        soup = self.get_soup
        time_age = soup.find('abbr', {'class': 'timeago'}).get_text()

        return '文章创建于：{}'.format(time_age)

    # 获取topic标题
    @property
    def topic_title(self):
        soup = self.get_soup
        title = soup.find('title').get_text()

        return '文章标题：{}'.format(title)

    # 获取文章阅读量
    @property
    def topic_volume(self):
        soup = self.get_soup
        infos = soup.find('div', {'class': 'info'}).get_text(strip=True)
        volume = [info.strip() for info in infos.split('·')][-1]

        return volume

    # 获取文章作者
    @property
    def topic_auth(self):
        soup = self.get_soup
        auth = soup.find('a', {'data-author': "true", 'class': 'user-name'}).get_text()

        return auth

    # 获取文章最后回复者
    @property
    def topic_last_reply(self):
        soup = self.get_soup
        infos = soup.find('div', {'class': 'info'}).get_text(strip=True)
        last_reply = [info.strip() for info in infos.split('·')][2]

        return last_reply

    # 获取文章点赞数
    def topic_like_numb(self):
        soup = self.get_soup
        return soup

    def __str__(self):
        return 'username:{}'.format(self.username)
