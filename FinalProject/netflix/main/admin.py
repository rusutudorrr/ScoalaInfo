from django.contrib import admin
from .models import Movie, Profile, User, Video

admin.site.register(Movie),
admin.site.register(Profile),
admin.site.register(User),
admin.site.register(Video)
