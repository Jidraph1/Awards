from importlib.resources import path
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name = 'index'),
    path('update-profile',views.update_profile, name='update_profile'),
    path('profile/<pk>',views.profile, name = 'profile'),
    path('search/',views.search_results, name='search_results'),
    path('submit-project',views.submit_project, name='submit_project'),
    path('site_details/<int:id>/',views.site_details,name='site_details'),
]