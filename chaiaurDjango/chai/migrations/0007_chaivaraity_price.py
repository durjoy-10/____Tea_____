# Generated by Django 5.1.4 on 2024-12-20 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0006_alter_chairiview_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivaraity',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]