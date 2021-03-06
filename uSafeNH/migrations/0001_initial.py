# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uSafeNH.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campus',
            fields=[
                ('campusID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('campusName', models.CharField(max_length=50)),
                ('campusAddressNumber', models.CharField(max_length=50)),
                ('campusAddressStreetName', models.CharField(max_length=50)),
                ('campusAddressMoreInfo', models.CharField(max_length=50)),
                ('campusCity', models.CharField(max_length=50)),
                ('campusZipcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='campusCounsel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campus')),
            ],
        ),
        migrations.CreateModel(
            name='campusCounselingCenter',
            fields=[
                ('cccID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('cccName', models.CharField(max_length=50)),
                ('cccConfidential', models.CharField(max_length=50)),
                ('cccHours', models.CharField(max_length=50)),
                ('cccAddressNumber', models.CharField(max_length=50)),
                ('cccAddressStreetName', models.CharField(max_length=50)),
                ('cccAddressMoreInfo', models.CharField(max_length=50)),
                ('cccCity', models.CharField(max_length=50)),
                ('cccZipcode', models.CharField(max_length=50)),
                ('cccPhone', models.CharField(max_length=50)),
                ('cccPhoneType', models.CharField(max_length=50)),
                ('cccPhoneExtension', models.CharField(max_length=50)),
                ('cccEmail', models.CharField(max_length=50)),
                ('cccEmailName', models.CharField(max_length=50)),
                ('cccWebsite', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='campusCrisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campus')),
            ],
        ),
        migrations.CreateModel(
            name='campusHospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campus')),
            ],
        ),
        migrations.CreateModel(
            name='campusLiaison',
            fields=[
                ('campusLiaisonID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('campusLiaisonEmail', models.CharField(max_length=50)),
                ('campusLiaisonFirstName', models.CharField(max_length=50)),
                ('campusLiaisonLastName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='campusPolice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campus')),
            ],
        ),
        migrations.CreateModel(
            name='campusSafety',
            fields=[
                ('campusSafetyID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('campusSafetyName', models.CharField(max_length=50)),
                ('campusSafetyIsOnCampus', models.CharField(max_length=50)),
                ('campusSafetyAddressNumber', models.CharField(max_length=50)),
                ('campusSafetyAddressStreetName', models.CharField(max_length=50)),
                ('campusSafetyAddressMoreInfo', models.CharField(max_length=50)),
                ('campusSafetyCity', models.CharField(max_length=50)),
                ('campusSafetyZipcode', models.CharField(max_length=50)),
                ('campusSafetyPhone', models.CharField(max_length=50)),
                ('campusSafetyPhoneType', models.CharField(max_length=50)),
                ('campusSafetyPhoneExtension', models.CharField(max_length=50)),
                ('campusSafetyWebsite', models.CharField(max_length=50)),
                ('campusSafetyReportOnlineURL', models.CharField(max_length=50)),
                ('campusSafetyReportOnlineType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('collegeID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('collegeName', models.CharField(max_length=50)),
                ('collegeAddressNumber', models.CharField(max_length=50)),
                ('collegeAddressStreetName', models.CharField(max_length=50)),
                ('collegeAddressMoreInfo', models.CharField(max_length=50)),
                ('collegeCity', models.CharField(max_length=50)),
                ('collegeZipcode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='crisisCenter',
            fields=[
                ('ccID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('ccName', models.CharField(max_length=50)),
                ('ccIsOnCampus', models.CharField(max_length=50)),
                ('ccAddressNumber', models.CharField(max_length=50)),
                ('ccAddressStreetName', models.CharField(max_length=50)),
                ('ccAddressMoreInfo', models.CharField(max_length=50)),
                ('ccCity', models.CharField(max_length=50)),
                ('ccZipcdoe', models.CharField(max_length=50)),
                ('ccPhone', models.CharField(max_length=50)),
                ('ccPhoneType', models.CharField(max_length=50)),
                ('ccPhoneExtension', models.CharField(max_length=50)),
                ('ccWebsite', models.CharField(max_length=50)),
                ('ccLogo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('hospitalID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('hospitalName', models.CharField(max_length=50)),
                ('hospitalAddressNumber', models.CharField(max_length=50)),
                ('hospitalAddressStreetName', models.CharField(max_length=50)),
                ('hospitalAddressMoreInfo', models.CharField(max_length=50)),
                ('hospitalCity', models.CharField(max_length=50)),
                ('hospitalZipcdoe', models.CharField(max_length=50)),
                ('hospitalPhone', models.CharField(max_length=50)),
                ('hospitalPhoneType', models.CharField(max_length=50)),
                ('hospitalPhoneExtension', models.CharField(max_length=50)),
                ('hospitalLogo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='police',
            fields=[
                ('policeID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('policeName', models.CharField(max_length=50)),
                ('policeCampus', models.CharField(max_length=50)),
                ('policeAddressNumber', models.CharField(max_length=50)),
                ('policeAddressStreetName', models.CharField(max_length=50)),
                ('policeAddressMoreInfo', models.CharField(max_length=50)),
                ('policeCity', models.CharField(max_length=50)),
                ('policeZipcdoe', models.CharField(max_length=50)),
                ('policePhone', models.CharField(max_length=50)),
                ('policePhoneType', models.CharField(max_length=50)),
                ('policePhoneExtension', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='specialized',
            fields=[
                ('specializedID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('specializedName', models.CharField(max_length=50)),
                ('specializedAddressNumber', models.CharField(max_length=50)),
                ('specializedAddressStreetName', models.CharField(max_length=50)),
                ('specializedAddressMoreInfo', models.CharField(max_length=50)),
                ('specializedCity', models.CharField(max_length=50)),
                ('specializedZipcdoe', models.CharField(max_length=50)),
                ('specializedPhone', models.CharField(max_length=50)),
                ('specializedPhoneType', models.CharField(max_length=50)),
                ('specializedPhoneExtension', models.CharField(max_length=50)),
                ('specializedEmailName', models.CharField(max_length=50)),
                ('specializedEmail', models.CharField(max_length=50)),
                ('campusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campus')),
            ],
        ),
        migrations.CreateModel(
            name='titleIX',
            fields=[
                ('titleIXID', models.CharField(default=uSafeNH.models.generateUUID, editable=False, max_length=36, primary_key=True, serialize=False, unique=True)),
                ('titleIXName', models.CharField(max_length=50)),
                ('titleIXAddressNumber', models.CharField(max_length=50)),
                ('titleIXAddressStreetName', models.CharField(max_length=50)),
                ('titleIXAddressMoreInfo', models.CharField(max_length=50)),
                ('titleIXPhone', models.CharField(max_length=50)),
                ('titleIXPhoneType', models.CharField(max_length=50)),
                ('titleIXPhoneExtension', models.CharField(max_length=50)),
                ('titleIXEmailName', models.CharField(max_length=50)),
                ('titleIXEmail', models.CharField(max_length=50)),
                ('collegeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.college')),
            ],
        ),
        migrations.AddField(
            model_name='campuspolice',
            name='policeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.police'),
        ),
        migrations.AddField(
            model_name='campusliaison',
            name='collegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.college'),
        ),
        migrations.AddField(
            model_name='campushospital',
            name='hospitalID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.hospital'),
        ),
        migrations.AddField(
            model_name='campuscrisis',
            name='ccID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.crisisCenter'),
        ),
        migrations.AddField(
            model_name='campuscounsel',
            name='cccID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.campusCounselingCenter'),
        ),
        migrations.AddField(
            model_name='campus',
            name='collegeID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uSafeNH.college'),
        ),
    ]
