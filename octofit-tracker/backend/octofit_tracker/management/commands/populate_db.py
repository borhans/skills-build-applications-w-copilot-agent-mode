
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Use pymongo to clear collections directly
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']
        db.teams.delete_many({})
        db.users.delete_many({})
        db.activities.delete_many({})
        db.workouts.delete_many({})
        db.leaderboards.delete_many({})

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(email='tony@marvel.com', username='Iron Man', team=marvel),
            User.objects.create(email='steve@marvel.com', username='Captain America', team=marvel),
            User.objects.create(email='bruce@marvel.com', username='Hulk', team=marvel),
            User.objects.create(email='clark@dc.com', username='Superman', team=dc),
            User.objects.create(email='bruce@dc.com', username='Batman', team=dc),
            User.objects.create(email='diana@dc.com', username='Wonder Woman', team=dc),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='cycle', duration=60, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        w2 = Workout.objects.create(name='Sprints', description='Speed training')
        w1.suggested_for.set([users[0], users[3]])
        w2.suggested_for.set([users[1], users[4]])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
