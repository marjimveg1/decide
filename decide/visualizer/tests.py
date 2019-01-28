from django.test import TestCase

# Create your tests here.

from base.tests import BaseTestCase
from voting.models import Voting, Question
from django.utils import timezone
from visualizer.views import Estadisticas
import datetime
from datetime import date

#Para poder usar months en lugar de days debe ser una versión superior que no es compatible

class VisualizerTest(BaseTestCase):

    def test_num_votaciones_totales(self):
        pregunta = Question(desc='pregunta1', )
        pregunta.save()
        votacion0 = Voting(pk=1000,
                             desc='descripcionVotacion0',
                             name='votacion0',
                             question = pregunta,
                             start_date=timezone.now() + datetime.timedelta(days=65),
                             )
        votacion1 = Voting(pk=1001,
                          desc='descripcionVotacion1',
                          name='votacion1',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=date.today() +datetime.timedelta (days=41),
                          )
        votacion2 = Voting(pk=1002,
                          desc='descripcionVotacion2',
                          name='votacion2',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=22),
                          )
        votacion3 = Voting(pk=1003,
                          desc='descripcionVotacion3',
                          name='votacion3',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=1),
                          )
        votacion4 = Voting(pk=1004,
                          desc='descripcionVotacion3',
                          name='votacion4',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=169),
                          )
        votacion0.save()
        votacion1.save()
        votacion2.save()
        votacion3.save()
        votacion4.save()



        resultados = Estadisticas.getEstadisticas(self)
        self.assertTrue(resultados[0] ==5)

    def test_num_votaciones_totales_falso(self):
        pregunta = Question(desc='pregunta1', )
        pregunta.save()
        votacion0 = Voting(pk=1001,
                             desc='descripcionVotacion1',
                             name='votacion1',
                             question = pregunta,
                             start_date=timezone.now() ,
                             end_date=timezone.now()+ datetime.timedelta(days=2),
                             )
        votacion1 = Voting(pk=1002,
                          desc='descripcionVotacion2',
                          name='votacion2',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=5),
                          )
        votacion2 = Voting(pk=1003,
                          desc='descripcionVotacion3',
                          name='votacion3',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=2),
                          )
        votacion3 = Voting(pk=1004,
                          desc='descripcionVotacion3',
                          name='votacion4',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days =8),
                          )
        votacion0.save()
        votacion1.save()
        votacion2.save()
        votacion3.save()

        resultados = Estadisticas.getEstadisticas(self)
        self.assertFalse(resultados[0] == 5)


    def test_numVotacionesSinEmpezar(self):
        pregunta = Question(desc='pregunta1', )
        pregunta.save()
        votacion0 = Voting(pk=1000,
                             desc='descripcionVotacion0',
                             name='votacion0',
                             question = pregunta,
                             start_date=timezone.now() + datetime.timedelta(days=65),
                            end_date=date.today() + datetime.timedelta(days=71),
                             )
        votacion1 = Voting(pk=1001,
                          desc='descripcionVotacion1',
                          name='votacion1',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=date.today() +datetime.timedelta (days=41),
                          )
        votacion2 = Voting(pk=1002,
                          desc='descripcionVotacion2',
                          name='votacion2',
                          question=pregunta,
                          start_date=timezone.now() + datetime.timedelta(days=15),
                          end_date=timezone.now() + datetime.timedelta(days=22),
                          )
        votacion3 = Voting(pk=1003,
                          desc='descripcionVotacion3',
                          name='votacion3',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=1),
                          )
        votacion4 = Voting(pk=1004,
                          desc='descripcionVotacion3',
                          name='votacion4',
                          question=pregunta,
                          start_date=timezone.now()+ datetime.timedelta(days=70),
                          end_date=timezone.now() + datetime.timedelta(days=169),
                          )
        votacion0.save()
        votacion1.save()
        votacion2.save()
        votacion3.save()
        votacion4.save()



        resultados = Estadisticas.getEstadisticas(self)
        self.assertTrue(resultados[1] ==3)

    def test_numVotacionesSinEmpezar_falso(self):
        pregunta = Question(desc='pregunta1', )
        pregunta.save()
        votacion0 = Voting(pk=1000,
                             desc='descripcionVotacion0',
                             name='votacion0',
                             question = pregunta,
                             start_date=timezone.now() + datetime.timedelta(days=65),
                            end_date=date.today() + datetime.timedelta(days=71),
                             )
        votacion1 = Voting(pk=1001,
                          desc='descripcionVotacion1',
                          name='votacion1',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=date.today() +datetime.timedelta (days=41),
                          )
        votacion2 = Voting(pk=1002,
                          desc='descripcionVotacion2',
                          name='votacion2',
                          question=pregunta,
                          start_date=timezone.now() + datetime.timedelta(days=15),
                          end_date=timezone.now() + datetime.timedelta(days=22),
                          )
        votacion3 = Voting(pk=1003,
                          desc='descripcionVotacion3',
                          name='votacion3',
                          question=pregunta,
                          start_date=timezone.now(),
                          end_date=timezone.now() + datetime.timedelta(days=1),
                          )
        votacion4 = Voting(pk=1004,
                          desc='descripcionVotacion3',
                          name='votacion4',
                          question=pregunta,
                          start_date=timezone.now()+ datetime.timedelta(days=70),
                          end_date=timezone.now() + datetime.timedelta(days=169),
                          )
        votacion0.save()
        votacion1.save()
        votacion2.save()
        votacion3.save()
        votacion4.save()

        resultados = Estadisticas.getEstadisticas(self)
        self.assertFalse(resultados[1] == 5)

