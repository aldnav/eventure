# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Activity, Verb
from extra.models import Game, Event, Post, Video


class ActivityModelTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='Gilfoyle', password='pass')
        self.user2 = User.objects.create_user(username='Dinesh', password='pass')
        self.game = Game.objects.create(title='Super Mario Kart')
        self.event = Event.objects.create(title='Book Signing')
        self.post = Post.objects.create(title='I Have a Dream')
        self.video = Video.objects.create(title='All Time Top 10')

    def test_implicit_activity(self):
        """Tests activity with no target"""
        play = Verb.objects.create(name='plays')
        activity = Activity.objects.create(
            actor=self.user1,
            object_ref=self.game,
            verb=play,
            title='{} {} {}'.format(self.user1, play, self.game)
        )
        print activity.title
        self.assertEqual(
            activity.title, '{} {} {}'.format(self.user1, play, self.game))

    def test_explicit_activity(self):
        """Tests activity with target"""
        mention = Verb.objects.create(name='mention')
        activity = Activity.objects.create(
            actor=self.user2,
            object_ref=self.user1,
            verb=mention,
            target=self.video,
            title='{} {} {} on {}'.format(
                self.user2, mention, self.user1, self.video)
        )
        print activity.title
        self.assertEqual(
            activity.title, '{} {} {} on {}'.format(
                self.user2, mention, self.user1, self.video))
