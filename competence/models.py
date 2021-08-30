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
    file_path = 'competence/{title}-{filename}'.format(
                title=str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class CompetenceModel(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['date_published']
        verbose_name = 'Competence'
        verbose_name_plural = 'Competence'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


@receiver(post_delete, sender=CompetenceModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))
pre_save.connect(pre_save_post_receiver, sender=CompetenceModel)
