from django.views.generic import TemplateView
from django.http import Http404
from voting.models import Voting
from store.models import Vote
from census.models import Census
from base import mods
import datetime
from datetime import date
from django.utils import timezone



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


class DashboardEstadisticas(TemplateView):
    template_name = 'visualizer/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            estadisticas = Estadisticas.getEstadisticas(self)

            context['<<'] = estadisticas[0]
            context['numVotacionesSinEmpezar'] = estadisticas[1]
            context['numVotacionesActivas'] = estadisticas[2]
            context['mediaOpciones'] =estadisticas[3]
            context['todosVotos'] = estadisticas[4]

            #Añadiendo estadísticas de votaciones por mes
            context['votacionesEnero'] = estadisticas[5]
            context['votacionesFebrero'] = estadisticas[6]
            context['votacionesMarzo'] = estadisticas[7]
            context['votacionesAbril'] = estadisticas[8]
            context['votacionesMayo'] = estadisticas[9]
            context['votacionesJunio'] = estadisticas[10]
            context['votacionesJulio'] = estadisticas[11]
            context['votacionesAgosto'] = estadisticas[12]
            context['votacionesSeptiembre'] = estadisticas[13]
            context['votacionesOctubre'] = estadisticas[14]
            context['votacionesNoviembre'] = estadisticas[15]
            context['votacionesDiciembre'] = estadisticas[16]

        except:
            raise Http404

        return context


class Estadisticas():

    def getEstadisticas(self):
        estadisticas =[]


        numVotacionesTotales = Voting.objects.all().count()
            #Voting.objects.filter(start_date__lte=date.today()).count()

        suma = 0
        for votacion in Voting.objects.all():
            if (votacion.question.options.none):
                break
            else:
                for opcion in votacion.question.options.option:
                    suma += 1

        numVotacionesActivas = 0
        numVotacionesSinEmpezar = 0
        for votacion in Voting.objects.all():
            hoy = datetime.date.today()
            if (str(votacion.start_date) <= str(hoy)) and (str(votacion.end_date) >= str(hoy)):
                numVotacionesActivas +=1
            elif (str(votacion.start_date) > str(hoy)):
                numVotacionesSinEmpezar +=1


        votacionesEnero = Voting.objects.filter(start_date__month='01').count()
        votacionesFebrero = Voting.objects.filter(start_date__month='02').count()
        votacionesMarzo = Voting.objects.filter(start_date__month='03').count()
        votacionesAbril = Voting.objects.filter(start_date__month='04').count()
        votacionesMayo = Voting.objects.filter(start_date__month='05').count()
        votacionesJunio = Voting.objects.filter(start_date__month='06').count()
        votacionesJulio = Voting.objects.filter(start_date__month='07').count()
        votacionesAgosto = Voting.objects.filter(start_date__month='08').count()
        votacionesSeptiembre = Voting.objects.filter(start_date__month='09').count()
        votacionesOctubre = Voting.objects.filter(start_date__month='10').count()
        votacionesNoviembre = Voting.objects.filter(start_date__month='11').count()
        votacionesDiciembre = Voting.objects.filter(start_date__month='12').count()



        mediaOpcionesPorVotacion = suma / numVotacionesTotales
        todosVotos = Census.objects.all().count()

        estadisticas.append(numVotacionesTotales)  #0
        estadisticas.append(numVotacionesSinEmpezar) #1
        estadisticas.append(numVotacionesActivas) #2
        estadisticas.append(mediaOpcionesPorVotacion) #3
        estadisticas.append(todosVotos)  # 4
        #Añadiendo estadísticas votaciones por meses
        estadisticas.append(votacionesEnero) #5
        estadisticas.append(votacionesFebrero) #6
        estadisticas.append(votacionesMarzo) #7
        estadisticas.append(votacionesAbril) #8
        estadisticas.append(votacionesMayo) #9
        estadisticas.append(votacionesJunio) #10
        estadisticas.append(votacionesJulio) #11
        estadisticas.append(votacionesAgosto) #12
        estadisticas.append(votacionesSeptiembre) #13
        estadisticas.append(votacionesOctubre) #14
        estadisticas.append(votacionesNoviembre) #15
        estadisticas.append(votacionesDiciembre) #16


    #    numVotosVotaciones = dict()
    #    for votacion in Voting.objects.all():
    #        idVotacion = votacion.id
    #        Vote.objects.filter(voting_id=idVotacion).count()






        return estadisticas



