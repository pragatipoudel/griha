from django.contrib import admin

from .models import HomePageContent, AboutContent, TagLine, VirtualWalkthrough


class AboutContentInline(admin.StackedInline):
    model = AboutContent


class VirtualWalkthroughInline(admin.StackedInline):
    model = VirtualWalkthrough


class TagLineInline(admin.StackedInline):
    model = TagLine


class HomePageAdmin(admin.ModelAdmin):
    inlines = [AboutContentInline, VirtualWalkthroughInline, TagLineInline]


admin.site.register(HomePageContent, HomePageAdmin)
