from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', description='Marvel team')
        self.assertEqual(str(team), 'Marvel')
    def test_create_user(self):
        team = Team.objects.create(name='DC', description='DC team')
        user = User.objects.create(email='batman@dc.com', username='batman', team=team)
        self.assertEqual(str(user), 'batman@dc.com')
    def test_create_activity(self):
        team = Team.objects.create(name='X-Men', description='Mutants')
        user = User.objects.create(email='logan@xmen.com', username='wolverine', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, date='2025-12-11')
        self.assertEqual(str(activity), 'logan@xmen.com - run')
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body')
        self.assertEqual(str(workout), 'Pushups')
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Avengers', description='Earth heroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Avengers - 100')
