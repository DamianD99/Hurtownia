# Generated by Django 3.1.7 on 2021-12-08 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0011_auto_20211208_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produkty',
            old_name='categoty',
            new_name='zepsuty',
        ),
    ]