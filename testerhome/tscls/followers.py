# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/4 16:41'
from testerhome.tsclient.settings import (FOLLOWERS_URL)
from testerhome.tscls.base import Base


class Followers(Base):
	def __init__(self, session, username):
		super(__class__, self).__init__(session)
		self.username = username

	def build_url(self):
		return FOLLOWERS_URL.format(self.username)

	# 关注者数量
	@property
	def followers_numb(self):
		soup = self.get_soup
		numbs = soup.find('a', {'class': "counter", 'href': "/{}/followers"
		                  .format(self.username)}).get_text()
		return u'关注者数量:{}'.format(numbs)

	# 关注detail
	@property
	def followers_detail(self):
		"""
		返回一个生成器,提高性能。
		:return:
		"""
		soup = self.get_soup
		tags = soup.find_all('a', {'class': 'user-name'})

		for tag in tags:
			yield (tag.get_text(), tag.attrs['data-name'])

	def __str__(self):
		return 'username:{}'.format(self.username)
