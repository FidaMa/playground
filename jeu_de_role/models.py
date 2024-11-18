from django.db import models

class Lieu(models.Model):
    id_lieu = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    type_lieu = models.CharField(max_length=50, choices=[('forteresse', 'Forteresse'), ('forêt', 'Forêt'), ('village', 'Village'), ('donjon', 'Donjon')])
    disponibilite = models.CharField(max_length=20, choices=[('libre', 'Libre'), ('occupé', 'Occupé')])
    niveau_acces = models.IntegerField(default=1)
    capacite_max = models.IntegerField(default=10)
    photo = models.ImageField(upload_to='lieux/')

    def __str__(self):
        return self.nom

class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    nom = models.CharField(max_length=100)
    etat = models.CharField(max_length=20)
    niveau = models.IntegerField(default=1)
    type = models.CharField(max_length=20, choices=[('Guerrier', 'Guerrier'), ('Mage', 'Mage'), ('Archer', 'Archer')])
    team = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='characters/')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
