from django.urls import path
##from rest_framework_simplejwt
## import TokenObtainPairView, TokenRefreshView
from .views import RegisterView , CustomLoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    
]