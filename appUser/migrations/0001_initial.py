# Generated by Django 4.2 on 2023-11-08 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthdate', models.DateField(verbose_name='Doğum Tarihi')),
                ('address1', models.TextField(verbose_name='Adres 1')),
                ('address2', models.TextField(verbose_name='Adres 2')),
                ('city', models.CharField(max_length=50, verbose_name='Şehir')),
                ('mobile', models.CharField(max_length=50, verbose_name='Telefon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
