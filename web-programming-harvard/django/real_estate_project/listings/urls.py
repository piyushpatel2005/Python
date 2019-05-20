from django.urls import path

from . import views

urlpatterns = [
    # empty means it will be used for /listings
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
