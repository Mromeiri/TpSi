# Generated by Django 5.0 on 2023-12-31 15:25

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0020_alter_commande_payed'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('montant', models.PositiveIntegerField()),
                ('obsrvation', models.CharField(blank=True, max_length=50, null=True)),
                ('Supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.supplier')),
            ],
        ),
    ]
