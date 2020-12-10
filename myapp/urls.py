from django.urls import path
from myapp.views import *

app_name = "myapp"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('filter-by-month/', filterbymonth, name="filterbymonth"),
]
