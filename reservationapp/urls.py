from django.urls import path
from . import views  # Import your views file

urlpatterns = [
    path('home_page/', views.home_page, name='home_page'),
    path('login/', views.login_view, name='login'),  # Login page
    path('sign/', views.sign_view, name='sign'),  # Login page
    path('nav/', views.nav_view, name='nav'),  # Login page
    path('index/', views.index_view, name='index'),  # Login page
    path('register/', views.register, name='register'),
    path('users/', views.user_list, name='user_list'),
    path('make-reservation/', views.make_reservation, name='make_reservation'),
    path('view-reservations/', views.view_reservations, name='view_reservations'),



]




