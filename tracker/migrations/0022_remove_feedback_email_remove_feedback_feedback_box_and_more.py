# Generated by Django 5.1.2 on 2024-12-31 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_remove_otp_user_delete_user_delete_otp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='email',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedback_box',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='rating',
        ),
        migrations.AddField(
            model_name='feedback',
            name='additional_comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='improvements',
            field=models.TextField(default='No value given'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='likes',
            field=models.TextField(default='No likes yet'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='satisfaction',
            field=models.IntegerField(choices=[(1, 'Very Dissatisfied'), (2, 'Dissatisfied'), (3, 'Neutral'), (4, 'Satisfied'), (5, 'Very Satisfied')], default=0),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]