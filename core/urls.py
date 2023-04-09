from django.urls import path
from . import views

urlpatterns = [
    path('', views.TwitterAPIView.as_view(), name='index'),
    path('tweets/', views.UserTweetsAPIView.as_view(), name='twitter_login'),
    # path('twitter_callback/', views.twitter_callback, name='twitter_callback'),
    # path('twitter_logout/', views.twitter_logout, name='twitter_logout'),
]