# Generated by Django 4.1.5 on 2023-03-08 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamientos',
            name='propietario',
            field=models.CharField(default='Bote', max_length=30),
        ),
    ]
