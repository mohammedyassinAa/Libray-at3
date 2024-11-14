from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()

    def __str__(self):
        return self.nom

class Livre(models.Model):
    titre = models.CharField(max_length=200)
    date_publication = models.DateField()
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
