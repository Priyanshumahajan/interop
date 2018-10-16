# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-16 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auvsi_suas', '0033_remove_mission_clock_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movingobstacle',
            name='waypoints',
        ),
        migrations.RemoveField(
            model_name='missionconfig',
            name='moving_obstacles',
        ),
        migrations.AlterField(
            model_name='takeofforlandingevent',
            name='timestamp',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='uastelemetry',
            name='timestamp',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.DeleteModel(
            name='MovingObstacle',
        ),
    ]
