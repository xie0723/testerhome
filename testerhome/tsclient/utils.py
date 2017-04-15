# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/4 16:11'

from functools import wraps
from testerhome.exception import *


# 强制拥有登录态
def login_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_login():
            return func(self, *args, **kwargs)
        else:
            raise NeedLoginException(self.username)

    return wrapper


# 单例,保证实例唯一
def singleton(cls):
    instance = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapper


# 判断用户是否登陆，若没登陆，判断是否提供了username
def is_username(func):
    @wraps(func)
    def wrapper(self, username, *args, **kwargs):
        try:
            func(self, username, *args, **kwargs)
            
        except NeedLoginOrUsernameException(self.is_login) as e:
            return e
        else:
            return func(self, username, *args, **kwargs)
    return wrapper
