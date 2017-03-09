# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/9 11:29'

from testerhome.tscls.base import Base


class Article(Base):
	def __init__(self):
		super(__class__, self).__init__()

	# 获取文章内容
	def topic(self):
		pass

	# 获取文章创建时间
	def topic_time(self):
		pass

	# 获取文章 标题
	def topic_title(self):
		pass

	# 获取文章作者对象
	def topic_author(self):
		pass

	#