from django.contrib import admin

from .models import HomePageContent, AboutContent


class AboutContentInline(admin.StackedInline):
    model = AboutContent


class HomePageAdmin(admin.ModelAdmin):
    inlines = [AboutContentInline]


admin.site.register(HomePageContent, HomePageAdmin)
