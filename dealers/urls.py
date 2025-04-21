from django.urls import path
from . import views


urlpatterns = [
    path('dealers/', views.DealerListCreateVie.as_view(), name='dealer-list'),

]