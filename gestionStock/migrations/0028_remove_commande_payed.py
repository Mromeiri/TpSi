# Generated by Django 4.2.3 on 2024-01-19 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0027_alter_sale_sale_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='payed',
        ),
    ]
