# Generated by Django 4.1.13 on 2024-10-05 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_add_job_application_status_add_job_interview_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_job',
            name='job_description',
        ),
    ]
