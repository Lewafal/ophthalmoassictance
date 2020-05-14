from django.db import models
from django.utils import timezone


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    numero_dossier=models.CharField(max_length=50)
    description = models.TextField(null=True)
    date_naissance = models.DateField(null=True)
    image = models.ImageField(null=True)
    date_enregistrement=models.DateTimeField(default=timezone.now, verbose_name ="Date et heure d'enregistrement du patient")

    class Meta:
        verbose_name="patient"
        ordering =['nom']
    def __str__(self):
        return self.nom

class Retinopathiediabetique(models.Model):
    STADES=(('Mild', 'Mild'), ('Moderete', 'Moderete'), ('No', 'No'), ('Proliferate', 'Proliferate'), ('Severe', 'Severe'))
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_diagnostic = models.DateTimeField(default=timezone.now,
    verbose_name ="Date et heure de diagnostic")
    statut = models.BooleanField()
    stade = models.CharField(max_length=12, choices=STADES)
    def __str__(self):
        return self.statut

# Create your models here