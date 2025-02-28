from django.db import models
from teams.models import Teams
from users.models import User

# Create your models here.
class Leagues(models.Model):
    league_name = models.CharField(max_length=50)
    teams = models.ManyToManyField(to=Teams, related_name='league_teams', blank=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='league_owner', blank=True, null=True)

    def __str__(self):
        return self.league_name