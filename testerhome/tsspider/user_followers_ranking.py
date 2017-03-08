# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/6 15:05'
from operator import itemgetter
from random import randint
from time import sleep

from bs4 import BeautifulSoup as bs4
from testerhome.tsclient.client import TesterHomeClient


class UserFollowersRank(TesterHomeClient):
	def __init__(self):
		super(UserFollowersRank, self).__init__()
		self.client = TesterHomeClient()
		self.top_100_user = 'https://testerhome.com/users'

	@property
	def get_soup(self):
		res = self.session.get(self.top_100_user)
		soup = bs4(res.text, 'html.parser')
		return soup

	# 获取top100 用户名
	def get_top_100_user(self):
		soup = self.get_soup
		tags = soup.find_all('a', {'class': 'user-name'})

		for tag in tags:
			yield (tag.string, tag.attrs['data-name'])

	# 排序
	def followers_rank(self):
		for name, zname in self.get_top_100_user():
			tm = randint(2, 9)
			sleep(tm)
			numb = self.client.followers(name).followers_numb
			yield (name, zname, int(numb))
			# yield (u'昵称:{} 名字：{}  关注者:{}'.format(name, zname, numb))


if __name__ == '__main__':
	rank = UserFollowersRank()
	datas = sorted(rank.followers_rank(), key=itemgetter(-1))
	for name ,zname ,numb in datas:
		print(u'昵称:{} 名字：{}  关注者:{}'.format(name, zname, numb))
