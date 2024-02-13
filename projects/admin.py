from django.contrib import admin

from .models import Project, AdditionalImage

class AdditionalImageAdmin(admin.StackedInline):
    model = AdditionalImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    inlines = [AdditionalImageAdmin]

    class Media:
        js = ('js/projects/slug.js',)

    class Meta:
        model = Project
