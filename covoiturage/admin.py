from django.contrib import admin
from .models import Trajet, Reservation, Commentaire, Notification, Paiement,Remboursement

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'trajet', 'date')
    list_filter = ('date',)
    search_fields = ('user__username', 'trajet__point_depart', 'trajet__destination')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('commentaire', 'note', 'destinataire', 'trajet')
    list_filter = ('note',)
    search_fields = ('destinataire__username', 'trajet__point_depart', 'trajet__destination')

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reservation', 'contenu', 'date')
    list_filter = ('date',)
    search_fields = ('user__username', 'reservation__user__username')

class PaiementAdmin(admin.ModelAdmin):
    list_display = ('trajet', 'utilisateur', 'montant', 'date')
    list_filter = ('date',)
    search_fields = ('utilisateur__username', 'trajet__point_depart', 'trajet__destination')


class RemboursementAdmin(admin.ModelAdmin):
    list_display = ('reservation', 'motif', 'montant', 'date')
    list_filter = ('date',)
    search_fields = ('reservation__user__username',)

admin.site.register(Remboursement, RemboursementAdmin)
admin.site.register(Trajet)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(Paiement, PaiementAdmin)



# Register your models here.
