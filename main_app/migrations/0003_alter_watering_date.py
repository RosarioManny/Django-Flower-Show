# Generated by Django 5.1.3 on 2024-11-13 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watering',
            name='date',
            field=models.DateField(verbose_name='Watering Date'),
        ),
    ]
