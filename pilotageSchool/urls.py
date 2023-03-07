from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('CreationDeCompte', views.register_page, name='CreationDeCompte'),
    path('', views.index, name='index'),
]
