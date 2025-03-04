# Generated by Django 4.2 on 2024-12-16 19:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.CharField(max_length=500)),
                ('StarRating', models.FloatField(help_text='Star rating must be between 0.0 and 5.0!', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('AmbienceScore', models.FloatField(help_text='Ambience score must be between 0.0 and 10.0!', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('ServiceQualityScore', models.FloatField(help_text='Service quality score must be between 0.0 and 10.0!', validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('Sentiment', models.CharField(choices=[('Satisfied', 'Satisfied'), ('Unsatisfied', 'Unsatisfied')], default='Unsatisfied', max_length=20)),
                ('facility', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.facility')),
            ],
        ),
    ]
