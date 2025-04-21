from django.urls import path
from . import views


urlpatterns = [
    path('cars/', views.CarListCreateView.as_view(), name='car-list'),

]