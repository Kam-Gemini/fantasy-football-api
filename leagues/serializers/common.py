from rest_framework import serializers
from ..models import Leagues

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leagues
        fields = '__all__'