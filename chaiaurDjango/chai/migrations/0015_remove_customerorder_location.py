# Generated by Django 5.1.4 on 2024-12-28 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0014_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorder',
            name='location',
        ),
    ]
