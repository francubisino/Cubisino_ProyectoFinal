# Generated by Django 4.1.5 on 2023-03-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0011_alter_alojamientos_balcon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruebas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=30)),
                ('img_alojamiento', models.ImageField(null=True, upload_to='img/')),
            ],
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='balcon',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='mascotas',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='pileta',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='alojamientos',
            name='ubicacion',
            field=models.CharField(max_length=30),
        ),
    ]
