import tweepy
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.views import Response
from rest_framework.views import APIView
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from . import utils
from .models import TwitterProfile
from django.contrib.auth import get_user_model
User = get_user_model()

def create_tweepy_client(access_token, access_token_secret):
    auth = tweepy.OAuth1UserHandler(utils.API_KEY, utils.API_KEY_SECRET, access_token, access_token_secret)
    return tweepy.API(auth)


class TwitterAPIView(APIView):
    def get(self, request):
        auth = tweepy.OAuth1UserHandler(utils.API_KEY, utils.API_KEY_SECRET)
        

        try:
            redirect_url = auth.get_authorization_url()

            #  redirect_url, request_token, request_token_secret = auth.get_authorization_url(redirect_url=redirect_url)
        except tweepy.TweepyException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        request.session['request_token'] = auth.request_token['oauth_token']
        request.session['request_token_secret'] = auth.request_token['oauth_token_secret']

        return redirect(redirect_url)

    def post(self, request):
        verifier = request.query_params.get('oauth_verifier')

        auth = tweepy.OAuth1UserHandler(utils.API_KEY, utils.API_KEY_SECRET, 
                                        request.session['request_token'], 
                                        request.session['request_token_secret'])

        try:
            auth.get_access_token(verifier)
        except tweepy.TweepyException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        access_token = auth.access_token
        access_token_secret = auth.access_token_secret

        # Save the user's access tokens to the database or another persistent storage mechanism
        # Get the user associated with the request
        user = request.user

        # Create or update the user's TwitterProfile with the access tokens
        twitter_profile, created = TwitterProfile.objects.get_or_create(user=user)
        twitter_profile.save_tokens(access_token, access_token_secret)


        return ( Response({'access_token': access_token, 'access_token_secret': access_token_secret}))
        
        
        
class UserTweetsAPIView(APIView):
    #authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = User.objects.get(username=username)
        twitter_profile = user.twitterprofile

        auth = tweepy.OAuth1UserHandler(
            utils.API_KEY, utils.API_KEY_SECRET,
            twitter_profile.access_token, twitter_profile.access_token_secret
        )

        api = tweepy.API(auth)

        try:
            tweets = api.user_timeline(screen_name=username, count=100)
            
        except tweepy.error.TweepError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serialized_tweets = [serialize_tweet(tweet) for tweet in tweets]

        return Response(serialized_tweets)

def serialize_tweet(tweet):
    return {
        'id': tweet.id_str,
        'text': tweet.text,
        'created_at': tweet.created_at,
        'favorite_count': tweet.favorite_count,
        'retweet_count': tweet.retweet_count,
    }

