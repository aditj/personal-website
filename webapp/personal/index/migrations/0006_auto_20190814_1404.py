# Generated by Django 2.2.1 on 2019-08-14 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20190814_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='report',
            field=models.URLField(null=True),
        ),
    ]
