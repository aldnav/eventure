# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core import serializers
from django.test import TestCase

from .views import ActivitySerializer
from .models import Post
from activity.models import Activity, Verb


class SerializerTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='Gilfoyle', password='pass')
        self.user2 = User.objects.create_user(username='Dinesh', password='pass')
        self.post = Post.objects.create(title='I Have a Dream')

    def test_serialize(self):
        like = Verb.objects.create(name='like')
        action = Activity.objects.create(
            actor=self.user1,
            verb=like,
            object_ref=self.post,
        )
        serializer = ActivitySerializer()
        serialized = serializer.serialize(action, ['pk', 'published'])
        self.assertIsNotNone(serialized)
        self.assertEquals(serialized['pk'], action.pk)
        # data = serializers.serialize('json', [action])
