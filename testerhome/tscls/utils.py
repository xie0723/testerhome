# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/6 12:48'

from functools import wraps


# 缓存首次请求数据
def cache_result(func):
	cache = {}

	@wraps(func)
	def wrapper(self, *args, **kwargs):
		uri = self.build_url()
		if uri not in cache:
			cache[uri] = func(self, *args, **kwargs)
		return cache[uri]

	return wrapper
