from django.db import models

# Create your models here.
from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    est_abonne = models.BooleanField(default=False)

class Journaliste(models.Model):
    nom = models.CharField(max_length=100)
    identifiant = models.CharField(max_length=50)

class Pub(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)
    type_pub = models.CharField(max_length=50, choices=[('National', 'National'), ('International', 'International')])

class Abonnement(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='abonnements')
    date_souscription = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=True)