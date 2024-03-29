# Generated by Django 4.2.7 on 2023-12-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0004_auto_20231101_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPCamera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('ip_address', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('anpr', models.BooleanField()),
            ],
        ),
    ]
