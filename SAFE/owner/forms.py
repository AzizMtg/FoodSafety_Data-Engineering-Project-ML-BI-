from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = [
            'predicted_revenue', 
            'seating_capacity', 
            'average_meal_price', 
            'marketing_budget', 
            'weekend_reservations', 
            'weekday_reservations', 
            'owner',  
        ]
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
    def clean_facility_name(self):
        """Validation pour vérifier si le nom de l'établissement existe déjà pour un autre propriétaire."""
        facility_name = self.cleaned_data.get('facility_name')
        if Facility.objects.filter(facility_name=facility_name).exclude(owner=self.user).exists():
            raise forms.ValidationError(
                "This facility name is already associated with another owner."
            )
        return facility_name

    def clean(self):
        """Validation générale des données."""
        cleaned_data = super().clean()
        facility_zip = cleaned_data.get('facility_zip')
        if facility_zip and not facility_zip.isdigit():
            self.add_error('facility_zip', "The ZIP code must contain only digits.")
        return cleaned_data

    def save(self, commit=True):
        """Associer automatiquement l'utilisateur connecté comme propriétaire."""
        instance = super().save(commit=False)
        if self.user and self.user.role == 'owner':  # Vérification que l'utilisateur est bien un propriétaire
            instance.owner = self.user  # Assigner l'utilisateur connecté comme propriétaire
        if commit:
            instance.save()
        return instance



class RevenueForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = [ 
            'seating_capacity', 
            'average_meal_price', 
            'marketing_budget', 
            'weekend_reservations', 
            'weekday_reservations', 
            'facility_name'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Rendre `facility_name` non modifiable
        self.fields['facility_name'].widget.attrs['readonly'] = True

    def clean_facility_name(self):
        facility_name = self.cleaned_data.get('facility_name')
        if not Facility.objects.filter(facility_name=facility_name, owner=self.user).exists():
            raise forms.ValidationError("This facility does not belong to you or does not exist.")
        return facility_name

    def clean(self):
        cleaned_data = super().clean()
        positive_fields = [
            'seating_capacity', 
            'average_meal_price', 
            'marketing_budget', 
            'weekend_reservations', 
            'weekday_reservations'
        ]
        for field in positive_fields:
            value = cleaned_data.get(field)
            if value is not None and value <= 0:
                self.add_error(field, f"{field.replace('_', ' ').capitalize()} must be strictly positive.")
        return cleaned_data
