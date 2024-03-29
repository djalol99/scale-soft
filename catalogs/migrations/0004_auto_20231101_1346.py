# Generated by Django 2.2.28 on 2023-11-01 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0003_auto_20231028_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='brand',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='brands', to='catalogs.VehicleBrand'),
            preserve_default=False,
        ),
    ]
