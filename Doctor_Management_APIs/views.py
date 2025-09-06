from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework import permissions

# POST & GET list
class DoctorListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# GET single, PUT, DELETE
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Doctor.objects.filter(user=self.request.user)