# Patient_Doctor_Mapping_APIs/views.py
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

# List all mappings / Create new mapping
class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

# Retrieve / Delete a single mapping
class PatientDoctorMappingDetailView(generics.RetrieveDestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

# List mappings filtered by patient
class PatientDoctorMappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

# Optional: All mappings grouped by patient
class MappingsGroupedByPatientView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        data = {}
        for m in mappings:
            data.setdefault(m.patient.name, []).append({
                "doctor": m.doctor.name,
                "created_at": m.created_at
            })
        return Response(data)
