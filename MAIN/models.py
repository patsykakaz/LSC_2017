#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.sites.models import *
from django.utils.translation import ugettext, ugettext_lazy as _

from settings import MEDIA_ROOT
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.utils.sites import current_site_id, current_request
from mezzanine.utils.models import upload_to
# from colorfield.fields import ColorField


class Client(Page, RichText):
    logo = FileField(verbose_name=_("Logo"),
        upload_to=upload_to("MAIN.Client", "Client"),
        format="Image", max_length=255, null=False, blank=False, default=False)
    # illustration = FileField(verbose_name=_("Illustration"),
        # upload_to=upload_to("MAIN.Client", "Client"),
        # format="Image", max_length=255, null=True, blank=True, default=False)
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        parent = Page.objects.get(title='CLIENTS')
        self.parent = parent
        self.in_menus = []
        super(Client, self).save(*args, **kwargs)

class Campagne(Page, RichText):
    clientKey = models.ForeignKey(Client)
    illustration = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.Campagne", "Campagne"),
        format="Image", max_length=255, null=False, blank=False)
    baseline = models.CharField(max_length=255,null=True, blank=True)
    level = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        parent = Page.objects.get(title='CAMPAGNES')
        self.parent = parent
        self.in_menus = []
        super(Campagne, self).save(*args, **kwargs)

class CampagneCaptions(models.Model):
    Campagne = models.ForeignKey("Campagne")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.Campagne", "Campagne"),
        format="Image", max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Captions'

class Worker(Page,RichText):
    job = models.CharField(max_length=255,)
    picture = FileField(verbose_name=_("Picture"),
    upload_to=upload_to("MAIN.Worjer", "Worker"),
    format="Image", max_length=255, null=False, blank=False, default=False)
    level = models.IntegerField(default=0)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # in_menus empty pour exclure les archives des content_tree
        parent = Page.objects.get(title='TEAM')
        self.parent = parent
        self.in_menus = []
        super(Worker, self).save(*args, **kwargs)


class FakeBlog(Page, RichText):
    baseline = models.CharField(max_length=255, null=True, blank=True, verbose_name='baseline')
    illustration = FileField(verbose_name=_("Illustration"),
        upload_to=upload_to("MAIN.FakeBlog", "FakeBlog"),
        format="Image", max_length=255, null=False, blank=False, default=False)

    class Meta:
        verbose_name = 'FAKE_BLOG'

    def save(self, *args, **kwargs):
        parent = Page.objects.get(title='FAKE_BLOG')
        self.parent = parent
        self.in_menus = []
        super(FakeBlog, self).save(*args, **kwargs)

class FakeBlogGalery(models.Model):
    FakeBlog = models.ForeignKey("FakeBlog")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("MAIN.FakeBlog", "FakeBlog"),
        format="Image", max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    display_size = models.IntegerField(default=6,help_text='taille de l\'image. Entrez un nombre pair, entre 2 et 12.',null=True, blank=True)

    class Meta:
        verbose_name = 'Gallerie FakeBlog'


