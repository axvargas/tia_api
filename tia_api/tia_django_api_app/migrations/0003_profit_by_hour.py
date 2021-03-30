# Generated by Django 3.1.7 on 2021-03-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tia_django_api_app', '0002_indicators'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profit_By_Hour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour_of_day', models.FloatField()),
                ('income', models.FloatField()),
                ('profit', models.FloatField()),
            ],
            options={
                'db_table': 'profit_by_hour',
            },
        ),
    ]