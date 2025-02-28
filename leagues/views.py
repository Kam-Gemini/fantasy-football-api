from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.middleware.permissions import IsOwnerOrReadOnly
from .models import Leagues
from teams.models import Teams

from .serializers.common import LeagueSerializer
from .serializers.populated import PopulatedLeagueSerializer

# Create your views here.
class LeaguesListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, _request):
        leagues = Leagues.objects.all()
        serialized_leagues = PopulatedLeagueSerializer(leagues, many=True)
        return Response(serialized_leagues.data)
    
    def post(self, request):
        request.data['user'] = request.user.id
        new_league = LeagueSerializer(data=request.data)
        if new_league.is_valid():
            new_league.save()
            return Response(new_league.data, status=201)
        return Response(new_league.errors, status=422)
    
class LeaguesDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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

        if 'team' in data:
            league.teams.set(Teams.objects.filter(id__in=data['team']))

        serialized_league = LeagueSerializer(league, data=request.data, partial=True)
        
        if serialized_league.is_valid():
            serialized_league.save()
            return Response(serialized_league.data)
        
        return Response(serialized_league.errors, status=422)        
    
    def delete(self, request, league_id):
        league = self.get_object(league_id)
        self.check_object_permissions(request, league)
        league.delete()
        return Response(status=204)