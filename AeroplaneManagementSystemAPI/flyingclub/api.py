from rest_framework.viewsets import ModelViewSet

from .serializers import AeroplanesSerializer
from .models import Aeroplanes

class AeroplanesViewSet(ModelViewSet):
    queryset = Aeroplanes.objects.all()
    serializer_class = AeroplanesSerializer   