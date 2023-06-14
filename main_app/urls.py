from django.urls import path
from . import views 


urlpatterns = [
    path('', views.loadIndexPage, name='home'),
    path('logout/', views.logout, name='logout'),

]