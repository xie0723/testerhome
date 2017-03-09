# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/3 14:37'

import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from testerhome.tsclient.settings import (DOMAIN_URL, LOGIN_URL, HEADERS, LOGIN_DATA)
from testerhome.exception import (GetTokenValueFailed, LoginTesterHomeFailed)
from testerhome.tsclient.utils import (need_login)


class TesterHomeClient(object):
    def __init__(self, flag=False, username=None):
        self._session = requests.Session()

        self.headers = HEADERS
        # 移除安全认证
        self._session.verify = False
        # 禁用安全请求警告
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.flag = flag
        self.username = username

    # 获取token
    @property
    def get_csrf_token(self):
        try:
            text = self._session.get(LOGIN_URL).text
        except Exception as e:
            return e
        else:
            soup = BeautifulSoup(text, 'html.parser')
            tags = soup.find_all('meta')

        for tag in tags:
            attr = tag.attrs
            if attr.get('name') == 'csrf-token':
                return attr.get('content')
        else:
            raise GetTokenValueFailed

    # 登陆
    def login(self, username: object, password: object) -> object:
        """

          :param username: 登录名
          :param password: 登录密码
          :return: 登录成功，返回登录名，未登录成功返回对应失败状态
          """
        LOGIN_DATA['user[login]'] = username
        LOGIN_DATA['user[password]'] = password

        # 添加token 到request headers
        self.headers['X-CSRF-Token'] = self.get_csrf_token

        try:
            r1 = self._session.post(LOGIN_URL, data=LOGIN_DATA, headers=self.headers)
            r2 = self._session.get(DOMAIN_URL)

        except Exception as e:
            return False, e

        else:
            if u'没有该用户' in r1.text:
                print(r1.text)
                return 0
            if u'帐号或密码错误' in r1.text:
                print(r1.text)
                return -1
            if username in r2.text:
                self.flag = True
                print(u'登录成功')
                return self.flag
            else:
                raise LoginTesterHomeFailed(username, password)
        finally:
            self.username = username

    # 设置代理
    def set_proxy(self, proxy=None):
        """
          :param proxy: :
                    proxies = { "http": "http://10.10.1.10:3128",
                               "https": "http://10.10.1.10:1080", }
          """

        if proxy is None:
            self._session.proxies.clear()
        else:
            self._session.proxies.update({'http': proxy, 'https': proxy})

    # 登录态
    def is_login(self):
        return self.flag

    # 关注者
    def followers(self, username=None):
        username = username or self.username

        from testerhome.tscls.followers import Followers
        return Followers(self._session, username)

    # 正在关注者
    def following(self, username=None):
        username = username or self.username

        from testerhome.tscls.following import Following
        return Following(self._session, username)

    # 收藏
    def favorites(self, username):
        username = username or self.username

        from testerhome.tscls.favorites import FAVORITES
        return FAVORITES(self._session, username)

    # 其他模块调用
    @property
    def session(self):
        return self._session

    # 获取登录用户的信息
    @need_login
    def me(self):
        from testerhome.tscls.me import Me
        return Me()


if __name__ == '__main__':
    th_client = TesterHomeClient()
    # print(th_client.get_csrf_token) # token  值获取
    th_client.login('xie0723', 'xie0723')  # 登录

    # print(client.is_login()) # 判断是否登录态
    # print(th_client.followers('seveniruby').followers_numb)  # 关注者数量
    # detail = th_client.followers('seveniruby').followers_detail
    # # for name, zname in detail:  # 关注者detail
    #      print(u'昵称:{:<16} 名字：{:<15}'.format(name, zname))
    # for title, id_ in th_client.favorites('xie_0723').favorites_detail:
    #     pprint(u'{:<25},ID:{}'.format(title, id_))
    # print(th_client.following('xie_0723').following_numb)
    # for name, zname in th_client.following('xie_0723').following_detail:
    #     print(u'昵称:{:<16} 名字：{:<15}'.format(name, zname))
