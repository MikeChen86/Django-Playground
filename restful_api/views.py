from django.contrib.auth.models import User
from rest_framework import viewsets, permissions

from .serializers.journey import JourneySerializer
from .serializers.auth import UserSerializer
from .models import Journey

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer
