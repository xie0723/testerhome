# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/7 16:54'


class TesterHomeException(Exception):
	pass


# 获取token 值失败异常类
class GetTokenValueFailed(TesterHomeException):
	def __init__(self, msg='get token fail'):
		self.msg = msg

	def __repr__(self):
		return self.msg

	__str__ = __repr__


# 登录失败异常类
class LoginTesterHomeFailed(TesterHomeException):
	def __init__(self, username, password=None, msg='Login Failed'):
		self.msg = msg
		self.username = username
		self.password = password

	def __repr__(self):
		return '{},{},{}'.format(self.msg, self.username, self.password)

	__str__ = __repr__


# 需要登录态的方法，未登录，异常类
class NeedLoginException(TesterHomeException):
	def __init__(self, msg):
		self.msg = msg

	def __repr__(self):
		return 'Need login to use the [{self.msg}] method.'.format(self=self)

	__str__ = __repr__


# 未登录and 未提供username 异常类
class NeedLoginOrUsernameException(TesterHomeException):
	def __init__(self, msg):
		"""
		调用某属性,当前未登录

		:param str|unicode msg: 当前试图调用的方法名
		"""
		self.msg = msg

	def __repr__(self):
		return 'login:{} or {}'.format(self.msg, u'请提供用户名')

	__str__ = __repr__


# 请求不存在的网页异常类
class NotExistUrlException(TesterHomeException):
	def __init__(self, msg):
		self.msg = msg

	def __repr__(self):
		return 'Url not exist :{}'.format(self.msg)

	__str__ = __repr__