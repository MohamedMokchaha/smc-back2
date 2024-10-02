from django.urls import path

from demandes.views import save_application

urlpatterns = [
    path('save/', save_application, name='save_application'),
]
