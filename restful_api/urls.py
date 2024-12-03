from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('journey', views.JourneyViewSet)
router.register('user', views.UserViewSet)
