from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

# tweet = twitter.get_home_timeline()[0] # 타임라인에서 가장 최근 트윗정보를 가져온다.
# print("Tweet text: ", tweet["text"])
# print("Tweet created at: ", tweet["created_at"])
# print("Tweeted by: ", tweet["user"]["name"])
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
                time.sleep(30) # 트윗 게시 중복요청을 방지하기 위해서 딜레이를 준다.

    print("Running.. Will try in another min")
