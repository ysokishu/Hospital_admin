
from django.contrib import admin
from .models import Department, Doctor, Patient, Appointment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "specialization",
        "department",
        "phone",
        "is_available",
    )
    search_fields = ("name", "specialization", "email")
    list_filter = ("department", "is_available")


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "date_of_birth",
        "gender",
        "phone",
        "created_at",
    )
    search_fields = ("name", "phone", "email")
    list_filter = ("gender", "created_at")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "patient",
        "doctor",
        "appointment_date",
        "appointment_time",
        "status",
    )
    search_fields = (
        "patient__name",
        "doctor__name",
        "patient__phone",
    )
    list_filter = (
        "status",
        "appointment_date",
        "doctor",
    )
    