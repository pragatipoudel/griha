from django.contrib import admin

from .models import HomePageContent, AboutContent, TagLine


class AboutContentInline(admin.StackedInline):
    model = AboutContent


class TagLineInline(admin.StackedInline):
    model = TagLine


class HomePageAdmin(admin.ModelAdmin):
    inlines = [AboutContentInline, TagLineInline]


admin.site.register(HomePageContent, HomePageAdmin)
