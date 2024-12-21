from django.db import models
from accounts.models import *

# Define constants outside the class
PROGRAM_STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
]

RISK_LEVELS = [
    ('MODERATE RISK', 'Moderate Risk'),
    ('HIGH RISK', 'High Risk'),
    ('LOW RISK', 'Low Risk'),
]

SERIAL_NUMBER_CHOICES = [
    'RESTAURANT (0-30) SEATS',
    'RESTAURANT (31-60) SEATS',
    'RESTAURANT (61-150) SEATS',
    'RESTAURANT (150+) SEATS',
]

class Facility(models.Model):
    # Basic Information
    serial_number = models.CharField(max_length=100)
    facility_name = models.CharField(max_length=255)
    facility_address = models.CharField(max_length=255)
    facility_city = models.CharField(max_length=100)
    facility_state = models.CharField(max_length=100)
    facility_zip = models.CharField(max_length=20)

    # Establishment Information
    program_status = models.CharField(
        max_length=10,
        choices=PROGRAM_STATUS_CHOICES,
    )

    # Optional Revenue Predictions
    predicted_revenue = models.FloatField(
        verbose_name="Revenue Prédit",
        null=True,
        blank=True,
    )
    seating_capacity = models.IntegerField(
        verbose_name="Capacité d'Accueil",
        null=True,
        blank=True,
    )
    average_meal_price = models.FloatField(
        verbose_name="Prix Moyen d'un Repas",
        null=True,
        blank=True,
    )
    marketing_budget = models.IntegerField(
        verbose_name="Budget Marketing",
        null=True,
        blank=True,
    )
    weekend_reservations = models.IntegerField(
        verbose_name="Réservations du Weekend",
        null=True,
        blank=True,
    )
    weekday_reservations = models.IntegerField(
        verbose_name="Réservations en Semaine",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='facilities',
        limit_choices_to={'role': 'owner'},
        verbose_name="Propriétaire",
    )

    def __str__(self):
        return self.facility_name
