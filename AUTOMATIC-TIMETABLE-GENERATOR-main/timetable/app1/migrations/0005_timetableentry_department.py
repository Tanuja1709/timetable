# Generated by Django 5.0.1 on 2024-02-15 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_timetableentry_day_remove_timetableentry_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetableentry',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.department'),
        ),
    ]
