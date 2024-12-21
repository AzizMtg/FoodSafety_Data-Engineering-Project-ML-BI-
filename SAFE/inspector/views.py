from django.shortcuts import render, redirect
from .forms import *
from .models import Inspection
from owner.models import Facility
from client.models import Client

import json
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

def create_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inspections_list')  # Redirect to inspection list
    else:
        form = InspectionForm()
    return render(request, 'inspector/create_inspection.html', {'form': form})



def update_inspection(request, pk):
    inspection = Inspection.objects.get(id=pk)
    if request.method == 'POST':
        form = InspectionForm(request.POST, instance=inspection)
        if form.is_valid():
            form.save()
            return redirect('inspections_list')
    else:
        form = InspectionForm(instance=inspection)
    return render(request, 'inspector/update_inspection.html', {'form': form, 'inspection': inspection})


def delete_inspection(request, pk):
    inspection = Inspection.objects.get(id=pk)
    if request.method == 'POST':
        inspection.delete()
        return redirect('inspections_list')
    return render(request, 'inspector/delete_inspection.html', {'inspection': inspection})
# Load the model and training data from JSON file
import os

file_path = os.path.join(os.path.dirname(__file__), 'knn_model.json')
with open(file_path, 'r') as f:    model_data = json.load(f)

# Rebuild the KNN model with the saved parameters
knn = KNeighborsClassifier(n_neighbors=model_data['n_neighbors'], metric=model_data['metric'])

# Recreate the training data from the JSON
X_train = np.array(model_data['X_train'])
y_train = np.array(model_data['y_train'])

# Fit the model manually (without re-training from scratch, just use the loaded data)
knn.fit(X_train, y_train)

# Initialize label encoder for state feature
label_encoder = LabelEncoder()

def inspections_list(request):
    facilities = Facility.objects.all()
    inspections = Inspection.objects.all()
    prediction_result = None  # Initialize variable for prediction result

    # Handle the form submission for prediction
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Get user input from form
            number_of_violations = form.cleaned_data['number_of_violations']
            facility_zip = form.cleaned_data['facility_zip']
            state = form.cleaned_data['state']
            poverty_percent = form.cleaned_data['poverty_percent']
            air_quality = form.cleaned_data['air_quality']
            water_pollution = form.cleaned_data['water_pollution']
            
            # Encode the state input
            state_encoded = label_encoder.fit_transform([state])[0]  # Encoding the input state
            
            # Prepare the input for prediction
            user_input = np.array([[number_of_violations, facility_zip, state_encoded, poverty_percent, air_quality, water_pollution]])
            
            # Make prediction using the trained KNN model
            prediction_result = knn.predict(user_input)[0]  # Get the predicted result

    else:
        form = PredictionForm()

    return render(request, 'inspector/inspections_list.html', {'inspections': inspections, 'form': form, 'prediction_result': prediction_result, 'facilities': facilities})

from django.shortcuts import render, get_object_or_404



def facility_insp(request, pk):
    # Get the facility by its primary key (pk)
    facility = get_object_or_404(Facility, pk=pk)
    
    # Get all inspections for the selected facility
    inspections = Inspection.objects.filter(facility=facility)
    
    # Render the 'facility_detail.html' template with the facility and its inspections
    return render(request, 'inspector/facility_insp.html', {'facility': facility, 'inspections': inspections})