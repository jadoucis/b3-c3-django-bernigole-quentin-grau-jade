from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pilotageSchool.urls')),
    path('admin/', admin.site.urls),

]
