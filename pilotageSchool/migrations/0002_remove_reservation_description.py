# Generated by Django 4.1.7 on 2023-03-08 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotageSchool', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='description',
        ),
    ]
