from django.shortcuts import render
from django.http import JsonResponse
from .models import Trainee, WorkoutPlan
from .mongo_client import mongo_db
#
#
# # Create your views here.
# def dashboard_view(request):
#     trainee, created = Trainee.objects.get_or_create(
#         email="yossi.dbo@ggmail.com",
#         defaults={"first_name": "yossi", ""
#                                          "last_name": "dbo"}
#     )
#
#     plan, _ = WorkoutPlan.objects.get_or_create(
#         trainee=trainee,
#         plan_name="Hypertrophy A",
#         defaults={"target_muscle_group": "Chest & Triceps",
#                   "exercises_count": 6}
#     )
#
#     log_entry = {
#         "trainee_email": trainee.email,
#         "action": "STARTED_WORKOUT",
#         "plan_name": plan.plan_name,
#         "status": "Success"
#
#     }
#
#     mongo_db.logs_collection.insert_one(log_entry)
#     recent_logs = list(mongo_db.logs_collection.find({}, {"_id": 0}).limit(5))
#
#     plan_length = len(plan)  # __len__ played
#     trainee_str = str(trainee)  # __str__ played
#
#     return JsonResponse({
#         "sql_data": {"trainee": trainee_str, "plan": plan_length},
#         "mongo_logs": recent_logs
#     }, json_dumps_params={'indent': 4})
def dashboard_view(request):
    """
    include searching and filtering in view
    exe: by status from Mongo?status=Success
    exe: by name from sql server ?search=yossi

    """
    status_filter = request.GET.get('status',None)
    search_query = request.GET.get('search_query',None)

    trainees_query = Trainee.objects.all()
    if search_query:
        trainees_query = trainees_query.filter(first_name__icontains=search_query)

    serialized_trainees = [
        {"id":t.id,"name":f"{t.first_name} {t.last_name}","email":t.email}
        for t in trainees_query
    ]

    mongo_query={}
    if status_filter:
        mongo_query = mongo_db(status_filter)

    recent_logs = list(mongo_db.logs_collection.find(mongo_query,{"_id":0}).limit(10))


    return JsonResponse({
        "filters_applied":{
            "search_trainee":search_query,
            "mongo_status":status_filter
        },
        "sql_server_results":serialized_trainees,
        "mongo_db_logs":recent_logs
    },json_dumps_params={'indent':4})