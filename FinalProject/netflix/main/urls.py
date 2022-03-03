from django.urls import path
from .views import homepage, profilelist, NewProfile, browse, moviedetail, playbutton

app_name = 'main'

urlpatterns = [
    path('', homepage),
    path('profile/', profilelist, name='profile_list'),
    path('profile/create/', NewProfile.as_view(), name='profile_create'),
    path('browse/<str:profile_id>/', browse, name='browse'),
    path('movie/detail/<str:movie_id>/', moviedetail, name='detail'),
    path('movie/play/<str:movie_id>/', playbutton, name='play')
]
