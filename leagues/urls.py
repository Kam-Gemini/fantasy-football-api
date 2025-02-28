from django.urls import path
from .views import LeaguesListView, LeaguesDetailView

urlpatterns = [
    path('', LeaguesListView.as_view()),
    path('<int:league_id>/', LeaguesDetailView.as_view())
]