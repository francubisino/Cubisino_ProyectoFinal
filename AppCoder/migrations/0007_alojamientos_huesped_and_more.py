# Generated by Django 4.1.5 on 2023-03-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_suscripciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamientos',
            name='huesped',
            field=models.CharField(default='NULL', max_length=20),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='img_alojamiento',
            field=models.ImageField(default='no hay imagen', upload_to='img/'),
            preserve_default=False,
        ),
    ]