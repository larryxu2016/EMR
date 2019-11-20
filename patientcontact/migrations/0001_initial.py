# Generated by Django 2.2.6 on 2019-10-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='xxx', max_length=30)),
                ('first_name', models.CharField(default='Jane', max_length=20)),
                ('middle_name', models.CharField(default='Chandler', max_length=20)),
                ('last_name', models.CharField(default='Doe', max_length=20)),
                ('address', models.CharField(default='2662 Cannon Point Ct', max_length=30)),
                ('city', models.CharField(default='Columbus', max_length=20)),
                ('state', models.CharField(default='OH', max_length=2)),
                ('zipCode', models.CharField(default='43209', max_length=12)),
                ('homePhone', models.CharField(default='6144555678', max_length=10)),
                ('cellPhone', models.CharField(default='6144567890', max_length=10)),
                ('email', models.CharField(default='xu.285@franklin.edu', max_length=30)),
            ],
        ),
    ]