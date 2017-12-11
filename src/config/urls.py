"""URL configuration."""
from django.urls import include, path
from django.contrib import admin

from um.core import views as core_views
from um.exercises import views as exercises_views
from um.exercises import urls as exercises_urls
from um.sheets import urls as sheets_urls


urlpatterns = [
    path('favicon.ico', core_views.favicon_view),  # redirect stupid browser looking for /favicon.ico
    path('robots.txt', core_views.robots_txt_view),  # serve the robots.txt
    path('', core_views.IndexView.as_view(), name='index'),
    path('root/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('aufgaben/', include(exercises_urls, namespace='exercises')),
    path('aufgabenblaetter/', include(sheets_urls, namespace='sheets')),
]
