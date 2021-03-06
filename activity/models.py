# -*- coding: utf-8 -*-
"""
Aims to follow this spec: http://activitystrea.ms/specs/atom/1.0/
"""

from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.humanize.templatetags.humanize import naturaltime


class Activity(models.Model):
    """An activity consists of an actor, a verb and an object.

    Implied shorthand format:
        <actor> <verb> <target> <time>
    Full entry format:
        <actor> <verb> <object> <target> <time>

    Examples:
        <wendy> <liked> a <tweet> <5 minutes ago>
        <ching> <added> a <Happy Birthday Song> to <playlist> <a minute ago>
    """
    # Actor.
    actor_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                   related_name='activities_actor')
    actor_id = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_type', 'actor_id')

    # Object
    object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                    related_name='activities')
    object_id = models.PositiveIntegerField()
    object_ref = GenericForeignKey('object_type', 'object_id')

    verb = models.ForeignKey('Verb', on_delete=models.CASCADE,
                             related_name='activities')

    # Target
    # "Wendy saved a song to her playlist", the target of the activity is
    # "playlist"
    target_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                    related_name='activities_target',
                                    null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey('target_type', 'target_id')

    published = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True)
    summary = models.CharField(max_length=255, blank=True)

    @property
    def published_verbose(self):
        return naturaltime(self.published)


class Verb(models.Model):
    """The Object of the Activity Construct """
    name = models.CharField(max_length=64, unique=True)
    # @NOTE: Handle tenses as properties

    def __unicode__(self):
        return self.name
