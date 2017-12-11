"""URL configuration for sheets app."""
from django.urls import path

from . import views


app_name = 'sheets'
urlpatterns = [
    path('neu', views.SheetCreateView.as_view(), name='create'),
    path('<str:pk>', views.SheetDetailView.as_view(), name='detail'),
    path('<str:pk>/bearbeiten', views.SheetUpdateView.as_view(), name='update'),
]
