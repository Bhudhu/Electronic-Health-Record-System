from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('search_patient/', views.search_patient, name='search_patient'),
    path('patient_card/<int:pk>/', views.patient_card, name='patient_card'),
    path('edit_patient/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('fetch_patient_by_name/', views.fetch_patient_by_name, name='fetch_patient_by_name'),
    path('logout/', views.logout_view, name='logout'),

]
