# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Authors(models.Model):
    first_name =models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors)
    published_date = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    in_print = models.BooleanField()


# Create your models here
