# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy_djangoitem import DjangoItem

# Create your models here.
class WebToScrap(models.Model):

    name = models.CharField(max_length=200)
    url = models.URLField()
    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)
    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name
    

class Web(models.Model):

    class Meta:
        verbose_name = "Web"
        verbose_name_plural = "Webs"

    titulo = models.CharField(max_length=254, blank=True)
    descripcion = models.TextField(blank=True)
    imagen = models.CharField(max_length=500, blank=True)
    precio = models.CharField(max_length=50, blank=True)
    ubicacion = models.CharField(max_length=500, blank=True)
    # webToScrap = models.ForeignKey(WebToScrap)  
    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)


    def __unicode__(self):
        return self.titulo
    
class WebItem(DjangoItem):
    django_model = Web