# Generated by Django 2.2 on 2021-09-12 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competence', '0005_auto_20210912_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competencemodel',
            name='body',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_ar',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_de',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_ja',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_ko',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='competencemodel',
            name='body_zh_cn',
        ),
    ]
