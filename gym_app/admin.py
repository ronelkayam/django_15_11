from django.contrib import admin
from .models import Trainee, WorkoutPlan

@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'joined_date')

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    # שים לב שכל שדה כאן מוקף בגרשיים ומופרד בפסיק ברור!
    list_display = ('id', 'plan_name', 'trainee', 'target_muscle_group', 'exercises_count', 'is_active')
    list_filter = ('target_muscle_group', 'is_active')
    search_fields = ('plan_name', 'trainee__first_name', 'trainee__email')