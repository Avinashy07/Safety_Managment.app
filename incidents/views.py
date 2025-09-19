# incidents/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import SafetyIncident
from django.contrib.auth.forms import AuthenticationForm
from django import forms

# Safety Incident Form
class IncidentForm(forms.ModelForm):
    class Meta:
        model = SafetyIncident
        fields = ['title', 'description', 'location']

# Login View
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('incident_list')
    else:
        form = AuthenticationForm()
    return render(request, 'incidents/login.html', {'form': form})

# Logout View
def user_logout(request):
    logout(request)
    return redirect('login')

# CRUD Views
@login_required
def incident_list(request):
    incidents = SafetyIncident.objects.all().order_by('-reported_date')
    return render(request, 'incidents/incident_list.html', {'incidents': incidents})

@login_required
def incident_create(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.reported_by = request.user
            incident.save()
            return redirect('incident_list')
    else:
        form = IncidentForm()
    return render(request, 'incidents/incident_form.html', {'form': form})

@login_required
def incident_update(request, pk):
    incident = get_object_or_404(SafetyIncident, pk=pk)
    if request.method == "POST":
        form = IncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('incident_list')
    else:
        form = IncidentForm(instance=incident)
    return render(request, 'incidents/incident_form.html', {'form': form})

@login_required
def incident_delete(request, pk):
    incident = get_object_or_404(SafetyIncident, pk=pk)
    if request.method == "POST":
        incident.delete()
        return redirect('incident_list')
    return render(request, 'incidents/incident_confirm_delete.html', {'incident': incident})
