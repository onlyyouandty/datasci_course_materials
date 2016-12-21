import tweepy

consumer_key = "5dFlhJHMo4ZCxC7IkRtUwBs6y"
consumer_secret = "JfVkLh2gFRy1Jkq1pqBLVttiCqKWUogEvh25J9zQ2qDH3YxRAr"
access_token = "295014074-4ZTxz5FFueNrZNvXzyJ0lbDadSfiFPBVAKc5Ri5v"
access_token_secret = "YLKtRc8pWQ2hHZXr3nyKfB2nZq5CiF8Nxp6L7Sl118C4g"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text