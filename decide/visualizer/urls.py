from django.urls import path
from .views import VisualizerView, VisualizerIndex, VisualizerTodasVotaciones


urlpatterns = [
    path('inicio/', VisualizerIndex.as_view()),
    path('todasVotaciones/', VisualizerTodasVotaciones.as_view()),
    path('mostrar/<int:voting_id>/', VisualizerView.as_view()),
]
