# Generated by Django 4.2.19 on 2025-02-27 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0003_alter_teams_total_cost_alter_teams_total_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='own_team', to=settings.AUTH_USER_MODEL),
        ),
    ]
