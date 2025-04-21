from django.urls import path
from . import views


urlpatterns = [
    path('dealers/', views.DealerListCreateView.as_view(), name='dealer-list-create'),

]