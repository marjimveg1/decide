from django.urls import path
from .views import VisualizerView, VisualizerIndex


urlpatterns = [
    path('inicio/', VisualizerIndex.as_view()),
    path('display/<int:voting_id>/', VisualizerView.as_view()),
]
