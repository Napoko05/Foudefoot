
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),  # Ajoute cette ligne
    path('pubs/', views.pubs, name='pubs'),
    path('abonnement_step1/', views.abonnement_step1, name='abonnement_step1'),
    path('abonnement_step2/', views.abonnement_step2, name='abonnement_step2'),
    path('abonnement_step3/', views.abonnement_step3, name='abonnement_step3'),
    path('abonnement/paiement/', views.abonnement_step4, name='abonnement_step4'),
    path('utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('envoyer_pub/', views.envoyer_pub, name='envoyer_pub'),
    
]