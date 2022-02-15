
from django.urls import path
from . import views
urlpatterns = [
    path('gettemp', views.gettemp),
    path('gethumid',views.gethumid),
    path('getmoist',views.getmoist),
    path('updatetemp/<str:temp>', views.updatetemp),
    path('updatehumid/<str:humid>',views.updatehumid),
    path('updatemoist/<str:moist>',views.updatemoist),
    path('toggle',views.toggleswitch),
]
