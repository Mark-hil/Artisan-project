from django.shortcuts import get_object_or_404, render, redirect
from .forms import ArtisanForm
from .models import Artisan


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