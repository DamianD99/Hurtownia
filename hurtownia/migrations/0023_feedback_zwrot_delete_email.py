# Generated by Django 4.0 on 2022-03-04 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hurtownia', '0022_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the sender', max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Zwrot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_zwrotu', models.CharField(max_length=30, null=True)),
                ('przyczyna', models.CharField(max_length=30, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('produkt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hurtownia.produkty')),
            ],
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]