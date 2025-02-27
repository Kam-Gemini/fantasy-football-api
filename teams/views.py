from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Teams
from players.models import Players

from .serializers.common import TeamSerializer
from .serializers.populated import PopulatedTeamSerializer

class TeamsListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, _request):
        teams = Teams.objects.all()
        serialized_teams = PopulatedTeamSerializer(teams, many=True)
        return Response(serialized_teams.data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        team_to_add = TeamSerializer(data=request.data)
        if team_to_add.is_valid():
            team_to_add.save()
            return Response(team_to_add.data, status=201)
        return Response(team_to_add.errors, status=422)
    
class TeamsDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, team_id):
        try:
            team = Teams.objects.get(id=team_id)
            return team
        except Teams.DoesNotExist as e:
            print(e)
            raise NotFound('Team not found.')

    def get(self, request, team_id):
        team = self.get_object(team_id)
        serialized_team = PopulatedTeamSerializer(team)
        return Response(serialized_team.data)

    def put(self, request, team_id):
        team = self.get_object(team_id)
        data = request.data

        if 'goalkeeper' in data:
            team.goalkeeper = Players.objects.get(id=data['goalkeeper'])
        if 'defenders' in data:
            team.defenders.set(Players.objects.filter(id__in=data['defenders']))
        if 'midfielders' in data:
            team.midfielders.set(Players.objects.filter(id__in=data['midfielders']))
        if 'forwards' in data:
            team.forwards.set(Players.objects.filter(id__in=data['forwards']))

        serialized_team = TeamSerializer(team, data=request.data, partial=True)
        
        if serialized_team.is_valid():
            serialized_team.save()
            populated_serializer = PopulatedTeamSerializer(team)
            return Response(populated_serializer.data)
        
        return Response(serialized_team.errors, 422)
    
    def delete(self, request, team_id):
        team = self.get_object(team_id)
        team.delete()
        return Response(status=204)