# Generated by Django 4.1.5 on 2023-01-18 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0002_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='ending_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
