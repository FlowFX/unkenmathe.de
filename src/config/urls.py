"""URL configuration."""
from django.conf.urls import include, url

from um.exercises import urls as exercises_urls
from um.exercises.views import ExcerciseListView


urlpatterns = [
    url(r'^$', ExcerciseListView.as_view(), name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^exercises/', include(exercises_urls, namespace='exercises')),
]
