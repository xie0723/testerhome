# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/4 11:51'

import os
from selenium import webdriver
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
js_path = (PATH('phantomjs.exe'))

driver = webdriver.PhantomJS(js_path)

driver.get('https://testerhome.com/account/sign_in')

driver.find_element_by_id('user_login').send_keys('xie_0723')
driver.find_element_by_id('user_password').send_keys('Xie151007')

driver.find_element_by_name('commit').click()

all_cookies = driver.get_cookies()

cookies = {'httponly': 'False', 'secure': 'False', 'domain': '.testerhome.com', 'path': '/'}

for cookie in all_cookies:
    if cookie.get('name') == '_homeland_session':
        cookies['_homeland_session'] = cookie['value']
    elif cookie.get('name') == 'user_id':
        cookies['user_id'] = cookie['value']

s = requests.Session()
s.verify = False
print('开始登陆')
s.get('https://testerhome.com/', cookies=cookies)
