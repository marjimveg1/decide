from django.urls import path
from .views import VisualizerView, VisualizerIndex, VisualizerTodasVotaciones


urlpatterns = [
    path('sobreNosotros/', VisualizerIndex.as_view()),
    path('votaciones/', VisualizerTodasVotaciones.as_view()),
    path('mostrar/<int:voting_id>/', VisualizerView.as_view()),
]
