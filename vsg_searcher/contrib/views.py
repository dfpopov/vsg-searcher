import requests
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from vsg_searcher.contrib.serializers import AnimeSerializer


class GetAnimeAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search", '/')
        print(request,'request')
        print(search,'search')
        parameters = search
        if not request.user.is_authenticated:
            parameters = search + '&limit=3'
        anime_list = requests.get(f'https://api.jikan.moe/v4/anime?q={parameters}')
        serializer = AnimeSerializer(data=anime_list.json()['data'], many=True)
        serializer.is_valid(raise_exception=True)
        template = loader.get_template('pages/home.html')
        context = {
            'data': serializer.data,
        }
        return HttpResponse(template.render(context, request))
