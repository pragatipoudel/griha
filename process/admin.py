from django.contrib import admin

from .models import Process, ProcessStep


class ProcessStepInline(admin.StackedInline):
    model = ProcessStep


class ProcessAdmin(admin.ModelAdmin):
    inlines = [ProcessStepInline]


admin.site.register(Process, ProcessAdmin)
