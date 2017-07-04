
from django.views.generic import View
from django.http import JsonResponse


class JSONView(View):
    response_class = JsonResponse

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.response_class(context, status=200)

    def get_context_data(self, **kwargs):
        return {}
