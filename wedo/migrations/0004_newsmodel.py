# Generated by Django 2.2 on 2021-07-31 19:18

import ckeditor.fields
from django.db import migrations, models
import wedo.models


class Migration(migrations.Migration):

    dependencies = [
        ('wedo', '0003_auto_20210731_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=wedo.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.CharField(choices=[('News and Analytics', 'News and Analytics'), ('Interesting facts', 'Interesting facts'), ('Data and Statistics', 'Data and Statistics'), ('Publications', 'Publications')], default='News and Analytics', max_length=2)),
            ],
            options={
                'verbose_name': 'News and Analytics',
                'verbose_name_plural': 'News and Analytics',
                'ordering': ['-date_published'],
            },
        ),
    ]
