# Generated by Django 2.2.28 on 2023-11-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0014_auto_20231108_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighing',
            name='date_tare',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
