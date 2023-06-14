from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.loadLoginPage, name='login'),
    path('token/', views.loadTokenPage, name='token'),
    path('activate/<uidb64>/<token>/', views.activate_token, name='activate'),
    path('signup/', views.loadSignupPage, name='signup'),
]