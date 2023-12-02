from django.contrib import admin
from django.urls import path, include, re_path
from Tokens import views as Tokens

urlpatterns = [
    path('admin/', admin.site.urls),
    path('strava_success', Tokens.strava_success, name='strava_success'),
    path('strava_error', Tokens.strava_error, name='strava_error'),
    path('Runnin/strava_callback/', Tokens.strava_callback, name='strava_callback'),
    path('Runnin/initiate_strava_auth/', Tokens.initiate_strava_auth, name='initiate_strava_auth'),
]
