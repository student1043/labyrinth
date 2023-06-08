from django.urls import path
from . import views

urlpatterns = [
    path('solve-labyrinth/', views.solve_labyrinth, name='solve-labyrinth'),
]
