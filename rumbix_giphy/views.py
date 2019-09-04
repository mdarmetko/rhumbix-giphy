from django.http import JsonResponse
import requests

def Giphy(request, search_term):
    giphy_url = get_giphy(search_term)
    return JsonResponse({'url': giphy_url})


def get_giphy(search):
    url = f'http://api.giphy.com/v1/gifs/search?q={search}&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1'
    response = requests.get(url)
    giphy_url = response.json()['data'][0]['embed_url']
    return giphy_url
