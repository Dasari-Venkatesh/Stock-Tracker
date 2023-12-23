from django.urls import path, include
from . import views

urlpatterns = [
    path('stockpicker/',views.stockPicker, name = 'stockpicker'),
    path('stocktracker/',views.stockTracker, name ='stocktracker' ),

]