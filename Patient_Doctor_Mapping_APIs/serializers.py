# Patient_Doctor_Mapping_APIs/serializers.py
from rest_framework import serializers
from Patient_Management_APIs.models import Patient   # ✅ use the correct model
from Doctor_Management_APIs.models import Doctor
from .models import PatientDoctorMapping



class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient = serializers.SlugRelatedField(
        queryset=Patient.objects.all(),
        slug_field="name"   # show patient name in dropdown
    )
    doctor = serializers.SlugRelatedField(
        queryset=Doctor.objects.all(),
        slug_field="name"
    )

    patient_name = serializers.CharField(source="patient.name", read_only=True)
    doctor_name = serializers.CharField(source="doctor.name", read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ["id", "patient", "patient_name", "doctor", "doctor_name", "created_at"]
