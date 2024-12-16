from django import forms
from .models import Artisan

class ArtisanForm(forms.ModelForm):
    class Meta:
        model = Artisan
        fields = ['name', 'category', 'location', 'phone_number', 'email', 'description', 'profile_picture']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'category': forms.TextInput(attrs={'placeholder': 'e.g., Plumber, Electrician'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g., Kumasi, Accra'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'e.g., 054XXXXXXX'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe your skills and experience', 'rows': 3}),
        }
        
        
class ServiceRequestForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    location = forms.CharField(max_length=200)
    service_type = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)