# Generated by Django 4.1.5 on 2023-03-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0015_alter_alojamientos_balcon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alojamientos',
            name='huesped',
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='balcon',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='baños',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='descripcion',
            field=models.CharField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='habitaciones',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='img_alojamiento',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='mascotas',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='max_personas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='pileta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='tipo',
            field=models.CharField(default='NULL', max_length=30),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='titulo',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='ubicacion',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
