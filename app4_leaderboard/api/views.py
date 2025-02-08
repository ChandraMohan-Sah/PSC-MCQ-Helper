
from django.shortcuts import render
from app6_upload_question.models import ExamAttempt
from django.db.models import Sum

def leaderboard(request):
    # Get top users ranked by their total score across all exams
    top_users = (
        ExamAttempt.objects.filter(status="Completed")
        .values("user__username")
        .annotate(total_score=Sum("score"))
        .order_by("-total_score")[:10]  # Top 10 users
    )

    return render(request, "app4_leaderboard/leaderboard.html", {"top_users": top_users,"sidebar_content" : "Knowledge Assessment" })
