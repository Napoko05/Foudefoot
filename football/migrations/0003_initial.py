# Generated by Django 5.2.1 on 2025-05-18 19:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('football', '0002_auto_20250518_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journaliste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('identifiant', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('type_pub', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('est_abonne', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_souscription', models.DateTimeField(auto_now_add=True)),
                ('statut', models.BooleanField(default=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abonnements', to='football.utilisateur')),
            ],
        ),
    ]
