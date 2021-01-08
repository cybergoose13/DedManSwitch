from os import system
from typing import Iterable
from TwitterAPI import TwitterAPI
from datetime import datetime
from time import sleep
import os.path
import json


class DedTime:  #Subject to name Change
    def __init__(self):
        return

    def parse_to_date(self, time_arr):
        return

    def remove_microseconds(self, time_stamp):
        return


class DedManSwitch:
    def __init__(self):
        return

    def get_keys():
        if not os.path.isfile('keys.json'):
            open('keys.json', 'w+')\
            .write('{\n\t"key":"KEY",\n\t"key_secret":"SECRET",\n\t"token":"TOKEN",\n\t"token_secret":"TOKEN_S"\n}')
            print("No keys.json was dedicated.\nNew File Generated. Add Valid Keys.")
            return exit(0)
        file= open('keys.json', 'r')
        return json.load(file)

    def get_api(self, keys):
        return TwitterAPI(keys['key'], keys['key_secret'], keys['token'], keys['token_secret'])

    def get_last_tweet(self, api):
        return api.request('statuses/user_timeline', {'count':'1'})

    def get_post_time(self, response): # change api to response
        for item in response.get_iterator():
            return item['created_at']

    def get_post_id(self, api): # change api to response
        return
    
    def get_post_text(self, api): # change api to response
        return

    def post_tweet(self, api, msg):
        return

    def reply_to_tweet(self, api, msg, tweet_id):
        return

    def run(self, msg, delay):
        sleep(delay)
        api= self.get_api(self.get_keys())
        if DedTime.remove_microseconds( datetime.utcnow() ) < self.get_post_time():
            r= self.reply_to_tweet(api, msg, self.get_post_id(api))
            print(r.status_code)
            return self.run(msg, delay)
        else:
            '''
            If no tweet has been made since they program ran.
            Execute code here.
            '''
            return


keys= DedManSwitch.get_keys()