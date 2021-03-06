# Generated by Django 2.2 on 2021-07-31 12:54

import ckeditor.fields
import competence.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompetenceModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=competence.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'Competence',
                'verbose_name_plural': 'Competence',
                'ordering': ['date_published'],
            },
        ),
    ]
