from django.urls import path
from . import views

urlpatterns = [
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/<int:id>/', views.detail_livre, name='detail_livre'),
]
