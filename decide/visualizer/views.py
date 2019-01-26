from django.views.generic import TemplateView
from django.http import Http404
from voting.models import Voting
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


class VisualizerTodasVotaciones(TemplateView):
    template_name = 'visualizer/visualizerTodasVotaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            todasVotaciones = Voting.objects.all()
            context['votaciones'] = todasVotaciones

        except:
            raise Http404

        return context


class Dashboard(TemplateView):
    template_name = 'visualizer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            numVotacionesTotales = Voting.objects.all().count()
            numVotacionesSinEmpezar = Voting.objects.filter(start_date=None).count()
            numVotacionesSinTerminar = Voting.objects.filter(end_date=None).count()
            numVotacionesSinTerminar = Voting.objects.filter(end_date=None).count()


            suma = 0
            for votacion in Voting.objects.all():
                a = votacion
                if(votacion.question.options.none):
                    break
                else:
                    for opcion in votacion.question.options.option:
                        suma +=1
            mediaOpcionesPorVotacion = suma/numVotacionesTotales
            tantoPorCienVotacionesCerradas = (numVotacionesSinEmpezar + numVotacionesSinTerminar)/numVotacionesTotales *100

            context['numVotacionesTotales'] = numVotacionesTotales
            context['numVotacionesSinEmpezar'] = numVotacionesSinEmpezar
            context['numVotacionesSinTerminar'] = numVotacionesSinTerminar
            context['mediaOpciones'] =mediaOpcionesPorVotacion
            context['tantoPorCienVotacionesCerradas'] = tantoPorCienVotacionesCerradas

        except:
            raise Http404

        return context


