# Generated by Django 3.1.12 on 2025-01-13 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20250112_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='num',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]