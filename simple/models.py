# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Outfit(models.Model):
    style = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

