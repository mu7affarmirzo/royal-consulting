from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete
from uuid import uuid4


import random as r

def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'wedo/{title}-{filename}'.format(
                title=str(instance.title), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class InformationPagesModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'What are we doing?'
        verbose_name_plural = 'What are we doing?'


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)



class OpportunitiesModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Business Opportunities'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class PhotoBankModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['-date_published']
        verbose_name = 'Photo bank'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return str(url)

    def __str__(self):
        return str(self.title)


R_A_CHOICES = [
    ('News and Analytics', 'News and Analytics'),
    ('Interesting facts', 'Interesting facts'),
    ('Data and Statistics', 'Data and Statistics'),
    ('Publications', 'Publications'),
]


class NewsModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)
    category = models.CharField(
        max_length=50,
        choices=R_A_CHOICES,
        default='News and Analytics',
    )


    class Meta:
        ordering = ['-date_published']
        verbose_name = 'News and Analytics'
        verbose_name_plural = 'News and Analytics'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


@receiver(post_delete, sender=InformationPagesModel)
@receiver(post_delete, sender=OpportunitiesModel)
@receiver(post_delete, sender=NewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))
pre_save.connect(pre_save_post_receiver, sender=InformationPagesModel)


def pre_save_opportunities_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))
pre_save.connect(pre_save_post_receiver, sender=OpportunitiesModel)


def pre_save_photo_bank_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))
pre_save.connect(pre_save_photo_bank_receiver, sender=PhotoBankModel)


def pre_save_news_bank_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))
pre_save.connect(pre_save_news_bank_receiver, sender=NewsModel)