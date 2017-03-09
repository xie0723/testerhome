# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/8 13:55'
from testerhome.tscls.base import Base
from testerhome.tsclient.settings import (FAVORITES_URL)


class FAVORITES(Base):
    def __init__(self, session, username):
        super(__class__, self).__init__(session, username)

    def build_url(self):
        return FAVORITES_URL.format(self.username)

    # 收藏数量
    @property
    def favorites_numb(self):
        soup = self.get_soup
        numb = soup.find('a', {'class': "counter", 'href': "/{}/favorites"
                         .format(self.username)}).get_text()
        return u'收藏数量:{}'.format(numb)

    # 收藏detail
    @property
    def favorites_detail(self):
        """
        返回一个生成器,节省内存。
        :return:
        """
        soup = self.get_soup
        for tag in soup.find_all('td', {'class': 'title'}):
            if tag.a:
                yield tag.a.get_text(), tag.a['href']
            else:
                pass

    def __str__(self):
        return 'username:{}'.format(self.username)
