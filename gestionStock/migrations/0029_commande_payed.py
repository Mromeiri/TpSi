# Generated by Django 4.2.3 on 2024-01-19 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0028_remove_commande_payed'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='payed',
            field=models.BooleanField(default=False),
        ),
    ]
