# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
