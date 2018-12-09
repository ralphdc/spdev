#!/usr/bin/env python3

from config import Config
from app import Log
import requests
import sys

class Parent():

    def __init__(self, cookies):
        try:
            self.init_url = Config.ren_index_url
            self.login_url = Config.login_url
            self.login_token_url = Config.login_ajax_token_url
            self.groups_data_url = Config.groups_data_url
            self.good_friend_url = Config.good_friend_url
            self.username = Config.username
            self.password = Config.password
        except Exception as e:
            Log.get_logger().exception(e)

        self.parse_cookie(cookies)


    def http_get(self, url, headers, params=None, cookies=None, json=None):
        try:
            response = requests.get(url, headers=headers, cookies=cookies, params=params)
        except Exception as e:
            Log.get_logger().exception(e)
            sys.exit(1)
        Log.get_logger().info("send http with GET method detected>>>>>>>>>>>>>>>>>>>>>>>>>")
        Log.get_logger().info("[ response code ]: %s " % response.status_code)
        Log.get_logger().info("[ response text ]: %s " % response.text.encode('unicode_escape').decode('utf-8'))
        Log.get_logger().info("[ response cookies ]: %s " % response.cookies)
        Log.get_logger().info("[ response headers ]: %s " % response.headers)

        return response.status_code, response.json() if json else response.text, response.cookies

    def http_post(self, url, headers, data=None, cookies=None, json=None):
        try:
            response = requests.post(url, headers=headers, cookies=cookies, data=data)
        except Exception as e:
            Log.get_logger().exception(e)

        Log.get_logger().info("send http with POST method detected>>>>>>>>>>>>>>>>>>>>>>>>>")
        Log.get_logger().info("[ response code ]: %s " % response.status_code)
        Log.get_logger().info("[ response text ]: %s " % response.text.encode('unicode_escape').decode('utf-8'))
        Log.get_logger().info("[ response cookies ]: %s " % response.cookies)
        Log.get_logger().info("[ response headers ]: %s " % response.headers)

        return response.status_code, response.json() if json else response.text, response.cookies

    def parse_cookie(self, cookies):
        cookies_list = cookies.split(';')
        cookie_dict = {}
        for cookie in cookies_list:
            k, v = cookie.split('=', 1)
            cookie_dict[k.strip()] = v
        self.cookie_dict = cookie_dict