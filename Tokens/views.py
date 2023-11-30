from django.shortcuts import render, redirect
import requests
from django.conf import settings
from Tokens.models import Athlete

# Create your views here.

#def strava_success(request):
#
#    return render(request, 'Runnin/strava_success.html')
#
#
#def strava_error(request):
#
#    return render(request, 'Runnin/strava_error.html')


def initiate_strava_auth(request):
    strava_auth_url = (
        "https://www.strava.com/oauth/authorize"
        "?client_id={client_id}"
        "&redirect_uri={redirect_uri}"
        "&response_type=code"
        "&approval_prompt=auto"  
        "&scope=activity:read_all,activity:write"
    ).format(
        client_id=settings.STRAVA_CLIENT_ID,
        redirect_uri="http://127.0.0.1:8000/Runnin/strava_callback/" 
    )

    return redirect(strava_auth_url)

def strava_callback(request):
    auth_code = request.GET.get('code')

    if auth_code:
        response = requests.post(
            settings.AUTH_URL,
            data={
                'client_id': settings.STRAVA_CLIENT_ID,
                'client_secret': settings.STRAVA_CLIENT_SECRET,
                'code': auth_code,
                'grant_type': 'authorization_code'
            }
        )

        if response.status_code == 200:
            data = response.json()
            athlete_data = data.get("athlete")
            if athlete_data is None:
                return redirect('strava_error')

            athlete_id = athlete_data.get("id")
            existing_athlete = Athlete.objects.filter(athlete_id=athlete_id).first()

            if existing_athlete:
                # Aktualizacja istniejącego obiektu Athlete
                existing_athlete.refresh_token = data.get("refresh_token")
                existing_athlete.access_token = data.get("access_token")
                existing_athlete.expires_at = data.get("expires_at")
                existing_athlete.save()
            else:
                # Tworzenie nowego obiektu Athlete
                Athlete.objects.create(
                    athlete_id=athlete_id,
                    refresh_token=data.get("refresh_token"),
                    access_token=data.get("access_token"),
                    expires_at=data.get("expires_at"),
                    firstname=athlete_data.get("firstname"),
                    lastname=athlete_data.get("lastname"),
                    city=athlete_data.get("city"),
                    state=athlete_data.get("state"),
                    country=athlete_data.get("country"),
                    sex=athlete_data.get("sex"),
                    follower_count=athlete_data.get("follower_count"),
                    following_count=athlete_data.get("following_count")
                )

            return redirect('strava_success')
        else:
            return redirect('strava_error')
    else:
        return redirect('trava_error')