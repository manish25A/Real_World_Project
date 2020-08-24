# Generated by Django 2.2.12 on 2020-08-24 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200824_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=150)),
                ('phone_no', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('datecreated', models.DateTimeField(default=datetime.datetime(2020, 8, 24, 12, 21, 53, 182053))),
            ],
            options={
                'db_table': 'candidate',
            },
        ),
        migrations.DeleteModel(
            name='CandidateForm',
        ),
    ]
