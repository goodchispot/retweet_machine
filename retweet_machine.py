#!/usr/bin/env python3
# coding=utf-8

# -- twitter app の上限 -------------------- #
# appからのツイート＋リツイート/3時間 == 300
# -> 36秒間隔でなら問題ない。
# -> sleepを40[s]にする。
# -> thread が増えたら、sleep数を増やす。
# -> sleep / thread数 == 40[s] になるようにする。
# -------------------------------------------#

__appname__ = 'retweet_machine.py'
__version__ = '0.01'

#  -- Values --  #
CHARACTER_CODE  = "utf-8"
#CHARACTER_CODE  = "shift_jis"

DEFAULT_URL_LIST_FILENAME        = "url_list.txt"
DEFAULT_SLEEP_SEC                = 40
REPEAT_NUM_EACH_URL              = 1
ERROR_LOG_FILENAME               = "retweet_error_url.txt"
#  ------------  #

import tweepy
from time import sleep
import random
import argparse
import credential

class RetweetMachine():

    def __init__(self, consumer_key, consumer_secret, access_token, \
                 access_token_secret, rt_url_list, title):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.rt_url_list = rt_url_list
        self.title = title

    def retweet(self, url, loop_num = REPEAT_NUM_EACH_URL, sleep_sec = DEFAULT_SLEEP_SEC):
        for i in range(loop_num):
            id_tweet = url.split("/")[-1].split("?")[0]
            try:
                status = self.api.get_status(id_tweet, include_my_retweet=1)
            except:
                o_error_log_file = open(ERROR_LOG_FILENAME, "a", encoding=CHARACTER_CODE)
                o_error_log_file.write(url)
                o_error_log_file.close()
                sleep(sleep_sec)
                continue
            if status.retweeted == True:
                self.api.destroy_status(status.current_user_retweet['id'])
            try:
                self.api.retweet(id_tweet)
            except:
                pass
            sleep(sleep_sec)

    def retweet_infinite(self, loop_num = REPEAT_NUM_EACH_URL, \
                         sleep_sec = DEFAULT_SLEEP_SEC):
        while True:
            random_rt_url_list = self.rt_url_list
            random.shuffle(random_rt_url_list)
            for url in random_rt_url_list:
                if self.title is not None:
                    print(self.title)
                print(url.strip())
                self.retweet(url, loop_num, sleep_sec)

def retreive_args():
    import argparse
    parser = argparse.ArgumentParser(description="This is retweet_machine.py.")
    parser.add_argument("-u", "--urllist", dest="urllist_filename", \
                        action="store", default=DEFAULT_URL_LIST_FILENAME, \
                        help="This option is urllist filename. Default \
                              urllist filename is \"" + DEFAULT_URL_LIST_FILENAME + "\".")
    parser.add_argument("-t", "--title", dest="tweet_title", \
                        action="store", default=None, \
                        help="This option is tweet title (if you'd like to show).")
    parser.add_argument("-s", "--sleep", dest="sleep_sec", \
                        action="store", default=DEFAULT_SLEEP_SEC, \
                        help="This option is sleep time [s]. Default sleep time is 40[s]")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = retreive_args()

    o_url_list_file = open(args.urllist_filename, "r", encoding=CHARACTER_CODE)
    url_list = o_url_list_file.readlines()
    o_url_list_file.close()

    retweet_machine = RetweetMachine(credential.consumer_key, \
                                     credential.consumer_secret, \
                                     credential.access_token, \
                                     credential.access_token_secret, \
                                     url_list, args.tweet_title)

    retweet_machine.retweet_infinite(REPEAT_NUM_EACH_URL, int(args.sleep_sec))
