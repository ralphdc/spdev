#!/usr/bin/env python3

from .Parent import Parent
from config import Config
from app import Log
import re
import json

class Spider(Parent):

    def __init__(self, cookies):
        super(Spider, self).__init__(cookies)
        try:
            self.headers = Config.chrome_headers
        except Exception as e:
            Log.get_logger().exception(e)

    def hello(self):
        print("hello world!")

    def get_login_page_cookie(self):
        code, text, cookie = self.http_get(self.init_url, self.headers)
        return cookie

    def get_login_token(self):
        cookies = self.get_login_page_cookie()
        code , text, _ = self.http_get(self.login_token_url, self.headers, None, cookies, 1)
        return text.get('rkey') if code == 200 else None




    def get_login_response(self):
        token = self.get_login_token()
        data = {"email": self.username, "domain": "renren.com", "key_id":1, "captcha_type": "web_login", "password": self.password, "rkey": token}
        code, text, cookies = self.http_post(self.login_url, self.headers, data, None)
        return text if code == 200 else None

    def get_profile(self):
        _, profile, _ = self.http_get(self.profile_url, self.headers, None, self.cookie_dict, 1)
        return  profile

    def get_groupsdata(self):
        _, groupsdata, _ = self.http_get(self.groups_data_url, self.headers, None, self.cookie_dict)
        return groupsdata

    def get_main_user_friends(self):
        _, groupsdata, _ = self.http_get(self.groups_data_url, self.headers, None, self.cookie_dict)
        if groupsdata:
            friends = re.search('\"friends\"(.*?)\}\]', groupsdata).group()
            return friends
        else:
            return None

    def get_main_user_groups(self):
        _, groupsdata, _ = self.http_get(self.groups_data_url, self.headers, None, self.cookie_dict)
        if groupsdata:
            groups = re.search('\"groups\"(.*?)\}\]', groupsdata).group()
            return groups
        else:
            return None

    def get_main_user_spfriends(self):
        _, spfriends, _ = self.http_get(self.groups_data_url, self.headers, None, self.cookie_dict)
        if spfriends:
            sp = re.search('\"specialfriends\"(.*?)\}\]', spfriends).group()
            return sp
        else:
            return None

    def get_main_user_fc(self):
        _, fc, _ = self.http_get(self.groups_data_url, self.headers, None, self.cookie_dict)
        if fc:
            fct = re.search('\"hostFriendCount\"(.*?)\,', fc).group()
            return fct
        else:
            return None

    def get_friend_list(self, fid, requestToken, _rtk):
        pn = 0
        frinds_list = []
        while True:
            page_json = {"fid": fid, "pz": "24", "type": "WEB_FRIEND", "pn": pn}
            data = {"p": json.dumps(page_json), "requestToken": requestToken, "_rtk": _rtk }
            _, f, _ = self.http_post(self.good_friend_url, self.headers, data, self.cookie_dict)

            api_data = json.loads(f)

            try:
                f_info = api_data.get('data').get('friends')
                f_state = api_data.get('data').get('more')
            except Exception as e:
                Log.get_logger().exception(e)
                break

            if not f_info or not f_state:
                break

            for fri in f_info:
                frinds_list.append(fri)
            pn += 1

        return frinds_list