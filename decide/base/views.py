from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from base import mods

# Create your views here.
class Base(TemplateView):
    template_name = 'base/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Index(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context