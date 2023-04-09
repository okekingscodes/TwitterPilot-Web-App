from django.contrib.auth.models import User
from django.db import models

class TwitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    access_token_secret = models.CharField(max_length=255)

    def save_tokens(self, access_token, access_token_secret):
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.save()