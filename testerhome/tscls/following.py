# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/8 13:55'

from testerhome.settings import (FOLLOWING_URL)
from testerhome.tscls.base import Base


class Following(Base):
    def __init__(self, session, username):
        super(__class__, self).__init__(session)
        self.username = username

    def build_url(self):
        return FOLLOWING_URL.format(self.username)

    # 正在关注数量
    @property
    def following_numb(self):
        soup = self.get_soup
        numbs = soup.find('a', {'class': "counter", 'href': "/{}/following"
                          .format(self.username)}).get_text()
        return '正在关注数量:{}'.format(numbs)

    # 正在关注detail
    @property
    def following_detail(self):
        """
        返回一个生成器.
        :return:
        """
        soup = self.get_soup
        for tag in soup.find_all('a', {'class': 'user-name'}):
            yield (tag.get_text(), tag.attrs['data-name'])

    def __str__(self):
        return 'username:{}'.format(self.username)
