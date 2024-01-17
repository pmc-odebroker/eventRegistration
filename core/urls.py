from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_page , name=' home'),
    path('event/<str:pk>/', views.event_page, name='event'),
    path('event-confikrmation/<str:pk>', views.registration_confirmation, name='registration_confirmation')
]
