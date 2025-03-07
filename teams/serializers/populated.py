from rest_framework import serializers
from .common import TeamSerializer
from players.serializers.common import PlayerSerializer

class PopulatedTeamSerializer(TeamSerializer):
    goalkeeper = PlayerSerializer()
    defenders = PlayerSerializer(many=True)
    midfielders = PlayerSerializer(many=True)
    forwards = PlayerSerializer(many=True)

    total_cost = serializers.SerializerMethodField()
    total_points = serializers.SerializerMethodField()

    def get_total_cost(self, obj):
        total_cost = 0
        if obj.goalkeeper:
            total_cost += obj.goalkeeper.price
        total_cost += sum(player.price for player in obj.defenders.all())
        total_cost += sum(player.price for player in obj.midfielders.all())
        total_cost += sum(player.price for player in obj.forwards.all())
        return total_cost

    def get_total_points(self, obj):
        total_points = 0
        if obj.goalkeeper:
            total_points += obj.goalkeeper.points
        total_points += sum(player.points for player in obj.defenders.all())
        total_points += sum(player.points for player in obj.midfielders.all())
        total_points += sum(player.points for player in obj.forwards.all())
        return total_points