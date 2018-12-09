#!/usr/bin/env python3


from app.Spider import Spider

import argparse

from app import Log

from app import MongoDB

import re

def parse_groups_data(data_string):
    data_body = re.search('\"groups\"(.*?)\]', data_string).group()
    print(data_body)


def get_person_friend(fid):
    pass


if __name__ == '__main__':
    Log.get_logger().info("----------------application begin to execute------------------")

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--run", type=str, default='spider', choices=['spider'], help="please input init operation~!")
    parser.add_argument("-p", "--operate", type=str, default='mainfriend', choices=['mainfriend', 'queryfriend', 'fire'], help="please input init operation~!")
    parser.add_argument("-f", "--fid", type=str, default='227858937', help="please input member fid~!")
    parser.add_argument("-t", "--rtk", type=str, default='-1716276427', help="please input request post token~!")
    parser.add_argument("-k", "--_rtk", type=str, default='6574b18f', help="please input request post token~!")
    parser.add_argument("-d", "--dg", type=str, default='fire', help="please input dg operate command~!")

    args = parser.parse_args()

    Cookie = "anonymid=jox4s669-z94iug; _r01_=1; ln_uact=yxba_02@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20141225/2040/main_OfDO_747d00029c29195a.jpg; jebe_key=06244583-718b-4363-9e4a-2ce0463f14ff%7Cf38044e0b216ea6d1642d82816df489c%7C1543165317107%7C1%7C1543165316373; __utmz=10481322.1543418285.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/223411359/profile; depovince=GW; _de=085C0D6D57D8483C5BF7EAB63017E04A; wp_fold=0; __utma=10481322.203082104.1543418285.1543418285.1544345645.2; _ga=GA1.2.2008285777.1543150874; _gid=GA1.2.1701398263.1544349788; jebecookies=04a25418-dab1-4e63-a670-62159647e5eb|||||; ick_login=8e1d318c-2d97-4e61-b557-a851dc538510; p=82c528b770f9356d5650c238e672e7ed7; first_login_flag=1; t=25423cb670a8526cbfe75ef6305329e07; societyguester=25423cb670a8526cbfe75ef6305329e07; id=102747867; xnsid=6d84261a; loginfrom=syshome; ch_id=10016; jebe_key=06244583-718b-4363-9e4a-2ce0463f14ff%7Cf38044e0b216ea6d1642d82816df489c%7C1543165317107%7C1%7C1544350852382"
    Cookie = "anonymid=jox4s669-z94iug; _r01_=1; ln_uact=yxba_02@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20141225/2040/main_OfDO_747d00029c29195a.jpg; jebe_key=06244583-718b-4363-9e4a-2ce0463f14ff%7Cf38044e0b216ea6d1642d82816df489c%7C1543165317107%7C1%7C1543165316373; depovince=GW; _de=085C0D6D57D8483C5BF7EAB63017E04A; _ga=GA1.2.2008285777.1543150874; _gid=GA1.2.1701398263.1544349788; __utma=10481322.203082104.1543418285.1544345645.1544351771.3; __utmz=10481322.1544351771.3.2.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/145749760/profile; __utmb=10481322.1.10.1544351771; jebecookies=15db1112-05e6-4653-809d-d791f8b34f6b|||||; ick_login=d59c6497-d399-4cf2-9894-929952a37e1b; p=82c528b770f9356d5650c238e672e7ed7; first_login_flag=1; t=25423cb670a8526cbfe75ef6305329e07; societyguester=25423cb670a8526cbfe75ef6305329e07; id=102747867; xnsid=6d6baaff; loginfrom=syshome; ch_id=10016; jebe_key=06244583-718b-4363-9e4a-2ce0463f14ff%7Cf38044e0b216ea6d1642d82816df489c%7C1543165317107%7C1%7C1544352459489; wp_fold=0"
    if args.run == "spider":
        if args.operate == "mainfriend":
            spider =  Spider(Cookie)
            friends = spider.get_main_user_friends()
            if friends:
               friends = friends.replace('\/', '/')
               friends_list = eval(friends.split(':', 1)[1])
               mgo = MongoDB()
               for friend in friends_list:
                   mgo.get_collection('main_friends').insert_one(friend)
                   print("%s insert ok!" % friend)

        elif args.operate == "queryfriend":
            fid     = args.fid
            rtk     = args.rtk
            _rtk    = args._rtk
            spider = Spider(Cookie)
            fid_friends = spider.get_friend_list(fid, rtk, _rtk)
        elif args.operate == "fire":
            rtk = args.rtk
            _rtk = args._rtk
            spider = Spider(Cookie)
            mgo = MongoDB()
            for d in mgo.get_collection('main_friends').find():
                fid = d.get('fid') or None
                if fid:
                    target = spider.get_friend_list(fid, rtk, _rtk)
                    if target:
                        print("---------------------------fid: %s----------------------------" % fid)
                        print(target)