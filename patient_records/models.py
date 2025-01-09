from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    id_number = models.CharField(max_length=20, unique=True)
    race = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    medical_aid_scheme = models.CharField(max_length=100, blank=True)
    medical_aid_number = models.CharField(max_length=100, blank=True)
    previous_surgeries = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    current_prescription = models.TextField(blank=True)
    address = models.TextField()
    height = models.FloatField()
    weight = models.FloatField()
    emergency_contact = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='patient_pictures/')
    
    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.id_number}"
