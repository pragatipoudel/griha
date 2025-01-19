from django.contrib import admin

from .models import (
    Service, ServiceHeader, AboutService,
    ServiceProcess, ServiceProcessStep,
    ServiceWalkthrough,
    ServiceImageComparisons,
    ServiceValue
)


class ServiceHeaderInline(admin.StackedInline):
    model = ServiceHeader


class AboutServiceInline(admin.StackedInline):
    model = AboutService


class ServiceProcessInline(admin.StackedInline):
    model = ServiceProcess


class ServiceProcessStepInline(admin.StackedInline):
    model = ServiceProcessStep



class ServiceWalkthroughInline(admin.StackedInline):
    model = ServiceWalkthrough


class ServiceImageComparisonsInline(admin.StackedInline):
    model = ServiceImageComparisons


class ServiceValueInline(admin.StackedInline):
    model = ServiceValue


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}
    inlines = [
        ServiceHeaderInline,
        AboutServiceInline,
        ServiceProcessInline,
        ServiceWalkthroughInline,
        ServiceImageComparisonsInline,
        ServiceValueInline,
    ]


@admin.register(ServiceProcess)
class ServiceProcessAdmin(admin.ModelAdmin):
    inlines = [
        ServiceProcessStepInline,
    ]
