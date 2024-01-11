# Generated by Django 4.2.9 on 2024-01-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0016_alter_vehicletare_scale_alter_weighing_scale_gross_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletare',
            name='photo_1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='vehicletare',
            name='photo_2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='vehicletare',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='weighing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
