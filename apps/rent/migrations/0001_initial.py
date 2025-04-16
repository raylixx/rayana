# Generated by Django 5.2 on 2025-04-16 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, max_length=50, null=True)),
                ('album_count', models.PositiveIntegerField(default=0)),
                ('image', models.PositiveIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Landlord',
                'verbose_name_plural': 'Landlords',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('apartment_image', models.ImageField(upload_to='apartments/image')),
                ('file', models.FileField(upload_to='apartments')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.landlord')),
            ],
            options={
                'verbose_name': 'Apartment',
                'verbose_name_plural': 'Apartments',
            },
        ),
    ]
