# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/16 15:12'

from .base import Base

class Search(Base):
    def __init__(self, session):
        super(__class__, self).__init__(session)

    def search(self):
        pass

