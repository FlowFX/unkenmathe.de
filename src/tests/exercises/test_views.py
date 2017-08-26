"""Unit tests."""
from django.urls import reverse

import magic

from um.core.factories import UserFactory
from um.exercises import factories, models, views


exercise_text = {'text': 'What is 5 + 4?'}


class TestBasicViews:

    def test_home_page_GET(self, client, mocker):
        # GIVEN any state
        exercises = factories.ExerciseFactory.build_batch(3)
        mocker.patch.object(views.ExcerciseListView, 'get_queryset', return_value=exercises)

        # WHEN calling the home page
        url = reverse('index')
        response = client.get(url)

        # THEN it's there
        assert response.status_code == 200

    def test_home_page_shows_all_exercises(self, db, client):
        # GIVEN a number of exercises
        ex1 = factories.ExerciseFactory.create()
        ex2 = factories.ExerciseFactory.create()

        # WHEN calling the home page
        url = reverse('index')
        response = client.get(url)

        # THEN all exercises are displayed
        assert ex1.text in response.content.decode()
        assert ex2.text in response.content.decode()


class TestExerciseCRUDViews:

    def test_get_create_view(self, client):
        # GIVEN any state
        # WHEN calling the exercise create view
        url = reverse('exercises:create')
        response = client.get(url)

        # THEN it's there
        assert response.status_code == 200

    def test_post_to_create_view_adds_author_to_object(self, db, rf):
        # GIVEN an empty database
        assert models.Exercise.objects.count() == 0
        # AND a user
        user = UserFactory.create()

        # WHEN making a post request to the create view
        url = reverse('exercises:create')
        request = rf.post(url, data=exercise_text)
        request.user = user
        views.ExerciseCreateView.as_view()(request)

        # THEN the user gets attached to the exercise as the author
        ex = models.Exercise.objects.first()
        assert ex.author == user

    def test_post_to_create_view_redirects_to_home_page(self, db, rf):
        # GIVEN any state
        # WHEN making a post request to the create view
        url = reverse('exercises:create')
        request = rf.post(url, data=exercise_text)
        request.user = UserFactory.create()
        response = views.ExerciseCreateView.as_view()(request, url)

        # THEN it redirects back to the home page
        assert response.status_code == 302
        assert response.url == '/'

    def test_get_update_view(self, client, mocker):
        # GIVEN an existing exercise
        ex = factories.ExerciseFactory.build()
        mocker.patch.object(views.ExerciseUpdateView, 'get_object', return_value=ex)

        # WHEN calling the exercise update view
        url = reverse('exercises:update', kwargs={'pk': ex.id})
        response = client.get(url)

        # THEN it's there
        assert response.status_code == 200

    def test_post_to_update_view_preserves_the_original_author(self, db, rf):
        # GIVEN an existing exercise
        user = UserFactory.create()
        ex = factories.ExerciseFactory.create()

        original_author = ex.author
        assert user != original_author

        # WHEN making a post request to the create view
        url = reverse('exercises:update', kwargs={'pk': ex.id})
        request = rf.post(url, data=exercise_text)
        request.user = UserFactory.create()
        views.ExerciseUpdateView.as_view()(request, pk=ex.id)

        # THEN the author is preserved
        updated_ex = models.Exercise.objects.get(id=ex.id)
        assert updated_ex.author == original_author

    def test_post_to_update_view_redirects_to_home_page(self, db, client):
        # GIVEN an existing exercise
        ex = factories.ExerciseFactory.create()

        # WHEN making a post request to the create view
        url = reverse('exercises:update', kwargs={'pk': ex.id})
        response = client.post(url, data=exercise_text)

        # THEN it redirects back to the home page
        assert response.status_code == 302
        assert response.url == '/'

    def test_get_detail_view(self, client, mocker):
        # GIVEN an existing exercise
        ex = factories.ExerciseFactory.build()
        mocker.patch.object(views.ExerciseDetailView, 'get_object', return_value=ex)

        # WHEN calling the exercise detail view
        url = reverse('exercises:detail', kwargs={'pk': ex.id})
        response = client.get(url)

        # THEN it's there
        assert response.status_code == 200


class TestExercisePDFViews:

    def test_pdf_view_returns_pdf(self, mocker, rf):
        # GIVEN an exercise
        ex = factories.ExerciseFactory.build(
            text='''# A title\nAnd some text''',
        )
        mocker.patch.object(models.Exercise.objects, 'get', return_value=ex)

        # WHEN calling the PDF view
        url = reverse('exercises:pdf', kwargs={'pk': ex.id})
        request = rf.get(url)
        response = views.exercise_pdf_view(request, pk=ex.id)

        # THEN the response is a PDF document
        assert response.status_code == 200
        assert magic.from_buffer(response.content, mime=True) == 'application/pdf'
