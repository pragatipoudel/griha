from django.contrib import admin

from .models import MainGallery, GalleryImage


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]


admin.site.register(MainGallery, GalleryAdmin)
