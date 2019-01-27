from django.test import TestCase

# Create your tests here.

from base.tests import BaseTestCase
from voting.models import Voting, Question
from django.utils import timezone
from visualizer.views import Estadisticas


class VisualizerTest(BaseTestCase):

    def test1(self):
        pregunta = Question(desc='pregunta1', )
        pregunta.save()
        votacion = Voting(pk=1000,
                             desc='descripcionVotacion1',
                             name='votacion1',
                             question = pregunta,
                             start_date=timezone.now(),
                             )
        votacion.save()



        resultados = Estadisticas.getEstadisticas(self)
        self.assertEqual(resultados[0] ==1)


