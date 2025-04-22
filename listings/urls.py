from django.urls import path
from . import views


urlpatterns = [
    path('listings/', views.ListingListCreateView.as_view(), name='listing-list'),
]