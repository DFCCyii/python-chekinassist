# Generated by Django 2.2.12 on 2020-05-19 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0004_auto_20200518_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='perfiles/img', verbose_name='Foto de perfil'),
        ),
    ]
