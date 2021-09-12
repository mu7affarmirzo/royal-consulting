from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# admin.site.register(CompetenceModel)
admin.site.register(ContactUsModel)

# Register your models here.
class BlockCompetenceCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "Competence blocks"
class BlockCompetenceAdmin(BlockCompetenceCustomAdmin, TranslationAdmin):
    pass
admin.site.register(BlockCompetenceModel, BlockCompetenceAdmin)


class CompetenceCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "Competence"
class CompetenceAdmin(CompetenceCustomAdmin, TranslationAdmin):
    pass
admin.site.register(CompetenceModel, CompetenceAdmin)


