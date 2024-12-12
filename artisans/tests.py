from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ArtisanForm
from .models import Artisan

class ArtisanModelTest(TestCase):
    def setUp(self):
        # Create a sample artisan
        self.artisan = Artisan.objects.create(
            name="John Doe",
            category="Electrician",
            location="Kumasi",
            phone_number="1234567890",
            email="john@example.com",
            description="Expert in residential electrical work.",
        )

    def test_artisan_creation(self):
        # Test if the artisan object is created correctly
        self.assertEqual(self.artisan.name, "John Doe")
        self.assertEqual(self.artisan.category, "Electrician")
        self.assertEqual(str(self.artisan), "John Doe")  # Ensure the __str__ method works

    def test_artisan_defaults(self):
        # Test that default values, if any, are correctly set
        pass  # Add this if your model has default fields


class ArtisanViewTests(TestCase):

    def setUp(self):
        # Create sample artisans
        self.artisan1 = Artisan.objects.create(
            name="John Doe",
            category="Plumber",
            location="Kumasi",
            phone_number="1234567890",
            email="johndoe@example.com",
            description="Experienced plumber with 5+ years of work experience.",
        )
        self.artisan2 = Artisan.objects.create(
            name="Jane Smith",
            category="Electrician",
            location="Accra",
            phone_number="0987654321",
            email="janesmith@example.com",
            description="Certified electrician specializing in home wiring.",
        )

    def test_artisan_list_view(self):
        # Test the artisan list page
        url = reverse('artisan_list')  # Replace 'artisan_list' with your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure the page loads
        self.assertContains(response, self.artisan1.name)  # Check if artisan1 is listed
        self.assertContains(response, self.artisan2.name)  # Check if artisan2 is listed
        self.assertTemplateUsed(response, 'artisans/artisan_list.html')  # Ensure correct template is used

    def test_artisan_detail_view(self):
        # Test the artisan detail page
        url = reverse('artisan_detail', args=[self.artisan1.id])  # Replace 'artisan_detail' with your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Ensure the page loads
        self.assertContains(response, self.artisan1.name)  # Check if the artisan's name is displayed
        self.assertContains(response, self.artisan1.category)  # Check if the category is displayed
        self.assertContains(response, self.artisan1.description)  # Check if the description is displayed
        self.assertTemplateUsed(response, 'artisans/artisan_detail.html')  # Ensure correct template is used

    def test_view_profile_link(self):
        # Test if "View Profile" link works
        list_url = reverse('artisan_list')
        response = self.client.get(list_url)
        detail_url = reverse('artisan_detail', args=[self.artisan1.id])
        self.assertContains(response, f'href="{detail_url}"')  # Check if the detail link exists



class ArtisanFormTest(TestCase):
    def test_valid_form(self):
        # Create data for a valid form
        data = {
            'name': 'John Doe',
            'category': 'Electrician',
            'location': 'Kumasi',
            'phone_number': '1234567890',
            'email': 'john@example.com',
            'description': 'Expert in residential electrical work.',
        }
        form = ArtisanForm(data=data)
        self.assertTrue(form.is_valid())  # Form should be valid

    def test_invalid_form(self):
        # Create data for an invalid form (e.g., missing required fields)
        data = {
            'name': '',  # Missing name
            'category': 'Electrician',
            'location': 'Kumasi',
        }
        form = ArtisanForm(data=data)
        self.assertFalse(form.is_valid())  # Form should be invalid



class ArtisanImageTest(TestCase):
    def test_image_upload(self):
        # Simulate an image file upload
        profile_picture = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        artisan = Artisan.objects.create(
            name="John Doe",
            category="Electrician",
            location="Kumasi",
            phone_number="1234567890",
            email="john@example.com",
            description="Expert in residential electrical work.",
            profile_picture=profile_picture,
        )
        self.assertTrue(artisan.profile_picture)  # Check if the image is saved

