from django.views.generic import TemplateView
from django.http import Http404
from voting.models import Voting
from census.models import Census
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


class DashboardEstadisticas(TemplateView):
    template_name = 'visualizer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            estadisticas = Estadisticas.getEstadisticas()

            context['numVotacionesTotales'] = estadisticas[0]
            context['numVotacionesSinEmpezar'] = estadisticas[1]
            context['numVotacionesActivas'] = estadisticas[2]
            context['mediaOpciones'] =estadisticas[3]
            context['tantoPorCienVotacionesCerradas'] = estadisticas[4]
            context['todosVotos'] = estadisticas[5]

        except:
            raise Http404

        return context


class Estadisticas():

    def getEstadisticas(self):
        estadisticas =[]

        numVotacionesTotales = Voting.objects.all().count()
        numVotacionesSinEmpezar = Voting.objects.filter(start_date=None)
        numVotacionesActivas = numVotacionesTotales - numVotacionesSinEmpezar

        suma = 0
        for votacion in Voting.objects.all():
            a = votacion
            if (votacion.question.options.none):
                break
            else:
                for opcion in votacion.question.options.option:
                    suma += 1

        mediaOpcionesPorVotacion = suma / numVotacionesTotales
        tantoPorCienVotacionesCerradas = ((numVotacionesTotales - numVotacionesSinEmpezar) / numVotacionesTotales) * 100

        todosVotos = Census.objects.all().count()

        estadisticas.append(numVotacionesTotales) #0
        estadisticas.append(numVotacionesSinEmpezar) #1
        estadisticas.append(numVotacionesActivas) #2
        estadisticas.append(mediaOpcionesPorVotacion) #3
        estadisticas.append(tantoPorCienVotacionesCerradas) #4
        estadisticas.append(todosVotos)  # 5
        estadisticas.append(todosVotos)  # 6

        return estadisticas



