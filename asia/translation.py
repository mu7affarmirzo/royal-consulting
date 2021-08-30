from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(CentralAsiaPagesModel)
class CAPTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body'
    )
