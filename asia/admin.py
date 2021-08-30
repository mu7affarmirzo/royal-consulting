from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# admin.site.register(CentralAsiaPagesModel)

# Register your models here.
class CAPagesCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "Central-Asia"
class CAPageAdmin(CAPagesCustomAdmin, TranslationAdmin):
    pass
admin.site.register(CentralAsiaPagesModel, CAPageAdmin)