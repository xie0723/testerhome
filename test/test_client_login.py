# -*- coding: utf-8 -*-
__Author__ = "xiewm"
__Date__ = '2017/3/9 11:03'

import unittest
from testerhome.tsclient.client import *


class TesterHomeClientTest(unittest.TestCase):
    def setUp(self):
        self.client = TesterHomeClient()

    def test_username_is_no_exist(self):

        self.assertEqual(0, self.client.login('no_exist_usernma', '1111'))

    def test_username_or_psw_error(self):

        self.assertEqual(-1, self.client.login('xie0723', '1111'))

    def test_login_success(self):
        self.assertTrue(self.client.login('xie0723', 'xie0723'))

    def test_username_or_psw_is_string(self):
        self.assertTrue(self.client.login('1112222', '222222'))

    def tearDown(self):
        pass
