# Generated by Django 2.2.12 on 2020-06-18 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0006_auto_20200514_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='images/perfiles', verbose_name='Foto de perfil'),
        ),
    ]
