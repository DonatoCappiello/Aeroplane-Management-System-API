from rest_framework import serializers

from .models import Aeroplanes

class AeroplanesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Aeroplanes
        fields = '__all__'