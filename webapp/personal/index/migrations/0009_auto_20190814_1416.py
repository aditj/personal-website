# Generated by Django 2.2.1 on 2019-08-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20190814_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
