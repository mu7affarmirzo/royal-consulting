from modeltranslation.translator import register, TranslationOptions
from competence.models import *


@register(CompetenceModel)
class CompetenceTranslationOptions(TranslationOptions):
    fields = (
        'title',
        # 'body'
    )


@register(BlockCompetenceModel)
class BlockCompetenceTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'body'
    )
