from .common import LeagueSerializer
from teams.serializers.common import TeamSerializer

class PopulatedLeagueSerializer(LeagueSerializer):
    teams = TeamSerializer(many=True)