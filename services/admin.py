from django.contrib import admin

from .models import Service, AdditionalImage

class AdditionalImageAdmin(admin.StackedInline):
    model = AdditionalImage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    inlines = [AdditionalImageAdmin]

    class Meta:
        model = Service
