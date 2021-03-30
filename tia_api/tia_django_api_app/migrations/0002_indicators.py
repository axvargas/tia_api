# Generated by Django 3.1.7 on 2021-03-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tia_django_api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_tickets', models.FloatField()),
                ('avg_margin', models.FloatField()),
                ('avg_products_qty', models.FloatField()),
            ],
            options={
                'db_table': 'indicators',
            },
        ),
    ]
