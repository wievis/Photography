from django.contrib import admin
from django.forms import TextInput, NumberInput
from django.db import models
from .models import Photo, Visitor

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'aparat', 'ogniskowa', 'naswietlanie', 'created']
    list_editable = ['order', 'aparat', 'ogniskowa', 'naswietlanie']
    readonly_fields = ['created']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '15'})},
        models.IntegerField: {'widget': NumberInput(attrs={'size': '5'})},
    }

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('ip', 'country', 'at')
    list_filter = ('country', 'ip')