from django.db import models


# Create your models here.
class Trainee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"<Trainee(id={self.id}, email='{self.email}')>"


class WorkoutPlan(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE,related_name='workout_plan')
    plan_name = models.CharField(max_length=100)
    target_muscle_group = models.CharField(max_length=20)
    exercises_count = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"Plan: {self.plan_name} [Target: {self.target_muscle_group}]"

    def __len__(self):
        return self.exercises_count