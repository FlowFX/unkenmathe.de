"""URL configuration for exercises app."""
from django.urls import path

from . import views


app_name = 'exercises'
urlpatterns = [
    path('', views.ExcerciseListView.as_view(), name='index'),
    path('howto', views.HowtoView.as_view(), name='howto'),
    path('neu', views.ExerciseCreateView.as_view(), name='create'),
    path('<str:slug>', views.ExerciseDetailView.as_view(), name='detail'),
    path('<str:slug>/bearbeiten', views.ExerciseUpdateView.as_view(), name='update'),
    path('<str:slug>/loeschen', views.ExerciseDeleteView.as_view(), name='delete'),
    path('<str:slug>/pdf', views.exercise_pdf_view, name='pdf'),
]
