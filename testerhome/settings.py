# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/3 15:04'

# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': '*/*;q=0.5, text/javascript, application/javascript, '
              'application/ecmascript, application/x-ecmascript',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
}

# 主域名
DOMAIN_URL = 'https://testerhome.com/'

# 登录接口
LOGIN_URL = DOMAIN_URL + 'account/sign_in'

# 登录
LOGIN_DATA = {
    'utf8': '✓',
    'user[login]': '',
    'user[password]': '',
    'user[remember_me]': 0,
    'commit': '登录'
}

# 关注
FOLLOWERS_URL = DOMAIN_URL + '{}/followers'

# 正在关注
FOLLOWING_URL = DOMAIN_URL + '{}/following'

# 收藏
FAVORITES_URL = DOMAIN_URL + '{}/favorites'

# 文章
ARTICLE_URL = DOMAIN_URL + 'topics/{}'

# 搜索
SEARCH_URL = DOMAIN_URL + 'search?{}'