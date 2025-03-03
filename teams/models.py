from django.db import models
from django.core.exceptions import ValidationError
from players.models import Players
from users.models import User

# Create your models here.
class Teams(models.Model):
    team_name = models.CharField(max_length=50)
    goalkeeper = models.ForeignKey(to=Players, on_delete=models.SET_NULL, related_name='teams_as_goalkeeper', null=True, blank=True)
    defenders = models.ManyToManyField(to=Players, related_name='team_defenders', null=True, blank=True)
    midfielders = models.ManyToManyField(to=Players, related_name='team_midfielders', null=True, blank=True)
    forwards = models.ManyToManyField(to=Players, related_name='team_forwards', null=True, blank=True)
    total_cost = models.IntegerField(blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='own_team', blank=True, null=True)

    def __str__(self):
        return self.team_name
    