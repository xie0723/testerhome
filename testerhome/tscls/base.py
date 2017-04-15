# -*- coding: utf-8 -*-


__Author__ = "xiewm"
__Date__ = '2017/3/6 13:12'

import abc
from bs4 import BeautifulSoup as bs4
from .utils import cache_result
from testerhome.exception import NotExistUrlException


class Base(object):
    def __init__(self, session):
        self._session = session
        self.username = None
    
    # 获取接口返回数据
    @property
    @cache_result
    def get_data(self):
        url = self.build_url()
        try:
            res = self._session.request(self.method,
                                        url=url,
                                        params=self.build_params,
                                        data=self._build_data,
                                        )
        except Exception as e:
            return e
        else:
            if res.status_code == 404:
                raise NotExistUrlException(url)
            
            return res
    
    @abc.abstractmethod
    def build_url(self):
        return ''
    
    @property
    def build_params(self):
        return None
    
    @property
    def method(self, method=None):
        return method if method else 'GET'
    
    @property
    def _build_data(self):
        return None
    
    @property
    def get_soup(self):
        html = self.get_data
        soup = bs4(html.text, 'html.parser')
        return soup
    
    @property
    def get_json_data(self):
        json_data = self.get_data.json()
        return json_data
