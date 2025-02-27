from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import PlayerSerializer
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .models import Players

# Create your views here.
class PlayersListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        players_queryset = Players.objects.all()
        players_serialized = PlayerSerializer(players_queryset, many=True)
        return Response(players_serialized.data)
    
    def post(self, request):
        player = PlayerSerializer(data=request.data)
        if player.is_valid():
            player.save()
            return Response(player.data, 201)
        print(player.errors)
        return Response(player.errors, 422)
    
class PlayersDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, player_id):
        try:
            player = Players.objects.get(id=player_id)
            return player
        except Players.DoesNotExist as e:
            print(e)
            raise NotFound('Player not found')

    def get(self, request, player_id):
        player = self.get_object(player_id)
        serialized_player = PlayerSerializer(player)
        return Response(serialized_player.data)
    
    def put(self, request, player_id):
        try:
            player = Players.objects.get(id=player_id)
            serialized_player = PlayerSerializer(player, data=request.data, partial=True)
            if serialized_player.is_valid():
                serialized_player.save()
                return Response(serialized_player.data, 201)
            print(serialized_player.errors)
            return Response(serialized_player.errors, 422)

        except player.DoesNotExist as e:
            print(e)
            raise NotFound('Player not found')
    
    def delete(self, request, player_id):
        try:
            player = Players.objects.get(id=player_id)
            player.delete()
            return Response(status=204)
        except Players.DoesNotExist as e:
            print(e)
            raise NotFound('Player not found')