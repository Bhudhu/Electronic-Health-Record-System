from django.test import TestCase
from .models import Patient

class PatientModelTest(TestCase):
    def setUp(self):
        # Create a sample patient for testing
        self.patient = Patient.objects.create(
            first_name="John",
            surname="Doe",
            id_number="1234567890",
            race="Caucasian",
            gender="Male",
            age=30,
            medical_aid_scheme="Medicare",
            medical_aid_number="MED123456",
            previous_surgeries="Appendectomy",
            allergies="None",
            current_prescription="Paracetamol",
            physical_address="123 Main Street",
            height=180,
            weight=75,
            emergency_contact_number="9876543210"
        )

    def test_patient_creation(self):
        """Test if the patient is created successfully."""
        patient = self.patient
        self.assertEqual(patient.first_name, "John")
        self.assertEqual(patient.surname, "Doe")
        self.assertEqual(patient.age, 30)

    def test_string_representation(self):
        """Test the string representation of the Patient model."""
        self.assertEqual(str(self.patient), "John Doe")
