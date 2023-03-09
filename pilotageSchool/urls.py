from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('CreationDeCompte', views.register_page, name='CreationDeCompte'),
    path('Reservations', views.reservations_pages, name='Reservations'),
    path('reservation/<str:school_name>', views.choose_reservation, name='choose_reservation'),
    path('', views.index, name='index'),
]
