
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('api_auth.urls')),
    path('', include('main_app.urls')),
]
