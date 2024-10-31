from django.contrib import admin
from content_app import models

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_type', 'description','is_public')  
    list_filter = ('content_type', 'is_public')  
    search_fields = ('title', 'description')
    ordering = ['title']

admin.site.register(models.Content, ContentAdmin)
