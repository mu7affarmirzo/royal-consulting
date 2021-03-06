# Generated by Django 2.2 on 2021-04-16 12:56

import ckeditor.fields
from django.db import migrations, models
import infopages.models


class Migration(migrations.Migration):

    dependencies = [
        ('infopages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('little_image', models.ImageField(blank=True, null=True, upload_to=infopages.models.upload_location)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=infopages.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
    ]
