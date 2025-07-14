from .forms import PetForm, AppointmentForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Pet, Owner, Appointment

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'petapp/pet_list.html', {'pets': pets})

@login_required
def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'petapp/owner_list.html', {'owners': owners})

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'petapp/appointment_list.html', {'appointments': appointments})

@login_required
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')  # Go back to pet list after saving
    else:
        form = PetForm()
    return render(request, 'petapp/add_pet.html', {'form': form})

@login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')  # Go back to appointment list after saving
    else:
        form = AppointmentForm()
    return render(request, 'petapp/add_appointment.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'petapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'petapp/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'petapp/home.html')

