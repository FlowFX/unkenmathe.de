"""URL configuration for sheets app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^new$', views.SheetCreateView.as_view(), name='create'),
    # url(r'^(?P<pk>[-\w]+)/$', views.ExerciseDetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[-\w]+)/edit$', views.ExerciseUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>[-\w]+)/delete$', views.ExerciseDeleteView.as_view(), name='delete'),
    # url(r'^(?P<pk>[-\w]+)/pdf$', views.exercise_pdf_view, name='pdf'),
]
