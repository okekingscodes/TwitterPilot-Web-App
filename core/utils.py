import tweepy

oauth1_user_handler = tweepy.OAuth1UserHandler(
    "API / Consumer Key here", "API / Consumer Secret here",
    callback="Callback / Redirect URI / URL here"
)