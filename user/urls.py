from django.urls import path
from .views import *

urlpatterns =[
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutVeiw.as_view(),name='logout'),
]