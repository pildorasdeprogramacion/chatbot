from django.urls import path
from .views import MensajeView
from .views import dashboard_view

urlpatterns = [
    path('api/mensaje/', MensajeView.as_view(), name='mensaje'),
    path('dashboard/', dashboard_view, name='dashboard'), 
]
