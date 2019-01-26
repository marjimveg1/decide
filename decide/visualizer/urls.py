from django.urls import path
from .views import VisualizerView, VisualizerIndex, VisualizerVotacion, VisualizerTodasVotaciones


urlpatterns = [
    path('inicio/', VisualizerIndex.as_view()),
    path('votacion/', VisualizerVotacion.as_view()),
    path('todasVotaciones/', VisualizerTodasVotaciones.as_view()),
    path('display/<int:voting_id>/', VisualizerView.as_view()),
]
