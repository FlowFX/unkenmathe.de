"""URL configuration."""
from django.conf.urls import include, url
from django.views.generic import TemplateView

from exercises import urls as exercises_urls


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^exercises/', include(exercises_urls, namespace='exercises')),
]
