"""Unit tests."""
import os

from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

import magic

from um.core.factories import UserFactory
from um.exercises import factories, models, views

import pytest


TEST_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


exercise_data = {
    'license': 'cc-by',
    'text': 'What is 5 + 4?',
}


class TestExamplesViews:

    def test_howto_view_returns_200(self, client, mocker):
        # GIVEN a an exercise example
        examples = factories.ExerciseExampleFactory.build_batch(3)

        mocker.patch.object(views.HowtoView, 'get_queryset', return_value=examples)

        # WHEN opening the howto page
        url = reverse('exercises:howto')
        response = client.get(url)
        html = response.content.decode()

        # THEN it's there and it displays all exercise texts
        assert response.status_code == 200
        assert examples[0].exercise.text in html

        # AND the example description, too
        assert examples[0].title in html
        assert examples[0].description in html


class TestExerciseCreateView:

    TESTPARAMS_CREATE_VIEW_GET = [
        ('anonymous', 302),
        ('authenticated', 200),
        ('staff', 200)]

    @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_CREATE_VIEW_GET)
    def test_create_view_doesnt_allow_anonymous_user(self, client, rf, users, user_status, status_code):
        # GIVEN a user
        user = users[user_status]

        # WHEN calling the exercise create view
        url = reverse('exercises:create')
        request = rf.get(url)
        request.user = user
        response = views.ExerciseCreateView.as_view()(request)

        # THEN it's there, or not
        assert response.status_code == status_code

    def test_post_to_create_view_adds_author_to_object(self, db, rf, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN an empty database
        assert models.Exercise.objects.count() == 0
        # AND a user
        user = UserFactory.create()

        # WHEN making a post request to the create view
        url = reverse('exercises:create')
        request = rf.post(url, data=exercise_data)
        request.user = user
        views.ExerciseCreateView.as_view()(request)

        # THEN the user gets attached to the exercise as the author
        ex = models.Exercise.objects.last()
        assert ex.author == user

    def test_creating_new_original_exercise_clears_source_information(self, db, rf, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN a user and extended exercise_data
        user = UserFactory.create()
        exercise_data['is_original'] = True
        exercise_data['original_author'] = user.id
        exercise_data['source_url'] = 'http://example.com'

        # WHEN creating the new exercise
        url = reverse('exercises:create')
        request = rf.post(url, data=exercise_data)
        request.user = user
        views.ExerciseCreateView.as_view()(request)

        # THEN the source information is wiped
        ex = models.Exercise.objects.last()
        assert not ex.original_author
        assert not ex.source_url

    def test_post_to_create_view_redirects_to_detail_view(self, db, rf, users, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN any state and a user
        user = UserFactory.create()

        # WHEN making a post request to the create view
        url = reverse('exercises:create')
        request = rf.post(url, data=exercise_data)
        request.user = user
        response = views.ExerciseCreateView.as_view()(request, url)

        # THEN it redirects to the detail view
        ex = models.Exercise.objects.last()
        assert response.status_code == 302
        assert response.url == ex.url

    def test_get_with_url_parameter_prepopulates_text(self, db, rf, mocker):
        # GIVEN an existing exercise
        mocker.patch('um.exercises.factories.Exercise.render_html')
        mocker.patch('um.exercises.factories.Exercise.render_tex')
        ex = factories.ExerciseFactory.create()

        # AND a user
        user = UserFactory.create()

        # WHEN making a GET request to the create view with the exercise id as url parameter
        url = reverse('exercises:create') + f'?template={ex.slug}'
        request = rf.get(url)
        request.user = user
        response = views.ExerciseCreateView.as_view()(request, url)

        # THEN it's there
        assert response.status_code == 200

        # AND the input field is pre-populated with the existing exercise's text
        response.render()
        html = response.content.decode()
        assert ex.text in html


class TestExerciseDetailView:

    def test_get_detail_view(self, rf, mocker):
        # GIVEN an existing exercise
        ex = factories.ExerciseFactory.build()
        mocker.patch.object(views.ExerciseDetailView, 'get_object', return_value=ex)

        # WHEN calling the exercise detail view
        url = reverse('exercises:detail', kwargs={'slug': ex.slug})
        request = rf.get(url)
        request.user = AnonymousUser()
        response = views.ExerciseDetailView.as_view()(request, slug=ex.slug)

        # THEN it's there
        assert response.status_code == 200

    TESTPARAMS_CAN_EDIT = [
        ('anonymous', False),
        ('authenticated', False),
        ('author', True),
        ('staff', True)]

    @pytest.mark.parametrize('user_status, can_edit', TESTPARAMS_CAN_EDIT)
    def test_context_includes_variable_can_edit(self, rf, users, mocker, user_status, can_edit):
        # GIVEN a user
        user = users[user_status]

        # AND an existing exercise
        ex = factories.ExerciseFactory.build()
        if user_status == 'author':
            ex.author = user
        mocker.patch.object(views.ExerciseDetailView, 'get_object', return_value=ex)

        # WHEN calling the exercise detail view
        url = reverse('exercises:detail', kwargs={'slug': ex.slug})
        request = rf.get(url)
        request.user = user
        response = views.ExerciseDetailView.as_view()(request, slug=ex.slug)

        # THEN the response includes the context variable `can_edit`
        assert response.context_data.get('can_edit') == can_edit


class TestExerciseUpdateView:

    TESTPARAMS_UPDATE_VIEW_GET = [
        ('anonymous', 302),
        ('authenticated', 302),
        ('author', 200),
        ('staff', 200)]

    @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_UPDATE_VIEW_GET)
    def test_update_view_requires_staff_or_author(self, rf, users, mocker, user_status, status_code):
        # GIVEN a user
        user = users[user_status]

        # AND an existing exercise
        ex = factories.ExerciseFactory.build()
        if user_status == 'author':
            ex.author = user
        mocker.patch.object(views.ExerciseUpdateView, 'get_object', return_value=ex)

        # WHEN calling the exercise update view
        url = reverse('exercises:update', kwargs={'slug': ex.slug})
        request = rf.get(url)
        request.user = user
        response = views.ExerciseUpdateView.as_view()(request, slug=ex.slug)

        # THEN it's there
        assert response.status_code == status_code

    def test_post_to_update_view_preserves_the_original_author(self, db, rf, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN an existing exercise
        user = UserFactory.create()
        ex = factories.ExerciseFactory.create()

        original_author = ex.author
        assert user != original_author

        # WHEN making a post request to the create view
        url = reverse('exercises:update', kwargs={'slug': ex.slug})
        request = rf.post(url, data=exercise_data)
        request.user = UserFactory.create()
        views.ExerciseUpdateView.as_view()(request, slug=ex.slug)

        # THEN the author is preserved
        updated_ex = models.Exercise.objects.get(slug=ex.slug)
        assert updated_ex.author == original_author

    def test_post_to_update_view_redirects_to_detail_view(self, db, rf, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN an existing exercise
        user = UserFactory.create()
        ex = factories.ExerciseFactory.create(author=user)

        exercise_data['author'] = user.id

        # WHEN making a post request to the create view
        url = reverse('exercises:update', kwargs={'slug': ex.slug})
        request = rf.post(url, data=exercise_data)
        request.user = user
        response = views.ExerciseUpdateView.as_view()(request, slug=ex.slug)

        # THEN it redirects to the detail view
        assert response.status_code == 302
        assert response.url == ex.url

    def test_post_request_with_continue_parameter_returns_to_update_view(self, db, rf, mocker):
        mocker.patch('um.exercises.views.Exercise.render_html')
        mocker.patch('um.exercises.views.Exercise.render_tex')

        # GIVEN an existing exercise
        user = UserFactory.create()
        ex = factories.ExerciseFactory.create(author=user)

        exercise_data['author'] = user.id
        exercise_data['continue'] = 'continue'

        # WHEN making a post request to the create view
        url = reverse('exercises:update', kwargs={'slug': ex.slug})
        request = rf.post(url, data=exercise_data, name='continue')
        request.user = user
        response = views.ExerciseUpdateView.as_view()(request, slug=ex.slug)

        # THEN it returns to the update view
        assert response.status_code == 302
        assert response.url == url


class TestExerciseDeleteView:

    TESTPARAMS_UPDATE_VIEW_GET = [
        ('anonymous', 302),
        ('authenticated', 302),
        ('author', 200),
        ('staff', 200)]

    @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_UPDATE_VIEW_GET)
    def test_delete_view_requires_staff_or_author(self, rf, users, mocker, user_status, status_code):
        # GIVEN a user
        user = users[user_status]

        # AND an existing exercise
        ex = factories.ExerciseFactory.build()
        if user_status == 'author':
            ex.author = user
        mocker.patch.object(views.ExerciseDeleteView, 'get_object', return_value=ex)

        # WHEN calling the exercise delete view
        url = reverse('exercises:delete', kwargs={'slug': ex.slug})
        request = rf.get(url)
        request.user = user
        response = views.ExerciseDeleteView.as_view()(request, slug=ex.slug)

        # THEN it's there
        assert response.status_code == status_code
        if status_code == 200:
            assert response.template_name[0] == 'exercises/exercise_confirm_delete.html'


class TestExercisePDFView:

    def test_pdf_view_returns_pdf(self, rf, mocker):
        # GIVEN an exercise
        ex = factories.ExerciseFactory.build(
            text='''# A title\nAnd some text''',
        )

        # mock the exercise
        mocker.patch.object(models.Exercise.objects, 'get', return_value=ex)

        # mock results of pdflatex running
        f = open(os.path.join(TEST_BASE_DIR, 'data/example.pdf'), 'rb')
        mocker.patch('um.exercises.views.pdflatex', return_value=f)

        # WHEN calling the PDF view
        url = reverse('exercises:pdf', kwargs={'slug': ex.slug})
        request = rf.get(url)
        response = views.exercise_pdf_view(request, slug=ex.slug)

        # THEN the response is a PDF document
        assert response.status_code == 200
        assert magic.from_buffer(response.content, mime=True) == 'application/pdf'


class TestExerciseListViews:

    def test_exercises_index_GET(self, mocker, rf, exercises):
        # GIVEN any state
        mocker.patch.object(views.ExcerciseListView, 'get_queryset', return_value=exercises)

        # WHEN calling exercises index page
        url = reverse('exercises:index')
        request = rf.get(url)
        response = views.ExcerciseListView.as_view()(request)

        # THEN it's there
        assert response.status_code == 200

    def test_exercises_index_shows_all_exercises(self, client, mocker, exercises):
        # GIVEN a number of exercises
        mocker.patch.object(views.ExcerciseListView, 'get_queryset', return_value=exercises)

        # WHEN calling the home page
        url = reverse('exercises:index')
        response = client.get(url)

        # # THEN all exercises are displayed with html text
        for ex in exercises:
            assert ex.text in response.content.decode()
