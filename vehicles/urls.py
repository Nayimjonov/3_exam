from django.urls import path
from . import views


urlpatterns = [
    path('makes/', views.MakeListView.as_view(), name='make-list'),
    path('makes/<int:make_id>/models/', views.ModelListByMakeView.as_view(), name='model-list-by-make'),
    path('body-types/', views.BodyTypeListView.as_view(), name='body-types'),
    path('features/', views.FeatureListView.as_view(), name='features'),

]