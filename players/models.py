from django.db import models

POSITION = [
    ('Goalkeeper', 'Goalkeeper'),
    ('Defender', 'Defender'),
    ('Midfielder', 'Midfielder'),
    ('Forward', 'Forward'),
]

# Create your models here.
class Players(models.Model):
    image = models.ImageField(upload_to='image/', default='image/default.jpg')
    name = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    position = models.CharField(max_length=50, choices=POSITION)
    price = models.FloatField()
    appearances = models.IntegerField(null=True, blank=True)
    goals = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    cleansheets = models.IntegerField(null=True, blank=True)
    yellow_cards = models.IntegerField(null=True, blank=True)
    red_cards = models.IntegerField(null=True, blank=True)
    own_goals = models.IntegerField(null=True, blank=True)
    pens_saved = models.IntegerField(null=True, blank=True)
    points = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name