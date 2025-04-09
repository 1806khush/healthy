from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=255)
    usertype = models.CharField(max_length=20)
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Doctor(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    specialization_choices = (
        ("Cardiology", "Cardiology"),
        ("Dentist", "Dentist"),
        ("Homeopathy", "Homeopathy"),
        ("Neurology", "Neurology"),
        ("Pediatrics", "Pediatrics"),
        ("Traumatology", "Traumatology"),
        ("Radiology", "Radiology"),
     
    )
    

    specialization = models.CharField(max_length=50, choices=specialization_choices, default="Homeopathy")
    
    qualification = (
        ("MBBS", "MBBS"),
        ("MD", "MD"),
        ("MS", "MS"),
        ("DM", "DM"),
    )
    language_choices = (
        ("English", "English"),
        ("Spanish", "Spanish"),
        ("French", "French"),
        ("German", "German"),
        ("Chinese", "Chinese"),
        ("Hindi", "Hindi"),
        ("Arabic", "Arabic"),
        ("Russian", "Russian"),
        ("Portuguese", "Portuguese"),
        ("Japanese", "Japanese"),
        ("Other", "Other"),
    )
      
    experience_level = (
        ("Junior", "Junior"),
        ("Senior", "Senior"),
        ("Consultant", "Consultant"),
        ("Head of Department", "Head of Department"),
    )
    
    highest_qualification = models.CharField(max_length=50, choices=qualification)
    position = models.CharField(max_length=100, choices=experience_level)
    
    name = models.CharField(max_length=100)
    consultation_fee = models.IntegerField(blank=True, null=True)
    emergency_fee = models.IntegerField(blank=True, null=True)
    surgery_fee = models.IntegerField(blank=True, null=True)
    years_of_experience = models.IntegerField()
    languages = models.CharField(max_length=100, choices=language_choices)
    patients_treated = models.IntegerField()
    biography = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True)
    
    morning_availability = models.IntegerField(null=True, blank=True)  # Hours available in morning
    afternoon_availability = models.IntegerField(null=True, blank=True)  # Hours available in afternoon
    evening_availability = models.IntegerField(null=True, blank=True)  # Hours available in evening
    
    telemedicine = models.BooleanField(default=False)
    emergency_service = models.BooleanField(default=False)
    home_visits = models.BooleanField(default=False)
    international_patients = models.BooleanField(default=False)
    insurance_accepted = models.BooleanField(default=False)
    research_publications = models.BooleanField(default=False)
    multilingual = models.BooleanField(default=False)
    weekend_availability = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    


class Booking(models.Model):
    appointment = models.BooleanField(default=True)
    
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    specialization_choices = (
         ("Cardiology", "Cardiology"),
         ("Dentist", "Dentist"),
         ("Homeopathy", "Homeopathy"),
         ("Neurology", "Neurology"),
         ("Pediatrics", "Pediatrics"),
         ("Traumatology", "Traumatology"),
         ("Radiology", "Radiology"),
    )

    
    specialization = models.CharField(max_length=50, choices=specialization_choices, default="Homeopathy")

    
    
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    
    
    reason = models.TextField()

    
    

