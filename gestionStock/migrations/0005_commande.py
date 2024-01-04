# Generated by Django 4.2.3 on 2023-12-24 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0004_product_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.client')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionStock.supplier')),
            ],
        ),
    ]
