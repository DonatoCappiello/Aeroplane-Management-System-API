# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeroplanes',
            fields=[
                ('registration_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('aircraft_hours', models.FloatField()),
                ('hourly_rate', models.FloatField()),
            ],
            options={
                'db_table': 'aeroplanes',
            },
        ),
        migrations.CreateModel(
            name='AeroplanesAvailabilityErrors',
            fields=[
                ('error_id', models.AutoField(db_column='error_ID', primary_key=True, serialize=False)),
                ('registration_no', models.CharField(max_length=20)),
                ('error_description', models.TextField()),
            ],
            options={
                'db_table': 'aeroplanes_availability_errors',
            },
        ),
        migrations.CreateModel(
            name='Amends',
            fields=[
                ('amend_id', models.AutoField(db_column='amend_ID', primary_key=True, serialize=False)),
                ('amend_description', models.TextField()),
                ('amend_priority', models.CharField(max_length=6)),
                ('person_for_the_task', models.CharField(max_length=50)),
                ('outcome', models.TextField()),
                ('amend_completed_date', models.DateField()),
                ('amend_completed_by', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'amends',
            },
        ),
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('flight_id', models.AutoField(db_column='flight_ID', primary_key=True, serialize=False)),
                ('registration_no', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('student_passenger_name', models.CharField(blank=True, max_length=50, null=True)),
                ('captain_name', models.IntegerField()),
                ('duty', models.TextField()),
                ('authorised_initials', models.IntegerField()),
                ('captain_initials_before_flight', models.IntegerField()),
                ('hobb_start', models.FloatField()),
                ('hobb_stop', models.FloatField(blank=True, null=True)),
                ('captain_initials_after_flight', models.IntegerField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('field_serviceability', models.TextField(blank=True, db_column=' serviceability', null=True)),
                ('cheque_no', models.IntegerField(blank=True, null=True)),
                ('treasurer_validation', models.IntegerField(blank=True, null=True)),
                ('member_no', models.IntegerField()),
            ],
            options={
                'db_table': 'flights',
            },
        ),
        migrations.CreateModel(
            name='ForecastMaintananceCompleted',
            fields=[
                ('job_completed_id', models.AutoField(db_column='job_completed_ID', primary_key=True, serialize=False)),
                ('job_list_id', models.IntegerField()),
                ('aircraft_hours_after_job_completed', models.FloatField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('completed_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'forecast_maintanance_completed',
            },
        ),
        migrations.CreateModel(
            name='ForecastMaintananceList',
            fields=[
                ('job_list_id', models.AutoField(db_column='job_list_ID', primary_key=True, serialize=False)),
                ('registration_no', models.CharField(max_length=20)),
                ('job_name', models.CharField(max_length=255)),
                ('job_frequency_hours', models.IntegerField(blank=True, null=True)),
                ('job_frequency_months', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'forecast_maintanance_list',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('licence_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('member_initials', models.CharField(max_length=10, unique=True)),
                ('member_no', models.IntegerField(primary_key=True, serialize=False)),
                ('current_member', models.IntegerField()),
                ('licence_expiring_date', models.DateField()),
                ('licence_valid', models.IntegerField()),
                ('medical_expiring_date', models.DateField()),
                ('certificate_of_experience_expiring_date', models.DateField()),
                ('flying_order_book_signature_date', models.DateField()),
                ('role_id', models.IntegerField(db_column='role_ID')),
            ],
            options={
                'db_table': 'members',
            },
        ),
        migrations.CreateModel(
            name='MembersRoles',
            fields=[
                ('role_id', models.AutoField(db_column='role_ID', primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'members_roles',
            },
        ),
        migrations.CreateModel(
            name='MembersStatusErrors',
            fields=[
                ('error_id', models.AutoField(db_column='error_ID', primary_key=True, serialize=False)),
                ('error_description', models.TextField()),
                ('member_no', models.IntegerField()),
            ],
            options={
                'db_table': 'members_status_errors',
            },
        ),
        migrations.CreateModel(
            name='Serviceability',
            fields=[
                ('serviceability_id', models.AutoField(db_column='serviceability_ID', primary_key=True, serialize=False)),
                ('registration_no', models.CharField(max_length=20)),
                ('serviceability_description', models.TextField()),
                ('job_card', models.CharField(blank=True, max_length=50, null=True)),
                ('work_carried_out', models.TextField(blank=True, null=True)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('completed_by', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'serviceability',
            },
        ),
    ]
