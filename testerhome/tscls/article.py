# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/9 11:29'

from testerhome.tscls.base import Base
from testerhome.tsclient.settings import ARTICLE_URL
from testerhome.tscls.utils import attrs_data


class Article(Base):
    def __init__(self, data_id, session):
        super(__class__, self).__init__(session)
        self.data_id = data_id

    def build_url(self):
        return ARTICLE_URL.format(self.data_id)

    # 获取文章内容
    @property
    @attrs_data('div', {'class': 'panel-body markdown markdown-toc'})
    def topic_text(self):
        return ''

    # 获取topic创建时间
    @property
    @attrs_data('abbr', {'class': 'timeago'})
    def topic_age(self):
        return ''

    @property
    @attrs_data('title')
    def topic_title(self):
        return ''

    # 获取文章阅读量
    @property
    def topic_volume(self):
        soup = self.get_soup
        infos = soup.find('div', {'class': 'info'}).get_text(strip=True)
        volume = [info.strip() for info in infos.split('·')][-1]

        return volume

    # 获取文章作者
    @property
    @attrs_data('a', {'data-author': "true", 'class': 'user-name'})
    def topic_auth(self):
        return ''

    # 获取文章最后回复者
    @property
    def topic_last_reply(self):
        soup = self.get_soup
        infos = soup.find('div', {'class': 'info'}).get_text(strip=True)
        last_reply = [info.strip() for info in infos.split('·')][2]

        return last_reply

    # 获取文章点赞数 未完成
    def topic_like_numb(self):
        soup = self.get_soup
        return soup

    def __str__(self):
        return 'username:{}'.format(self.username)
