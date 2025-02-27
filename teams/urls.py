from django.urls import path
from .views import TeamsListView, TeamsDetailView

urlpatterns = [
    path('', TeamsListView.as_view()),
    path('<int:team_id>/', TeamsDetailView.as_view())
]