# Generated by Django 4.0 on 2022-01-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0019_produkty_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkty',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
