from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('school/', include('pilotageSchool.urls')),
    path('admin/', admin.site.urls),

]
