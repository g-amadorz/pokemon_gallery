# Generated by Django 5.1.5 on 2025-01-31 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_user_rename_pokemon_pokemondata_pokemon_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemondata',
            name='ability',
            field=models.CharField(max_length=50),
        ),
    ]
