import requests
from django.http import JsonResponse


def get_animes(request):
    search = request.GET.get("text", "")
    get = requests.get(f'https://api.jikan.moe/v4/anime?q={search}')
    return JsonResponse({"text": search})
