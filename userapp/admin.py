from django.contrib import admin
from .models import *

class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'clients_count', 'projects_count', 'upcoming_projects_count', 'events_count')
    list_display_links = ('id',)
    list_editable = ('clients_count', 'projects_count', 'upcoming_projects_count', 'events_count')

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('name', 'email', 'message', 'created_at')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')
    list_filter = ('designation',)
    ordering = ('designation',)
    fields = ('name', 'designation', 'image')

class WhatWeOfferInline(admin.TabularInline):
    model = WhatWeOffer
    extra = 1

class SDGInline(admin.TabularInline):
    model = SDG
    extra = 4

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_first_name', 'project_last_name')
    search_fields = ('project_first_name', 'project_last_name')
    inlines = [WhatWeOfferInline, SDGInline]
    fieldsets = (
        (None, {
            'fields': ('project_first_name', 'project_last_name', 'description', 'image', 'who_we_are', 'our_impact')
        }),
    )

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_at') 
    list_filter = ('status', 'name')
    search_fields = ('name', 'description')

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
    search_fields = ('description',)
    list_filter = ('description',)

class HighlightMediaAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'uploaded_at')
    search_fields = ('description',)

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'uploaded_at')
    search_fields = ('title', 'media_type')
    list_filter = ('media_type', 'uploaded_at')
    ordering = ('-uploaded_at',)

class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')

class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'applied_at')
    search_fields = ('name', 'email')
    list_filter = ('position', 'applied_at')
    readonly_fields = ('name', 'email', 'position', 'resume', 'message', 'applied_at')

class SupportMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(HighlightMedia, HighlightMediaAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
admin.site.register(JobOpening, JobOpeningAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(SupportMessage, SupportMessageAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)

