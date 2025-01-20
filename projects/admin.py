from django.contrib import admin

from .models import Project, ProjectImage


class ProjectImageInline(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    inlines = [ProjectImageInline]

    class Media:
        js = ('js/projects/slug.js',)

    class Meta:
        model = Project
