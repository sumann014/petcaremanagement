from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pets/', views.pet_list, name='pet_list'),
    path('owners/', views.owner_list, name='owner_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('add-pet/', views.add_pet, name='add_pet'),
    path('add-appointment/', views.add_appointment, name='add_appointment'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


]
