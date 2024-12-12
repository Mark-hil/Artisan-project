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


class ArtisanListViewTest(TestCase):
    def setUp(self):
        self.artisan = Artisan.objects.create(
            name="Jane Smith",
            phone_number="9876543210",
            profile_picture=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )
    # def setUp(self):
    #     # Create sample artisans
    #     Artisan.objects.create(name="John Doe", category="Electrician", location="Kumasi")
    #     Artisan.objects.create(name="Jane Smith", category="Plumber", location="Accra")

    def test_artisan_list_view_status_code(self):
        # Check if the view returns a 200 status code
        response = self.client.get(reverse('artisan_list'))
        self.assertEqual(response.status_code, 200)

    def test_artisan_list_view_template(self):
        # Check if the correct template is used
        response = self.client.get(reverse('artisan_list'))
        self.assertTemplateUsed(response, 'artisans/artisan_list.html')

    def test_artisan_list_view_content(self):
        # Check if the content includes the names of the artisans
        response = self.client.get(reverse('artisan_list'))
        # self.assertContains(response, "John Doe")
        self.assertContains(response, "Jane Smith")
    
    
        



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

