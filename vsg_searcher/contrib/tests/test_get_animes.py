import pytest
from django.test import RequestFactory
from vsg_searcher.contrib.views import GetAnimeAPIView

pytestmark = pytest.mark.django_db

class TestGetAnimeView:

    def test_get_animes(self, rf: RequestFactory):
        view = GetAnimeAPIView()
        request = rf.get("/get_animes?q=attack")
        response = view.get(request)
        assert response.status_code == 200
        assert 'myanimelist.net' in response.content.decode('utf-8')
