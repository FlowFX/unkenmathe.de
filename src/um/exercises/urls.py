"""URL configuration for exercises app."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ExcerciseListView.as_view(), name='index'),
    url(r'^howto$', views.HowtoView.as_view(), name='howto'),
    url(r'^new$', views.ExerciseCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[-\w]+)/$', views.ExerciseDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[-\w]+)/edit$', views.ExerciseUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>[-\w]+)/delete$', views.ExerciseDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[-\w]+)/pdf$', views.exercise_pdf_view, name='pdf'),
]
