from importlib.resources import path
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name = 'index'),
    path('update-profile',views.update_profile, name='update_profile'),
    path('profile/<pk>',views.profile, name = 'profile'),
]