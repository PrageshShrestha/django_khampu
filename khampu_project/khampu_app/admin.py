from django.contrib import admin
from .models import (
    UserProfile, Images, SiteContent, Temple, 
    Festival, SocialLink, Activity
)

@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ['key', 'content_type', 'value_preview']
    list_filter = ['content_type']
    search_fields = ['key', 'value']
    
    def value_preview(self, obj):
        return obj.value[:50] + '...' if len(obj.value) > 50 else obj.value
    value_preview.short_description = 'Preview'

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    list_display = ['name', 'caption', 'order']
    list_editable = ['order']
    prepopulated_fields = {}

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'english_date', 'nepali_date']
    list_filter = ['english_date']
    search_fields = ['name']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'order']
    list_editable = ['order']

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'order']
    list_editable = ['order']

# Register existing models
admin.site.register(UserProfile)
admin.site.register(Images)
