from rest_framework.serializers import ModelSerializer
from ..models import Players

class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

class PlayerNamePriceSerializer(ModelSerializer):
    class Meta:
        model = Players
        fields = ['name', 'price']