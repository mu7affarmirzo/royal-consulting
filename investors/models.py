from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete
from uuid import uuid4

import random as r

from djmoney.models.fields import MoneyField

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'blog/{title}-{filename}'.format(
                title=str(instance.title), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class IndustriesModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    little_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    main_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['-date_published']

    @property
    def imageURL(self):
        try:
            url = self.little_image.url
        except:
            url = ''
        return url

    @property
    def mainimageURL(self):
        try:
            url = self.main_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


FILTER_CHOICES = (
    ('business sale', 'Business sale'),
    ('idea and development', 'Idea and developments'),
    ('industries', 'Industries'),
    ('investment size', 'Investment size'),
)

class FilterModel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=20, choices=FILTER_CHOICES, default='1')

    class Meta:
        ordering = ('name',)
        verbose_name = 'filter'
        verbose_name_plural = 'filters'

    def __str__(self):
        return self.name

class BusinessModel(models.Model):
    category = models.ForeignKey(FilterModel, related_name='business', on_delete=models.CASCADE)
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    little_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    main_image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)
    price = MoneyField(max_digits=14, default_currency='USD')
    # price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    class Meta:
        ordering = ['-date_published']

    @property
    def imageURL(self):
        try:
            url = self.little_image.url
        except:
            url = ''
        return url

    @property
    def mainimageURL(self):
        try:
            url = self.main_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)






@receiver(post_delete, sender=IndustriesModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))

pre_save.connect(pre_save_blog_post_receiver, sender=IndustriesModel)


def pre_save_business_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))

pre_save.connect(pre_save_business_post_receiver, sender=BusinessModel)