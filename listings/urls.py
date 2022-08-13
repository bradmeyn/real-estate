from django.urls import path

from . import views
# path /listings
urlpatterns = [
    # path, method to call, name
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search',views.search, name='search')

]