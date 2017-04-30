# -*- coding: utf-8 -*-
__author__ = "xiewm"
__date__ = '2017/3/3 15:04'

# 请求头

from fake_useragent import FakeUserAgent

def get_user_agent():
    ua = FakeUserAgent()
    return ua.random

headers = {
    'user-agent': get_user_agent(),
    'accept': '*/*;q=0.5, text/javascript, application/javascript, '
              'application/ecmascript, application/x-ecmascript',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'x-requested-with': 'xmlhttprequest',
}

# 主域名
domain_url = 'https://testerhome.com/'

# 登录接口
login_url = domain_url + 'account/sign_in'

# 登录
login_data = {
    'utf8': '✓',
    'user[login]': '',
    'user[password]': '',
    'user[remember_me]': 0,
    'commit': '登录'
}

# 关注
followers_url = domain_url + '{}/followers'

# 正在关注
following_url = domain_url + '{}/following'

# 收藏
favorites_url = domain_url + '{}/favorites'

# 文章
article_url = domain_url + 'topics/{}'

# 搜索
search_url = domain_url + 'search?{}'

