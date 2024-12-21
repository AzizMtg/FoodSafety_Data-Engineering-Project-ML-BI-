from django import forms
from .models import Inspection
from owner.models import Facility

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'activity_date', 
            'score', 
            'grade', 
            'service_description', 
            'risk', 
            'service_code', 
            'violation_code', 
            'facility'  # Include facility field
        ]
        widgets = {
            'activity_date': forms.DateInput(attrs={'type': 'date'}),
        }

    # Add a ModelChoiceField for the facility dropdown list
    facility = forms.ModelChoiceField(
        queryset=Facility.objects.all(),  # Query all available facilities
        empty_label="Select a Facility",   # Optional: display a placeholder option
        widget=forms.Select(attrs={'class': 'form-control'})  # Optional: add CSS class
    )
    
class PredictionForm(forms.Form):
    number_of_violations = forms.IntegerField()
    facility_zip = forms.IntegerField()
    state = forms.CharField(max_length=100)
    poverty_percent = forms.FloatField()
    air_quality = forms.FloatField()
    water_pollution = forms.FloatField()
