#define URLs where to serve data Django router
#author Donato Cappiello

from .api import AeroplanesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'aeroplanes', AeroplanesViewSet)

urlpatterns = router.urls