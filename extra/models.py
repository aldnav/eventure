# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.db import models

allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


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


class Application(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class ProfileManager(models.Manager):

    def create_anon_user(self, ip_address):
        username = get_random_string(length=4, allowed_chars=allowed_chars)
        user = User(username=username, first_name='Anon', last_name='User')
        user.set_unusable_password()
        user.save()
        profile = Profile.objects.create(owner=user, ip_address=ip_address)
        return profile


class Profile(models.Model):
    owner = models.OneToOneField(User, related_name='profile')
    ip_address = models.CharField(max_length=15, blank=True)

    objects = ProfileManager()
