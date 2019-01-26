from django.views.generic import TemplateView
from django.conf import settings
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from base import mods

class VisualizerIndex(TemplateView):
    template_name = 'visualizer/visualizerIndex.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class VisualizerView(TemplateView):
    template_name = 'visualizer/visualizer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vid = kwargs.get('voting_id', 0)

        try:
            r = mods.get('voting', params={'id': vid})
            context['votacion'] = r[0]
        except:
            raise Http404

        return context

class VisualizerVotacion(TemplateView):
    template_name = 'visualizer/visualizerVotacion.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VisualizerTodasVotaciones(TemplateView):
    template_name = 'visualizer/visualizerTodasVotaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            todasVotaciones = mods.get('voting')
            context['votaciones'] = todasVotaciones


        except:
            raise Http404

        return context

