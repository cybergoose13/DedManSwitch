from TwitterAPI import TwitterAPI
from datetime import datetime
from time import sleep
import os.path
import json


class DedTime:  #Subject to name Change
    def __init__(self):
        return

    def parse_to_date(self, time_arr):
        time_arr= time_arr.split(' ')
        date_str= time_arr[5] + "-" + time_arr[1] + "-" + time_arr[2] +\
            " " + time_arr[3]
        return datetime.strptime(date_str, "%Y-%b-%d %H:%M:%S")

    def remove_microseconds(self, time_stamp):
        time_s= time_stamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-7]
        return datetime.strptime(time_s, "%Y-%m-%d %H:%M:%S")


class DedManSwitch:
    def __init__(self):
        return

    def get_keys(self):
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

    def get_post_time(self, response):
        for item in response.get_iterator():
            return item['created_at']

    def get_post_id(self, response):
        for item in response.get_iterator():
            return item['id']
    
    def get_post_text(self, response):
        for item in response.get_iterator():
            return item['text']

    def post_tweet(self, api, msg):
        return api.request('statuses/update', {'status': msg})

    def reply_to_tweet(self, api, msg, tweet_id):
        return api.request('statuses/update', {'in_reply_to_status_id': tweet_id, 'status': msg})

    def run(self, msg, delay):
        ded_start= DedTime().remove_microseconds(datetime.utcnow())
        sleep(delay)
        api= self.get_api(self.get_keys())
        last_post= self.get_last_tweet(api)
        post_time= self.get_post_time(last_post)
        if ded_start < DedTime().parse_to_date(post_time):
            print('Recent post found')
            r= self.reply_to_tweet(api, msg, self.get_post_id(last_post))
            print(r.status_code)
            print("SLEEPING")
            return self.run(msg, delay)
        else:
            '''
            If no tweet has been made since they program ran.
            Execute code here.
            '''
            print("ENDING")
            return

DedManSwitch().run("Check-In passed.\n\t-Bot", 120)