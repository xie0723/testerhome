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

# 属性提取方法抽象成装饰器
def attrs_data(name=None, attrs={}, strip=False, **kw):
    def decorate(func):
        def wrapper(self, *args, **kwargs):
            soup = self.get_soup
            attr = soup.find(name, attrs, **kw).get_text(strip=strip)
            func(self, *args, **kwargs)
            return '{}:'.format(func.__name__) + attr
        return wrapper
    return decorate
