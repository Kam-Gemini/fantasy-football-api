from rest_framework.serializers import ModelSerializer
from ..models import Players

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'