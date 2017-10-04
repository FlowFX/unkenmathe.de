"""Admin."""
from django.contrib import admin
from .models import Exercise, ExerciseExample


class ExerciseAdmin(admin.ModelAdmin):
    """Admin interface for the Exercise model."""

    fields = ('author', 'text', 'text_html', 'text_tex')
    readonly_fields = ('text_html', 'text_tex')

    list_display = ('pk', 'text', 'author', 'license', 'created')
    list_filter = ('author', 'license')


class ExerciseExampleAdmin(admin.ModelAdmin):
    """Admin interface for the ExerciseExample model."""

    fields = ('title', 'exercise', 'description')

    list_display = ('title', 'exercise', 'description')


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseExample, ExerciseExampleAdmin)
