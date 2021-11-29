
from django.urls import path
from . import views
urlpatterns = [
    path('gettemp', views.gettemp),
    path('gethumid',views.gethumid),
    path('getmoist',views.getmoist),
]
