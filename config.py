#!/usr/bin/env python3

class Config():

    version = "0.1"
    chrome_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
        "Connection": "close"
    }
    log_app_path = "D:/python/spdev/log/app.log"
    ren_index_url = "http://renren.com/"
    login_url = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018110230913"
    username = "yxba_02@163.com"
    password = "test4BiddingOS!@"
    profile_url = ""
    login_ajax_token_url = "http://login.renren.com/ajax/getEncryptKey"
    groups_data_url = "http://friend.renren.com/groupsdata"

    #搜索好友列表；
    good_friend_url = "http://friend.renren.com/friend/api/getotherfriendsdata"


    redis_host = "127.0.0.1"
    redis_port = 6379

    mongo_host = "127.0.0.1"
    mongo_port = 27017
    mongo_db = "renren"
    mongo_user = "renren"
    mongo_pwd = "renren123"
    mongo_collection = "main_user"
