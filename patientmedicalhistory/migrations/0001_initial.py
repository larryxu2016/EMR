# Generated by Django 2.2.6 on 2019-10-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='Jane', max_length=30)),
                ('info_type', models.CharField(default='symptoms', max_length=30)),
                ('med_history', models.CharField(default='Fever', max_length=30)),
            ],
        ),
    ]
