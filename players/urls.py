from django.urls import path
from .views import PlayersListView, PlayersDetailView

urlpatterns = [
    path('', PlayersListView.as_view()),
    path('<int:player_id>/', PlayersDetailView.as_view())
]