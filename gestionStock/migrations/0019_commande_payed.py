# Generated by Django 5.0 on 2023-12-31 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0018_paymentcommande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='payed',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
