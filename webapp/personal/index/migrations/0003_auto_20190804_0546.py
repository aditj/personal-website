# Generated by Django 2.2.1 on 2019-08-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190803_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='images/projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='report',
            field=models.FileField(null=True, upload_to='project_reports'),
        ),
    ]
