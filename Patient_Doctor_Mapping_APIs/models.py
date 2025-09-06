# Patient_Doctor_Mapping_APIs/models.py
from django.db import models
from Patient_Management_APIs.models import Patient   # ✅ import only
from Doctor_Management_APIs.models import Doctor     # ✅ import only


class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="mappings")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')  # prevent duplicate assignments

    def __str__(self):
        return f"{self.patient.name} ↔ {self.doctor.name}"
