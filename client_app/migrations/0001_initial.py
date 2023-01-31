# Generated by Django 4.1.5 on 2023-01-11 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('ALL', 'All'), ('RUNNING', 'Running'), ('UPCOMING', 'Upcoming'), ('CLOSED', 'Closed')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_num', models.IntegerField()),
                ('client_name', models.CharField(max_length=100)),
                ('project_name', models.TextField(max_length=1000)),
                ('project_details', models.TextField(max_length=1000)),
                ('project_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_app.role')),
                ('project_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_app.status')),
            ],
        ),
    ]
