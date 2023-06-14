from django.urls import path 
from . import views 


urlpatterns = [
    path('books/', views.loadBooksPage, name='books'),
    path('book/<slug:slug>/', views.loadSingleBookPage, name='book')
]