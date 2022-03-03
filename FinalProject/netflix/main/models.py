from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

MOVIE_CHOICES = (
    ('series', 'Series'),
    ('movie', 'Movie')
)


class User(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    # This will allow to differentiate users based on age
    uuid = models.UUIDField(default=uuid.uuid4)


class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    # uuid will allow to differentiate between movies and series with unique ids just like Netflix
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    banner = models.ImageField(upload_to='banners')
    poster = models.ImageField(upload_to='posters')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)


class Video(models.Model):
    # Blank is true because that way movies can be standalones and series will have episode numbers
    title = models.CharField(max_length=225, blank=True, null=True)
    file = models.FileField(upload_to='Movies')
