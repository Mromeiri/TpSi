# Generated by Django 4.2.3 on 2024-01-21 17:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestionStock', '0030_delete_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_of_registration',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
