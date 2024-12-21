from django.shortcuts import render, get_object_or_404, redirect
from .models import Facility
from .forms import *
from client.models import Client
from django.contrib.auth.decorators import login_required
import os
import numpy as np

# List view for facilities
def facilities_list(request):
    facilities = Facility.objects.all()
    return render(request, 'owner/facilities_list.html', {'facilities': facilities})

# Create view for facilities
@login_required
def create_facility(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            facility = form.save(commit=False)
            facility.owner = request.user
            facility.save()
            return redirect('facilities_list')
    else:
        form = FacilityForm()
    return render(request, 'owner/create_facility.html', {'form': form})

# Update view for a specific facility
def update_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facilities_list')
    else:
        form = FacilityForm(instance=facility)
    return render(request, 'owner/update_facility.html', {'form': form, 'facility': facility})

# Delete view for a specific facility
def delete_facility(request, pk):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        facility.delete()
        return redirect('facilities_list')
    return render(request, 'owner/delete_facility.html', {'facility': facility})

def facility_detail(request, id):
    facility = get_object_or_404(Facility, id=id)
    clients = Client.objects.filter(facility=facility)
    return render(request, 'owner/facility_detail.html', {'facility': facility, 'clients': clients})

# View for predicting revenue (disabled model loading and prediction logic)
def predicter_Revenue(request, pk):
    facility = get_object_or_404(Facility, pk=pk)

    if request.method == 'POST':
        form = RevenueForm(request.POST, instance=facility, user=request.user)
        if form.is_valid():
            # Save facility without prediction logic
            facility = form.save(commit=False)
            facility.save()
            return redirect('facilities_list')
    else:
        form = RevenueForm(instance=facility, user=request.user)

    return render(
        request,
        'owner/predicter_Revenue.html',
        {
            'form': form,
            'facility': facility
        }
    )
