# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView

from .mixins import JSONView
from .serializer import activity_serializer
from activity.models import Activity


class HomeView(TemplateView):
    template_name = 'extra/index.html'


class ActivityResourceView(JSONView):
    serializer = activity_serializer

    def get_context_data(self, **kwargs):
        context = super(ActivityResourceView, self).get_context_data(**kwargs)
        context['objects'] = []
        filters = self.request.GET.dict()
        query_set = Activity.objects.filter(**filters)
        fields = ['pk', 'actor', 'object_ref', 'target', 'verb', 'published',
                  'title', 'summary']
        for obj in query_set:
            obj = self.serializer.serialize(obj, fields)
        return context
