from django.db import models
from django.contrib.auth.models import User


class Trajet(models.Model):
    point_depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_depart = models.DateTimeField()
    places_disponibles = models.IntegerField()
    modele = models.CharField(max_length=255,null=True)
    plaque = models.CharField(max_length=10,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

      
    def __str__(self):
        return f"{self.point_depart} - {self.destination}"

class Reservation(models.Model):
    class STATUT(models.TextChoices):
        EN_ATTENTE = "En attente" 
        CONFIRME = "Confirme"
        REJECT = "annule"

    user= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE,null=True)
    statut = models.CharField(max_length=18, choices=STATUT.choices, default=STATUT.EN_ATTENTE)
    avance = models.PositiveIntegerField(null=True)
    date= models.DateTimeField(null=True) 
    
    def __str__(self):
        return f"{self.user} - {self.trajet}"

class Commentaire(models.Model):
    commentaire = models.TextField()
    note = models.IntegerField()
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentaires_clients',null=True)
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.commentaire
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE,null=True)
    contenu = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.contenu

class Paiement(models.Model):
    trajet = models.ForeignKey(Trajet, on_delete=models.CASCADE,null=True)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    montant = models.PositiveIntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.utilisateur} - {self.montant}"

class Remboursement(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    motif = models.TextField()
    montant = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Remboursement pour la réservation {self.reservation.user}"

    class Meta:
        verbose_name = "Remboursement"
        verbose_name_plural = "Remboursements"
