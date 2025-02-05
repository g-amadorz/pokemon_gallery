# Generated by Django 5.1.5 on 2025-01-25 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20250113_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=300)),
                ('ability', models.CharField(max_length=30)),
                ('region', models.CharField(max_length=12)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.pokemon')),
            ],
        ),
    ]
