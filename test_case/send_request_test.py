#!/usr/bin/env python
# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/7 2:08 上午
# @Author  : jhyfugug
# @File    : send_request_test.py
import pytest
import requests


class TestSendRequest:

    def test_post_token(self):
        # 通过登录获取到token
        url = 'https://api-saas.wemew.com/chagoi-auth-service/oauth/token'
        data = {
            "Content-Type": "application/x-www-form-urlencoded",
            "grant_type": "password",
            "username": "18080498443",
            "password": "B60118A697BA46AE",
            "client_id": "admin",
            "client_secret": "A73D5D6F15B70548F35E53EE9C08A710"
        }
        rep = requests.post(url, data=data)
        print(rep.json())
        print(rep.json()['data']['token'])


if __name__ == '__main__':
    pytest.main(['-vs'])
