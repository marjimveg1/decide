from django.test import TestCase

# Create your tests here.

from base.tests import BaseTestCase
from voting.models import Voting, Question
from django.utils import timezone
from visualizer.views import Estadisticas


class VisualizerTest(BaseTestCase):

    def test1(self):
        self.question = Question(desc='pregunta1', voting=self.voting)
        self.question.save()
        self.voting = Voting(pk=1000,
                             desc='descripcionVotacion1',
                             name='votacion1',
                             start_date=timezone.now(),
                             )


        self.voting.save()
        resultados = Estadisticas.getEstadisticas()
        self.assertEqual(resultados[0] ==1)


