from django.contrib import admin
from django.forms import TextInput, NumberInput
from django.db import models
from django.utils.html import format_html
from .models import Photo, Visitor

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_thumbnail', 'order', 'created']
    list_editable = ['order']
    readonly_fields = ['created']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.IntegerField: {'widget': NumberInput(attrs={'style': 'width: 60px'})},
    }

    def display_thumbnail(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; width: auto;" />', obj.thumbnail.url)

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'country', 'at')
    list_filter = ('country', 'ip')