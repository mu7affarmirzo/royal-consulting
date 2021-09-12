from modeltranslation.translator import register, TranslationOptions
from wedo.models import *


@register(InformationPagesModel)
class InformationPagesTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body'
    )


@register(OpportunitiesModel)
class OpportunitiesTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body'
    )


@register(NewsModel)
class NewsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body'
    )