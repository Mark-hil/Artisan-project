from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArtisanForm, ServiceRequestForm
from .models import Artisan, ServiceRequest


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def artisan_list(request):
    artisans = Artisan.objects.all()
    return render(request, 'artisans/artisan_list.html', {'artisans': artisans})


def success(request):
    return render(request, 'success.html')



def register_artisan(request):
    if request.method == 'POST':
        form = ArtisanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('artisan_list')
    else:
        form = ArtisanForm()
    return render(request, 'artisans/register_artisan.html', {'form': form})

def artisan_detail(request, artisan_id):
    artisan = get_object_or_404(Artisan, id=artisan_id)
    return render(request, 'artisans/artisan_detail.html', {'artisan': artisan})


def request_service(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            # Optionally, save the service request to the database
            ServiceRequest.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                location=form.cleaned_data['location'],
                service_type=form.cleaned_data['service_type'],
                description=form.cleaned_data['description']
            )
            return redirect('success')  # Redirect to a success page
    else:
        form = ServiceRequestForm()

    return render(request, 'artisans/request_service.html', {'form': form})

def view_requested_services(request):
    # Query all requested services
    services = ServiceRequest.objects.all()
    context = {'services': services}
    return render(request, 'artisans/view_requested_services.html', context)