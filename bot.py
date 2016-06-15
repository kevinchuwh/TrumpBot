import tweepy
import random
import datetime

consumer_key = "" #consumer key
consumer_secret = "" #consumer secret
access_token = "" #access token
access_token_secret = "" #access token secret

screen_name = "" #twitter target username

tweet_list = ["deck yourself with some battle gear at Trump's upcoming debate!",
                "don't settle for #dryfit, get #TrumpFit",
                "get into the rhythm, get a trump bobblehead",
                "damn trump stickers. make papa proud again.",
                "distract hillary crook. get a trump flag.",
                "the donald mug. assert your dominance in office"]
product_link = ["https://www.amazon.com/gp/product/B00LQ3BPFE/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B00LQ3BPFE&linkId=a705755796d00501582e7ae5cf63275d",
                "https://www.amazon.com/gp/product/B013IU1JAS/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B013IU1JAS&linkId=4049ecdf4b54962b81dfbf47cf3b9d01",
                "https://www.amazon.com/gp/product/B019CWKSIA/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B019CWKSIA&linkId=3efb3d184a1f94ff1fd750b2729d3e03",
                "https://www.amazon.com/gp/product/B01AVHMMG6/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01AVHMMG6&linkId=a0f21e9b270c4a5f989a2df5bfaae03b",
                "https://www.amazon.com/gp/product/B01DIM5YA2/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01DIM5YA2&linkId=bdcc1b26d7a0d9f47c5c9df2d1ddf73f",
                "https://www.amazon.com/gp/product/B01DLB3CI6/ref=as_li_qf_sp_asin_il_tl?ie=UTF8&tag=reddit04fe-20&camp=1789&creative=9325&linkCode=as2&creativeASIN=B01DLB3CI6&linkId=6c4a43f0e8a14a0dba26557ba74facf3"]
try:
    auth = tweepy.OAuthHandler(consumer_key[0], consumer_secret[0])
    auth.set_access_token(access_token[0], access_token_secret[0])
except tweepy.TweepError:
    print("error")

    
api = tweepy.API(auth)
statuses = api.user_timeline(id = "25073877", count = 1) #count refers to number of tweets of target you want to find

for status in statuses:
    retweeters = api.retweets(status.id, count=1) #count refers to number of targets
    for retweeter in retweeters:
        r_int2 = random.randrange(0,6)
        api.create_friendship(retweeter.user.id)
        api.update_status(".@"+retweeter.user.screen_name+" "+tweet_list[r_int2]+" "+product_link[r_int2])
        print("***")
        print("Followed @" + retweeter.user.screen_name)
        print("TrumpBot sent a product!")
        current_time = datetime.datetime.now()
        with open("log.txt", "a") as log: #logging system
            log.write(str(current_time) + "\t@" + retweeter.user.screen_name + "\n")            
