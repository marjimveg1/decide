from django.urls import path
from .views import Base, Index

urlpatterns = [
    path('inicio/', Base.as_view()),
    path('inicio2/', Index.as_view()),
]
