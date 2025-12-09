from rest_framework import serializers
from .common import LeagueSerializer
from teams.serializers.league import LeagueTeamSerializer

class PopulatedLeagueSerializer(LeagueSerializer):
    teams = LeagueTeamSerializer(many=True)

    class Meta(LeagueSerializer.Meta):
        fields = LeagueSerializer.Meta.fields