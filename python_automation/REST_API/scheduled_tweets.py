from twython import Twython

APP_KEY = 'YwPserC40bg5pD8n1o9wVLxmX'
APP_SECRET = 'QcaZ08DmePhD6pGsJYGpwSVI0O7Ha3uC1rdkGuPfvmWL18auai'
OAUTH_TOKEN = '1079548375005945858-XPKUnSsUSZHiluY9kRGqhjCJRpW9IL'
OAUTH_TOKEN_SECRET = '290sqmnu7Ynt98czHB9XFctG1o0QyokkDqLznqhzQDgfX'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# tweet = twitter.get_home_timeline()
# print(tweet)
# print("Tweet text: ", tweet["text"])
# print("Tweet created at: ", tweet["created_at"])
# print("Tweeted by: ", tweet["entitles"]["user_mentions"][0]["name"])
# print("Re Tweeted?: ", tweet["retweet_count"])

from datetime import datetime
import pytz, time
from pytz import timezone
import tweet_config as config

while True:
    for msg in config.scheduled_messages:
        print(msg["timezone"])
        tz = timezone(msg["timezone"])
        utc = pytz.utc
        utc_dt = datetime.utcnow().replace(tzinfo=utc)
        au_dt = utc_dt.astimezone(tz)
        sday = au_dt.strftime('%Y-%m-%d')
        stime = au_dt.strftime('%H:%M')
        print("Current Day: Time", sday, stime)

        if sday == msg["day"]:
            if stime == msg["time"]:
                print("Time", stime)
                print("Content", msg["content"])
                twitter.update_status(status='%s' % msg["content"])

    print("Running.. Will try in another min")