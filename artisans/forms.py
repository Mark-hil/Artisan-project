from django import forms
from .models import Artisan

class ArtisanForm(forms.ModelForm):
    class Meta:
        model = Artisan
        fields = ['name', 'category', 'location', 'phone_number', 'email', 'description', 'profile_picture']
