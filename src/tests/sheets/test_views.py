"""Unit tests."""
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

from um.core.factories import UserFactory
from um.exercises.factories import ExerciseFactory
from um.sheets import factories, models, views

import pytest


class TestSheetCreateView:

    TESTPARAMS_CREATE_VIEW_GET = [
        ('anonymous', 302),
        ('authenticated', 200),
        ('staff', 200)]

    @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_CREATE_VIEW_GET)
    def test_create_view_doesnt_allow_anonymous_user(self, client, rf, users, user_status, status_code):
        # GIVEN a user
        user = users[user_status]

        # WHEN calling the sheet create view
        url = reverse('sheets:create')
        request = rf.get(url)
        request.user = user
        response = views.SheetCreateView.as_view()(request)

        # THEN it's there, or not
        assert response.status_code == status_code

    def test_post_to_create_view_adds_author_to_object(self, db, rf, users, mocker):
        # GIVEN an existing exercise AND a user
        ex = ExerciseFactory.create()
        user = UserFactory.create()

        # WHEN making a post request to the create view
        url = reverse('sheets:create')
        request = rf.post(url, data={'exercises': ex.id})
        request.user = user
        views.SheetCreateView.as_view()(request)

        # THEN the user gets attached to the sheet as the author
        sheet = models.Sheet.objects.last()
        assert sheet.author == user

    def test_post_to_create_view_redirects_to_detail_view(self, db, rf, users, mocker):
        # GIVEN an existing exercise AND a user
        ex = ExerciseFactory.create()
        user = UserFactory.create()

        # WHEN making a post request to the create view
        url = reverse('sheets:create')
        request = rf.post(url, data={'exercises': ex.id})
        request.user = user
        response = views.SheetCreateView.as_view()(request, url)

        # THEN it redirects to the detail view
        sheet = models.Sheet.objects.last()
        assert response.status_code == 302
        assert response.url == sheet.url


class TestSheetDetailView:

    def test_get_detail_view(self, db, rf, mocker):
        # GIVEN an existing exercise sheet
        exs = ExerciseFactory.create_batch(2)
        sheet = factories.SheetFactory.create(exercises=(exs[0].id, exs[1].id))
        mocker.patch.object(views.SheetDetailView, 'get_object', return_value=sheet)

        # WHEN calling the sheet detail view
        url = reverse('sheets:detail', kwargs={'pk': sheet.pk})
        request = rf.get(url)
        request.user = AnonymousUser()
        response = views.SheetDetailView.as_view()(request, pk=sheet.pk)

        # THEN it's there
        assert response.status_code == 200

        # AND it can be rendered
        response.render()

        # AND it shows some basic informtion
        html = response.content.decode()
        assert str(sheet.id) in html

    TESTPARAMS_CAN_EDIT = [
        ('anonymous', False),
        ('authenticated', False),
        ('author', True),
        ('staff', True)]

    @pytest.mark.parametrize('user_status, can_edit', TESTPARAMS_CAN_EDIT)
    def test_context_includes_variable_can_edit(self, rf, users, mocker, user_status, can_edit):
        # GIVEN a user
        user = users[user_status]

        # AND an exercise sheet
        sheet = factories.SheetFactory.build()

        if user_status == 'author':
            sheet.author = user
        mocker.patch.object(views.SheetDetailView, 'get_object', return_value=sheet)

        # WHEN calling the sheet detail view
        url = reverse('sheets:detail', kwargs={'pk': sheet.pk})
        request = rf.get(url)
        request.user = user
        response = views.SheetDetailView.as_view()(request, pk=sheet.pk)

        # THEN the response includes the context variable `can_edit`
        assert response.context_data.get('can_edit') == can_edit


# class TestExerciseUpdateView:

#     TESTPARAMS_UPDATE_VIEW_GET = [
#         ('anonymous', 302),
#         ('authenticated', 302),
#         ('author', 200),
#         ('staff', 200)]

#     @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_UPDATE_VIEW_GET)
#     def test_update_view_requires_staff_or_author(self, rf, users, mocker, user_status, status_code):
#         # GIVEN a user
#         user = users[user_status]

