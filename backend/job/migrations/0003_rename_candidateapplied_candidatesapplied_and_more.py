# Generated by Django 4.1.7 on 2023-02-24 19:16

from django.conf import settings
from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0002_candidateapplied'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CandidateApplied',
            new_name='CandidatesApplied',
        ),
        migrations.AlterField(
            model_name='job',
            name='last_date',
            field=models.DateTimeField(default=job.models.return_date_time),
        ),
    ]