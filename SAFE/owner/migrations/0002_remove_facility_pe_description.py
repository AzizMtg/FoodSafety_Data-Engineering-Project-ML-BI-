# Generated by Django 4.2 on 2024-12-18 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='pe_description',
        ),
    ]
