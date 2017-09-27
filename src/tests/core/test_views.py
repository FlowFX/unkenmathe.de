"""Test some core views."""
from django.urls import reverse

from um.exercises import views as exercises_views

import pytest



def test_favicon(client):
    # GIVEN any state
    # WHEN a browser requests the favicon.ico from the website root
    url = '/favicon.ico'
    response = client.get(url)

    # THEN it gets redirected to the file
    assert response.status_code == 302


def test_robots_txt(client):
    # GIVEN any state
    # WHEN a browser requests the robots.txt
    url = '/robots.txt'
    response = client.get(url)

    # THEN it is served
    assert response.status_code == 200
    assert 'www.unkenmathe.de' in response.content.decode()


class TestBasicViews:

    def test_home_page_GET(self, mocker, rf, exercises):
        # GIVEN any state
        mocker.patch.object(exercises_views.ExcerciseListView, 'get_queryset', return_value=exercises)

        # WHEN calling the home page
        url = reverse('index')
        request = rf.get(url)
        response = exercises_views.ExcerciseListView.as_view()(request)

        # THEN it's there
        assert response.status_code == 200

    def test_home_page_shows_all_exercises(self, client, mocker, exercises):
        # GIVEN a number of exercises
        mocker.patch.object(exercises_views.ExcerciseListView, 'get_queryset', return_value=exercises)

        # WHEN calling the home page
        url = reverse('index')
        response = client.get(url)

        # # THEN all exercises are displayed with html text
        for ex in exercises:
            assert ex.text in response.content.decode()
