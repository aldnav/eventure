# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic import TemplateView, View

from .mixins import JSONView
from .models import Profile, Note, Game
from .serializer import activity_serializer
from activity.models import Activity, Verb


class HomeView(TemplateView):
    template_name = 'extra/index.html'


class ActivityResourceView(JSONView):
    serializer = activity_serializer

    def get_context_data(self, **kwargs):
        context = super(ActivityResourceView, self).get_context_data(**kwargs)
        context['objects'] = []
        filters = self.request.GET.dict()
        query_set = Activity.objects.filter(**filters)
        print query_set
        fields = ['pk', 'actor', 'object_ref', 'target', 'verb',
                  'published_verbose', 'title', 'summary']
        for obj in query_set:
            # obj = self.serializer.serialize(obj, fields)
            context['objects'].append(obj)
        return context


class DrumKitView(TemplateView):
    template_name = 'drumkit/index.html'

    def post(self, request, *args, **kwargs):
        note = request.POST.get('note')
        ip_address = self.get_client_ip()
        verb = Verb.objects.get(name='play')
        game = Game.objects.get(title='Drumkit')
        note, _ = Note.objects.get_or_create(title=note)
        profiles = Profile.objects.filter(ip_address=ip_address)
        if profiles.count() == 0:
            user = Profile.objects.create_anon_user(ip_address).owner
        else:
            user = profiles.first().owner
        activity = Activity.objects.create(
            actor=user,
            object_ref=note,
            verb=verb,
            target=game,
            title='{} {} {} {}'.format(
                user.username, verb.name, note.title, game.title)
        )
        return JsonResponse({'activity': activity.pk})

    def get_client_ip(self, **kwargs):
        request = self.request
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
