"""URL configuration for sheets app."""
from django.conf.urls import url

from . import views


app_name = 'sheets'
urlpatterns = [
    url(r'^neu$', views.SheetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>[-\w]+)/$', views.SheetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[-\w]+)/bearbeiten$', views.SheetUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>[-\w]+)/delete$', views.ExerciseDeleteView.as_view(), name='delete'),
    # url(r'^(?P<pk>[-\w]+)/pdf$', views.exercise_pdf_view, name='pdf'),
]
