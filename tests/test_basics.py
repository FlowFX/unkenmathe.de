"""Unit tests."""
from django.urls import reverse


class TestBasicViews:

    def test_home_page_GET(self, client):
        # GIVEN any state
        # WHEN calling the home page
        response = client.get('/')

        # THEN it's there
        assert response.status_code == 200

    def test_exercise_create_view(self, client):
        # GIVEN any state
        # WHEN calling the exercise create view
        url = reverse('exercises:create')
        response = client.get(url)


class TestExerciseModel:

    def test_exercise_can_be_saved(self, db):
        # GIVEN any state
        # WHEN adding a new exercise to the database
        # THEN it works
        pass
