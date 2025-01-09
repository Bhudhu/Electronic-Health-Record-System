from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import PatientForm
from .models import Patient
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import logging


def home(request):
    return render(request, 'patient_records/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == 'admin':
            return redirect('dashboard')
    return render(request, 'patient_records/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    # Get total number of patients
    total_patients = Patient.objects.count()

    # Get the number of recent patients (e.g., last 7 days based on another field like 'age')
    # Example: recent patients with age under 30 (modify as needed)
    recent_patients = Patient.objects.filter(age__lt=30).count()

    # Get the number of patients at risk (you could use a custom field for this)
    patients_at_risk = Patient.objects.filter(allergies__contains='Asthma').count()

    # Latest activity (this can be a custom model or tracked events)
    latest_activity = [
        {'patient_name': 'John Doe', 'action': 'Added', 'date': '2024-11-15'},
        {'patient_name': 'Jane Smith', 'action': 'Updated', 'date': '2024-11-14'},
    ]

    return render(request, 'patient_records/dashboard.html', {
        'total_patients': total_patients,
        'recent_patients': recent_patients,
        'patients_at_risk': patients_at_risk,
        'latest_activity': latest_activity,
    })


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Patient saved successfully!")  # Debug message
            return redirect('dashboard')  # Adjust as needed
        else:
            print("Form errors:", form.errors)  # Debug validation errors
    else:
        form = PatientForm()

    return render(request, 'patient_records/add_patient.html', {'form': form})


@login_required
def search_patient(request):
    if request.method == 'POST':
        query = request.POST.get('query', '').strip()
        print(f"Search Query: {query}")  # Debug to confirm query input

        if query:
            # Querying based on multiple fields using OR logic
            patients = Patient.objects.filter(
                Q(id_number__icontains=query) |
                Q(first_name__icontains=query) |
                Q(surname__icontains=query) |
                Q(first_name__icontains=query.split()[0], surname__icontains=query.split()[-1])
            )
            print(f"Patients Found: {patients}")  # Debug: Check returned queryset
            
            if patients.exists():
                # If multiple patients, show a list, or redirect to one if unique
                return redirect('patient_card', pk=patients.first().id)

        return render(request, 'patient_records/search_patient.html', {'error': 'No patients found'})
    
    return render(request, 'patient_records/search_patient.html')
    
@login_required
def patient_card(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient_records/patient_card.html', {'patient': patient})

@login_required
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = PatientForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after saving
    else:
        form = PatientForm(instance=patient)
    
    return render(request, 'patient_records/edit_patient.html', {'form': form, 'patient': patient})

@login_required
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('dashboard')
    return render(request, 'patient_records/delete_patient.html', {'patient': patient})

# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
def fetch_patient_by_name(request):
    logger.info(f"Received request: {request.method} with data {request.POST if request.method == 'POST' else request.GET}")

    # Extract name from request
    name_from_hikvision =  request.POST.get('name') or request.GET.get('name')

    if not name_from_hikvision:
        return render(request, 'patient_records/patient_card.html', {'error': 'No name provided in the request'})

    # Split name into first and last
    name_parts = name_from_hikvision.split()
    
    if len(name_parts) < 2:
        return render(request, 'patient_records/patient_card.html', {'error': 'Invalid name format. Provide both first and last names.'})

    first_name, *middle, surname = name_parts[0], name_parts[1]
    
    # Search for the patient
    patient = Patient.objects.filter(first_name__iexact=first_name, surname__iexact=surname).first()

    if patient:
        print(f"Patient ID: {patient.id}")
        return render(request, 'patient_records/search_patient.html', {'error': 'No patients found', 'patient': patient})

    else:
        logging.warning("No patient found")
        return HttpResponse("No patient found", status=404)