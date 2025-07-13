from .forms import PetForm
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Pet, Owner, Appointment

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'petapp/pet_list.html', {'pets': pets})

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'petapp/owner_list.html', {'owners': owners})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'petapp/appointment_list.html', {'appointments': appointments})
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')  # Go back to pet list after saving
    else:
        form = PetForm()
    return render(request, 'petapp/add_pet.html', {'form': form})
def home(request):
    return render(request, 'petapp/home.html')

