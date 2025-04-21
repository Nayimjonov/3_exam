from django.urls import path
from . import views


urlpatterns = [
    path('dealers/', views.DealerListCreateView.as_view(), name='dealer-list-create'),
    path('dealers/<int:pk>/', views.DealerRetrieveUpdateDestroyView.as_view(), name='dealer-detail'),
    path('dealers/<int:dealer_id>/listings/', views.DealerListingsView.as_view(), name='dealer-listings'),

]