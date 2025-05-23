# Generated by Django 5.2 on 2025-04-26 18:44

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_aboutinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='aboutinfo',
            name='profession',
            field=models.TextField(null=True, verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='about',
            field=models.TextField(null=True, verbose_name='About'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='img',
            field=models.ImageField(null=True, upload_to='img', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='aboutinfo',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, verbose_name='Phone'),
        ),
    ]
