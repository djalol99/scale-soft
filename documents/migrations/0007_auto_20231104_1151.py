# Generated by Django 2.2.28 on 2023-11-04 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20231104_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weighing',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
