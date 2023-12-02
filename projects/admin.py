from django.contrib import admin

from .models import Project, AdditionalImage

class AdditionalImageAdmin(admin.StackedInline):
    model = AdditionalImage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [AdditionalImageAdmin]

    class Meta:
        model = Project

