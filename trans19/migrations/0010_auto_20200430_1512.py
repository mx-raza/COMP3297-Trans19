# Generated by Django 3.0.5 on 2020-04-30 15:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trans19', '0009_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(default=datetime.date.today, verbose_name='Date From')),
                ('date_to', models.DateField(default=datetime.date.today, verbose_name='Date To')),
                ('detail', models.CharField(blank=True, max_length=65536, null=True)),
                ('category', models.CharField(choices=[('r', 'Residence'), ('w', 'Workplace'), ('v', 'Visit'), ('s', 'School')], default='v', max_length=1, verbose_name='Category')),
            ],
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='Location_Visited',
            new_name='location_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='XCoord',
            new_name='x_coord',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='YCoord',
            new_name='y_coord',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='caseNum',
            new_name='case_number',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='DCC',
            new_name='date_case_confirmed',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='DOB',
            new_name='date_of_birth',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='patient_name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='District',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='IDN',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Location',
        ),
        migrations.AddField(
            model_name='location',
            name='district',
            field=models.CharField(choices=[('Hong Kong Island', (('central and western', 'Central and Western'), ('eastern', 'Eastern'), ('southern', 'Southern'), ('wan chai', 'Wan Chai'))), ('Kowloon', (('Sham Shui Po', 'Sham Shui Po'), ('Kowloon City', 'Kowloon City'), ('Kwun Tong', 'Kwun Tong'), ('Wong Tai Sin', 'Wong Tai Sin'), ('Yau Tsim Mong', 'Yau Tsim Mong'))), ('New Teritories', (('Islands', 'Islands'), ('Kwai Tsing', 'Kwai Tsing'), ('North', 'North'), ('Sai Kung', 'Sai Kung'), ('Sha Tin', 'Sha Tin'), ('Tai Po', 'Tai Po'), ('Tsuen Wan', 'Tsuen Wan'), ('Tuen Mun', 'Tuen Mun'), ('Yuen Long', 'Yuen Long')))], default='central and western', help_text='District of the Location', max_length=200, verbose_name='District'),
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(blank=True, help_text='Identity Document Number', max_length=10, null=True, verbose_name='Patient Identity Document Number'),
        ),
        migrations.DeleteModel(
            name='TravelHistory',
        ),
        migrations.AddField(
            model_name='visit',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans19.Location'),
        ),
        migrations.AddField(
            model_name='visit',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans19.Patient'),
        ),
    ]