from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Leagues
from teams.models import Teams
from .serializers.common import LeagueSerializer
from .serializers.populated import PopulatedLeagueSerializer

class LeaguesListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, _request):
        leagues = Leagues.objects.all()
        serialized_leagues = PopulatedLeagueSerializer(leagues, many=True)
        return Response(serialized_leagues.data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        league_to_add = LeagueSerializer(data=request.data)
        if league_to_add.is_valid():
            league_to_add.save()
            return Response(league_to_add.data, status=201)
        return Response(league_to_add.errors, status=422)

class LeaguesDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, league_id):
        try:
            league = Leagues.objects.get(id=league_id)
            return league
        except Leagues.DoesNotExist as e:
            print(e)
            raise NotFound('League not found.')

    def get(self, request, league_id):
        league = self.get_object(league_id)
        serialized_league = PopulatedLeagueSerializer(league)
        return Response(serialized_league.data)

    def put(self, request, league_id):
        league = self.get_object(league_id)
        data = request.data

        if 'teams' in data:
            league.teams.set(Teams.objects.filter(id__in=data['teams']))

        serialized_league = LeagueSerializer(league, data=request.data, partial=True)
        
        if serialized_league.is_valid():
            serialized_league.save()
            populated_serializer = PopulatedLeagueSerializer(league)
            return Response(populated_serializer.data)
        
        return Response(serialized_league.errors, status=422)        
    
    def delete(self, request, league_id):
        league = self.get_object(league_id)
        league.delete()
        return Response(status=204)