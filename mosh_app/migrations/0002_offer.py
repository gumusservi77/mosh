# Generated by Django 4.1 on 2022-08-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mosh_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
