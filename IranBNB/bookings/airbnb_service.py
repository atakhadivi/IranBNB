import requests
from django.conf import settings

def search_destination(query, country="USA"):
    url = "https://airbnb19.p.rapidapi.com/api/v1/searchDestination"
    headers = {
        'x-rapidapi-key': settings.AIRBNB_API_KEY,
        'x-rapidapi-host': "airbnb19.p.rapidapi.com"
    }
    params = {
        'query': query,
        'country': country
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()
