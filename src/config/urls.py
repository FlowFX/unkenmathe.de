"""URL configuration."""
from django.conf.urls import include, url
from django.contrib import admin

from um.core import views as core_views
from um.exercises import views as exercises_views
from um.exercises import urls as exercises_urls
from um.sheets import urls as sheets_urls


urlpatterns = [
    url(r'^favicon\.ico$', core_views.favicon_view),  # redirect stupid browser looking for /favicon.ico
    url(r'^robots\.txt$', core_views.robots_txt_view),  # serve the robots.txt
    url(r'^$', core_views.IndexView.as_view(), name='index'),
    url(r'^root/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^aufgaben/', include(exercises_urls, namespace='exercises')),
    url(r'^aufgabenblaetter/', include(sheets_urls, namespace='sheets')),
]
