from django.test import TestCase
from unittest.mock import patch
from .models import Trainee,WorkoutPlan
from .mongo_client import  Mongo_Service

# Create your tests here.
class GymSystemModelTests(TestCase):
    def setUp(self):
        self.trainee = Trainee.objects.create(
            first_name='John',
            last_name='Levi',
            email='jhon.levi@ggmail.com'
        )

    def test_trainee_string_representation(self):
        self.assertEqual(str(self.trainee),'John Lvei')

    def test_workout_plan_dunder_len(self):
        plan = WorkoutPlan.objects.create(
            trainee=self.trainee,
            plan_name='Legs',
            exercises_count=20
        )

        self.assertEqual(plan.exercises_count,20)