# Generated by Django 4.1.7 on 2023-02-27 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_point'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='point',
        ),
    ]
