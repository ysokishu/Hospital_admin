
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="doctors"
    )

    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.name}"


class Patient(models.Model):
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("CONFIRMED", "Confirmed"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    patient = models.ForeignKey(
        Patient,
        on_delete=models.PROTECT,
        related_name="appointments"
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.PROTECT,
        related_name="appointments"
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="SCHEDULED"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["appointment_date", "appointment_time"]

    def __str__(self):
        return (
            f"{self.patient.name} - "
            f"Dr. {self.doctor.name} - "
            f"{self.appointment_date}"
        )