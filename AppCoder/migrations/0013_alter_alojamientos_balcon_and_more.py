# Generated by Django 4.1.5 on 2023-03-05 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0012_pruebas_alter_alojamientos_balcon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamientos',
            name='balcon',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='mascotas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='pileta',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
