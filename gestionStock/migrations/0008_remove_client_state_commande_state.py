# Generated by Django 4.2.3 on 2023-12-24 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0007_client_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='state',
        ),
        migrations.AddField(
            model_name='commande',
            name='state',
            field=models.CharField(choices=[('1', 'En attente'), ('2', 'Confirmée'), ('3', 'En cours de préparation'), ('4', 'Expédiée'), ('5', 'En cours de livraison'), ('6', 'Livrée'), ('7', 'Annulée'), ('8', 'Retournée'), ('9', 'Partiellement arrivée')], default='1', max_length=1),
        ),
    ]