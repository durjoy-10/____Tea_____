# Generated by Django 5.1.4 on 2024-12-23 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0010_customerorder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=255)),
                ('tea_name', models.CharField(max_length=255)),
                ('tea_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tea_quantity', models.IntegerField()),
                ('tea_total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_tea_data', models.TextField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
