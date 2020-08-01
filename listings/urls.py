from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing' ),
    path('search', views.search, name='search'),
 
]
# we are using <int:listing_id> to take id as parameter