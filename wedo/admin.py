from django.contrib import admin
from wedo.models import *
from modeltranslation.admin import TranslationAdmin

# admin.site.register(CentralAsiaPagesModel)

# Register your models here.
class InformationCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "What are we doing?"
class InformationAdmin(InformationCustomAdmin, TranslationAdmin):
    pass
admin.site.register(InformationPagesModel, InformationAdmin)


class NewsCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "News and analytics"
class NewsAdmin(NewsCustomAdmin, TranslationAdmin):
    pass
admin.site.register(NewsModel, NewsAdmin)


class OpportunitiesCustomAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published')
    class Meta:
        verbose_name = "Business Opportunities"
class OpportunitiesAdmin(OpportunitiesCustomAdmin, TranslationAdmin):
    pass
admin.site.register(OpportunitiesModel, OpportunitiesAdmin)

