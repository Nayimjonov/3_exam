from django.urls import path
from . import views


urlpatterns = [
    path('listings/', views.ListingListCreateView.as_view(), name='listing-list'),
    path('listings/<int:pk>/', views.ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),

    path('listings/<int:listing_id>/images/', views.ListingImagesListView.as_view(), name='listing-images-list'),
    path('listings/<int:listing_id>/images/add/', views.ListingImagesCreateView.as_view(),
         name='listing-images-create'),
    path('listings/<int:listing_id>/images/<int:pk>/', views.ListingImageDeleteView.as_view(),
         name='listing-image-delete'),
    path('listings/<int:listing_id>/price-history/', views.ListingPriceHistoryView.as_view(),
         name='listing-price-history'),
    path('listings/featured/', views.FeaturedListingsView.as_view(), name='featured-listings'),
    path('listings/my/', views.MyListingsView.as_view(), name='my-listings'),
]