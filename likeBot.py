import tweepy
import time

def get_last_seen_id(file_name):
    fread=open(file_name,'r')
    last_seen_id=fread.read().strip()
    fread.close()
    if last_seen_id is None:
        return 0
    else:
        return int(last_seen_id)

def put_last_seen_id(last_seen_id, file_name):
    fwrite=open(file_name,'w')
    fwrite.write(str(last_seen_id))
    fwrite.close()
    return

file_name="C:/Users/Supriya Singh/PycharmProjects/twitterBot/venv/last_seen_id.txt"

consumer_key= 'rzkYlaT2VSNecYnm0Zpx'
consumer_key_secret= '4ZRN5WYS2LgovGoumyluZEidZEMKSwMaDaSeF1436pYJn1'
acess_token= '1294229047396847616-rL5US5KR3COrEUOmKq3MfCIWl'
access_token_secret= 'ROic6zThp3MKV3YjF7TlBvKyWRenltJhfTiNfA6'

auth= tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(acess_token,access_token_secret)

api= tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user= api.me()

hashtag= '#AatmaNirbharBharat OR @narendramodi'
no_of_searches= 5

old_last_seen_id= get_last_seen_id(file_name)
print(old_last_seen_id,"is last seen id.")

new_last_seen_id=None

tweets=tweepy.Cursor(api.search, hashtag, result_type='recent').items(no_of_searches)
for tweet in tweets:
    if tweet.id==old_last_seen_id:
        print("matched! tweet_id is",tweet.id,"and old_last_seen_id is",old_last_seen_id)
        break
    try:
        if new_last_seen_id==None:
            new_last_seen_id=tweet.id
        print("New tweet found:",tweet.id, tweet.text)
        tweet.favorite()
        time.sleep(1)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
if new_last_seen_id==None:
    put_last_seen_id(old_last_seen_id, file_name)
else:
    put_last_seen_id(new_last_seen_id, file_name)
print("Done")