#         # AND an existing exercise
#         ex = factories.ExerciseFactory.build()
#         if user_status == 'author':
#             ex.author = user
#         mocker.patch.object(views.ExerciseUpdateView, 'get_object', return_value=ex)

#         # WHEN calling the exercise update view
#         url = reverse('exercises:update', kwargs={'pk': ex.id})
#         request = rf.get(url)
#         request.user = user
#         response = views.ExerciseUpdateView.as_view()(request, pk=ex.id)

#         # THEN it's there
#         assert response.status_code == status_code

#     def test_post_to_update_view_preserves_the_original_author(self, db, rf, mocker):
#         mocker.patch('um.exercises.views.Exercise.render_html')
#         mocker.patch('um.exercises.views.Exercise.render_tex')

#         # GIVEN an existing exercise
#         user = UserFactory.create()
#         ex = factories.ExerciseFactory.create()

#         original_author = ex.author
#         assert user != original_author

#         # WHEN making a post request to the create view
#         url = reverse('exercises:update', kwargs={'pk': ex.id})
#         request = rf.post(url, data=exercise_data)
#         request.user = UserFactory.create()
#         views.ExerciseUpdateView.as_view()(request, pk=ex.id)

#         # THEN the author is preserved
#         updated_ex = models.Exercise.objects.get(id=ex.id)
#         assert updated_ex.author == original_author

#     def test_post_to_update_view_redirects_to_home_page(self, db, rf, mocker):
#         mocker.patch('um.exercises.views.Exercise.render_html')
#         mocker.patch('um.exercises.views.Exercise.render_tex')

#         # GIVEN an existing exercise
#         user = UserFactory.create()
#         ex = factories.ExerciseFactory.create(author=user)

#         # WHEN making a post request to the create view
#         url = reverse('exercises:update', kwargs={'pk': ex.id})
#         request = rf.post(url, data=exercise_data)
#         request.user = user
#         response = views.ExerciseUpdateView.as_view()(request, pk=ex.id)

#         # THEN it redirects back to the home page
#         assert response.status_code == 302
#         assert response.url == '/'


# class TestExerciseDeleteView:

#     TESTPARAMS_UPDATE_VIEW_GET = [
#         ('anonymous', 302),
#         ('authenticated', 302),
#         ('author', 200),
#         ('staff', 200)]

#     @pytest.mark.parametrize('user_status, status_code', TESTPARAMS_UPDATE_VIEW_GET)
#     def test_delete_view_requires_staff_or_author(self, rf, users, mocker, user_status, status_code):
#         # GIVEN a user
#         user = users[user_status]

#         # AND an existing exercise
#         ex = factories.ExerciseFactory.build()
#         if user_status == 'author':
#             ex.author = user
#         mocker.patch.object(views.ExerciseDeleteView, 'get_object', return_value=ex)

#         # WHEN calling the exercise delete view
#         url = reverse('exercises:delete', kwargs={'pk': ex.id})
#         request = rf.get(url)
#         request.user = user
#         response = views.ExerciseDeleteView.as_view()(request, pk=ex.id)

#         # THEN it's there
#         assert response.status_code == status_code
#         if status_code == 200:
#             assert response.template_name[0] == 'exercises/exercise_confirm_delete.html'


# class TestExercisePDFView:

#     def test_pdf_view_returns_pdf(self, rf, mocker):
#         # GIVEN an exercise
#         ex = factories.ExerciseFactory.build(
#             text='''# A title\nAnd some text''',
#         )

#         # mock the exercise
#         mocker.patch.object(models.Exercise.objects, 'get', return_value=ex)

#         # mock results of pdflatex running
#         f = open(os.path.join(TEST_BASE_DIR, 'data/example.pdf'), 'rb')
#         mocker.patch('um.exercises.views.pdflatex', return_value=f)

#         # WHEN calling the PDF view
#         url = reverse('exercises:pdf', kwargs={'pk': ex.id})
#         request = rf.get(url)
#         response = views.exercise_pdf_view(request, pk=ex.id)

#         # THEN the response is a PDF document
#         assert response.status_code == 200
#         assert magic.from_buffer(response.content, mime=True) == 'application/pdf'
