# Generated by Django 4.1.5 on 2023-03-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0007_alojamientos_huesped_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamientos',
            name='img_alojamiento',
            field=models.ImageField(null=True, upload_to='img/'),
        ),
    ]
