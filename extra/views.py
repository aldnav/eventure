# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ast

from django.views.generic import TemplateView

from .mixins import JSONView
from activity.models import Activity


class HomeView(TemplateView):
    template_name = 'extra/index.html'


class ActivitySerializer(object):

    def serialize(self, instance, fields):
        serialized = {}
        for field in fields:
            try:
                serialized[field] = getattr(instance, field, None)
            except Exception as e:
                print e
        return serialized

serializer = ActivitySerializer()


class ActivityResourceView(JSONView):

    def get_context_data(self, **kwargs):
        context = super(ActivityResourceView, self).get_context_data(**kwargs)
        context['objects'] = []

        filters = ast.literal_eval(self.request.GET.get('filters'))
        query_set = Activity.objects.filter(**filters)
        fields = ['pk', 'actor', 'object_ref', 'target', 'verb', 'published',
                  'title', 'summary']
        for obj in query_set:
            obj = serializer.serialize(obj, fields)
        return context
