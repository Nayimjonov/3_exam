from django.urls import path
from . import views


urlpatterns = [
    path('makes/', views.MakeListView.as_view(), name='make-list'),

]