import pytest
from django.test import RequestFactory
from vsg_searcher.contrib.views import GetAnimeAPIView
from vsg_searcher.users.models import User


pytestmark = pytest.mark.django_db

class TestGetAnimeView:

    def test_get_animes(self, user: User, rf: RequestFactory):
        view = GetAnimeAPIView()
        request = rf.get("/?search=attack")
        request.user = user
        response = view.get(request)
        assert response.status_code == 200
        assert 'myanimelist.net' in response.content.decode('utf-8')
