from django.test import Client, TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import ArtisanForm, ServiceRequestForm
from .models import Artisan, ServiceRequest

class ArtisanModelTest(TestCase):
    def setUp(self):
        # Create a sample artisan
        self.artisan = Artisan.objects.create(
            name="John Doe",
            category="Electrician",
            location="Kumasi",
            phone_number="1234567890",
            email="john@gmail.com",
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
        # Create a sample artisan with an image
        self.artisan = Artisan.objects.create(
            name="Jane Smith",
            phone_number="9876543210",
            profile_picture=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )

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
        self.assertContains(response, "Jane Smith")


class ArtisansAppTestCase(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = Client()

        # Create test data for RequestedService
        self.requested_service_data = {
            "name": "John Doe",
            "email": "john@gmail.com",
            "phone_number": "1234567890",
            "location": "Kumasi",
            "service_type": "Plumbing",
            "description": "Need urgent plumbing repairs."
        }

        # Create test data for RegisterArtisan with required fields
        self.artisan_data = {
            "name": "Jane Smith",
            "email": "jane@gmail.com",
            "phone_number": "0987654321",
            "category": "Electrician",  # Add this field
            "location": "Accra",  # Add this field
            "description": "Expert in electrical work",  # Add this field
        }

    # Test for Request Service Form
    def test_request_service_form_valid(self):
        form = ServiceRequestForm(data=self.requested_service_data)
        self.assertTrue(form.is_valid(), "Request Service form should be valid with correct data")

    # Test for Register Artisan Form
    def test_register_artisan_form_valid(self):
        form = ArtisanForm(data=self.artisan_data)
        print(form.errors)  # To inspect validation errors
        self.assertTrue(form.is_valid(), "Register Artisan form should be valid with correct data")

    # Test POST Register Artisan
    def test_post_register_artisan(self):
        response = self.client.post(reverse('register_artisan'), self.artisan_data)
        print(response.status_code)  # To inspect the status code
        self.assertEqual(response.status_code, 302, "Register Artisan form submission should redirect")
        self.assertTrue(Artisan.objects.filter(email="jane@gmail.com").exists())

class ArtisanImageTest(TestCase):
    def test_image_upload(self):
        # Simulate an image file upload
        profile_picture = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        artisan = Artisan.objects.create(
            name="John Doe",
            category="Electrician",
            location="Kumasi",
            phone_number="1234567890",
            email="john@gmail.com",
            description="Expert in residential electrical work.",
            profile_picture=profile_picture,
        )
        self.assertTrue(artisan.profile_picture)  # Check if the image is saved


class ArtisansAppTestCase(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = self.client

        # Create test data for ServiceRequest
        self.requested_service_data = {
            "name": "John Doe",
            "email": "john@gmail.com",
            "phone_number": "1234567890",
            "location": "Kumasi",
            "service_type": "Plumbing",
            "description": "Need urgent plumbing repairs."
        }

        # Create test data for RegisterArtisan
        self.artisan_data = {
            "name": "Jane Smith",
            "email": "jane@gmail.com",
            "phone_number": "0987654321",
        }

    def test_request_service_form_valid(self):
        form = ServiceRequestForm(data=self.requested_service_data)
        self.assertTrue(form.is_valid(), "Request Service form should be valid with correct data")

    # def test_register_artisan_form_valid(self):
    #     form = ArtisanForm(data=self.artisan_data)
    #     self.assertTrue(form.is_valid(), "Register Artisan form should be valid with correct data")

    def test_homepage_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, "Homepage should load successfully")
        self.assertTemplateUsed(response, 'home.html')

    def test_about_page_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200, "About page should load successfully")
        self.assertTemplateUsed(response, 'about.html')

    def test_services_page_view(self):
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200, "Services page should load successfully")
        self.assertTemplateUsed(response, 'services.html')

    def test_contact_page_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200, "Contact page should load successfully")
        self.assertTemplateUsed(response, 'contact.html')

    def test_post_request_service(self):
        response = self.client.post(reverse('request_service'), self.requested_service_data)
        self.assertEqual(response.status_code, 302, "Request Service form submission should redirect")
        self.assertTrue(ServiceRequest.objects.filter(email="john@gmail.com").exists())

    # def test_post_register_artisan(self):
    #     response = self.client.post(reverse('register_artisan'), self.artisan_data)
    #     self.assertEqual(response.status_code, 302, "Register Artisan form submission should redirect")
    #     self.assertTrue(Artisan.objects.filter(email="jane@gmail.com").exists())
        
    # def test_register_artisan_form_valid(self):
    #     form = ArtisanForm(data=self.artisan_data)
    #     print(form.errors)  # Add this to inspect form validation errors
    #     self.assertTrue(form.is_valid(), "Register Artisan form should be valid with correct data")

