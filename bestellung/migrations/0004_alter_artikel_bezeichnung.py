# Generated by Django 5.1.3 on 2024-12-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestellung', '0003_lagerplatz_lieferposition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='bezeichnung',
            field=models.CharField(max_length=250, verbose_name='Bezeichnung'),
        ),
    ]