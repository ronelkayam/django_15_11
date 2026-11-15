from django.contrib import admin
from .models import Trainee,WorkoutPlan
from .mongo_client import *


# Register your models here.
@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','joined_date')



@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('id','plan_name','trainee,target_muscle_group','exercises_count')

# @admin.register(MongoWorkoutLog)
# class MongoWorkoutLogAdmin(admin.ModelAdmin):
#     pass
