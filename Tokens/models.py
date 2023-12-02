from django.db import models
from django.contrib import admin




class Athlete(models.Model):
    #token fields
    refresh_token = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    expires_at = models.IntegerField()
    
    #athlete fields
    athlete_id = models.IntegerField(unique=True)
    firstname = models.CharField(max_length=50, null = True, blank = True)
    lastname = models.CharField(max_length=50, null = True, blank = True)
    city = models.CharField(max_length=50, null = True, blank = True)
    state = models.CharField(max_length=50, null = True, blank = True)
    country = models.CharField(max_length=20, null = True, blank = True)
    sex = models.CharField(max_length=5, null = True, blank = True)
    follower_count = models.IntegerField(null = True, blank = True)
    following_count = models.IntegerField(null = True, blank = True)

# def __str__(self):
