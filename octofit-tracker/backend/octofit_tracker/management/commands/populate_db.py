from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Equipo Marvel')
        dc = Team.objects.create(name='DC', description='Equipo DC')

        # Crear usuarios superhéroes
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel', is_superhero=True)
        spiderman = User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', is_superhero=True)
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC', is_superhero=True)
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC', is_superhero=True)

        # Crear actividades
        Activity.objects.create(user='Iron Man', type='Running', duration=30, date='2025-10-15')
        Activity.objects.create(user='Spider-Man', type='Cycling', duration=45, date='2025-10-15')
        Activity.objects.create(user='Batman', type='Swimming', duration=60, date='2025-10-15')
        Activity.objects.create(user='Superman', type='Yoga', duration=20, date='2025-10-15')

        # Crear leaderboard
        Leaderboard.objects.create(team='Marvel', points=100, rank=1)
        Leaderboard.objects.create(team='DC', points=90, rank=2)

        # Crear workouts
        Workout.objects.create(name='Push Ups', description='Flexiones de brazos', difficulty='Medium')
        Workout.objects.create(name='Squats', description='Sentadillas', difficulty='Easy')
        Workout.objects.create(name='Plank', description='Plancha abdominal', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db poblada con datos de prueba (superhéroes, equipos, actividades, leaderboard y workouts).'))
