# Generated by Django 4.0 on 2022-03-04 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0024_zwrot_klijent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zwrot',
            name='klijent',
        ),
        migrations.AlterField(
            model_name='zwrot',
            name='data',
            field=models.DateField(),
        ),
    ]