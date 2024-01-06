# Generated by Django 4.2.7 on 2023-12-27 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0001_initial'),
        ('documents', '0015_auto_20231108_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletare',
            name='scale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='devices.scale'),
        ),
        migrations.AlterField(
            model_name='weighing',
            name='scale_gross',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='grosses', to='devices.scale'),
        ),
        migrations.AlterField(
            model_name='weighing',
            name='scale_tare',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tares', to='devices.scale'),
        ),
    ]
