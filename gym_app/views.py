from django.shortcuts import render
from django.http import JsonResponse
from .models import Trainee, WorkoutPlan
from .mongo_client import mongo_db


# Create your views here.
def dashboard_view(request):
    trainee, created = Trainee.objects.get_or_create(
        email="yossi.dbo@ggmail.com",
        defaults={"first_name": "yossi", ""
                                         "last_name": "dbo"}
    )

    plan, _ = WorkoutPlan.objects.get_or_create(
        trainee=trainee,
        plan_name="Hypertrophy A",
        defaults={"target_muscle_group": "Chest & Triceps",
                  "exercises_count": 6}
    )

    log_entry = {
        "trainee_email": trainee.email,
        "action": "STARTED_WORKOUT",
        "plan_name": plan.plan_name,
        "status": "Success"

    }

    mongo_db.logs_collection.insert_one(log_entry)
    recent_logs = list(mongo_db.logs_collection.find({}, {"_id": 0}).limit(5))

    plan_length = len(plan)  # __len__ played
    trainee_str = str(trainee)  # __str__ played

    return JsonResponse({
        "sql_data": {"trainee": trainee_str, "plan": plan_length},
        "mongo_logs": recent_logs
    }, json_dumps_params={'indent': 4})
