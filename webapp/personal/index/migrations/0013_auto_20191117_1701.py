# Generated by Django 2.2.1 on 2019-11-17 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20191116_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='read_on',
            field=models.DateField(blank=True, null=True, verbose_name='Date Read On'),
        ),
    ]
