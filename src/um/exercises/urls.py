"""URL configuration for exercises app."""
from django.urls import path
from django.conf.urls import url

from . import views


app_name='exercises'
urlpatterns = [
    url(r'^$', views.ExcerciseListView.as_view(), name='index'),
    url(r'^howto$', views.HowtoView.as_view(), name='howto'),
    url(r'^neu$', views.ExerciseCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', views.ExerciseDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/bearbeiten$', views.ExerciseUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/loeschen$', views.ExerciseDeleteView.as_view(), name='delete'),
    url(r'^(?P<slug>[-\w]+)/pdf$', views.exercise_pdf_view, name='pdf'),
]
