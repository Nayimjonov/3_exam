from django.urls import path
from . import views


urlpatterns = [
    path('dealers/', views.DealerListCreateView.as_view(), name='dealer-list-create'),
    path('dealers/<int:pk>/', views.DealerRetrieveUpdateDestroyView.as_view(), name='dealer-detail'),

]