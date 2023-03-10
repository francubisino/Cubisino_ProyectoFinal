# Generated by Django 4.1.5 on 2023-03-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_alter_alojamientos_baños_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamientos',
            name='balcon',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='descripcion',
            field=models.CharField(default='NULL', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='huesped',
            field=models.CharField(default='NULL', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='mascotas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='pileta',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='tipo',
            field=models.CharField(default='NULL', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='titulo',
            field=models.CharField(default='NULL', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='ubicacion',
            field=models.CharField(default='NULL', max_length=30, null=True),
        ),
    ]
