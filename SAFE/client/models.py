from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from owner.models import Facility

class Client(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null= True)
    Comment = models.CharField(max_length=500)
    StarRating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Star rating must be between 0.0 and 5.0!"
    )
    AmbienceScore = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Ambience score must be between 0.0 and 10.0!"
    )
    ServiceQualityScore = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],
        help_text="Service quality score must be between 0.0 and 10.0!"
    )
    Sentiment = models.CharField(
        max_length=20, 
        choices=[('Satisfied', 'Satisfied'), ('Unsatisfied', 'Unsatisfied')],
        default='Unsatisfied'
    )
    def __str__(self):
        return self.RestaurantName
