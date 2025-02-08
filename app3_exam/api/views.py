from django.shortcuts import render, redirect
from django.contrib.auth import logout
from datetime import date, timedelta
from app6_upload_question.models import MCQ, ExamAttempt
from django.core.paginator import Paginator
from datetime import date

def exam(request):
    context = {
        "sidebar_content" : "Knowledge Assessment"
    }
    return render(request, 'app3_exam/exam.html', context) 


def custom_logout_view(request):
    logout(request)  
    return redirect('exam')  


def exam_status(request):
    today = date.today()
    exam_dates = MCQ.objects.values('created_at__date').distinct().order_by('-created_at__date')  # Get distinct dates only
    exam_status = []

    for exam_date in exam_dates:
        exam_date = exam_date['created_at__date']  # Extract date from the queryset
        
        # Check if the user has attempted the exam for this date
        exam_attempt = ExamAttempt.get_exam_status(request.user, exam_date)

        if exam_attempt is None:
            # If there's no exam attempt for this date, create a pending exam status
            exam_attempt = ExamAttempt.objects.create(user=request.user, exam_date=exam_date)
            status = 'Pending'
            score = 0  # Score 0 if not attempted
        else:
            status = exam_attempt.status
            score = exam_attempt.score
        
        exam_status.append({'date': exam_date, 'status': status, 'score': score})
    
    # Paginate the exam statuses (7 per page)
    paginator = Paginator(exam_status, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'app3_exam/check_status.html', {
        'exam_status': page_obj,  # Send paginated exam status
        'sidebar_content': "Knowledge Assessment"
    })



def take_exam(request, exam_date_str):
    exam_date = date.fromisoformat(exam_date_str)  # Assuming exam_date is passed in 'YYYY-MM-DD' format
    questions = MCQ.objects.filter(created_at__date=exam_date)

    paginator = Paginator(questions, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    timer_minutes = 10
    is_exam_page = request.path.startswith('/app3_exam/exam/take/')


    if request.method == "POST":
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        
        # Retrieve or create ExamAttempt for the specific exam_date
        exam_attempt, created = ExamAttempt.objects.get_or_create(user=request.user, exam_date=exam_date)
        
        # Mark the exam as completed and update the score
        exam_attempt.mark_completed(score)
        exam_attempt.save()  # Ensure the changes are saved
        
        return redirect('exam_status')

    return render(request, 'app3_exam/take_exam.html', {
        'page_obj': page_obj,
        'sidebar_content': "Knowledge Assessment",
        'is_exam_page': is_exam_page,  # Pass the flag to template
        'exam_date': exam_date_str,    # Pass the exam date to the template
    })


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden


def review_exam(request, exam_date_str):
    exam_date = date.fromisoformat(exam_date_str)
    questions = MCQ.objects.filter(created_at__date=exam_date)

    # Ensure the user has completed the exam
    exam_attempt = get_object_or_404(ExamAttempt, user=request.user, exam_date=exam_date)

    # Create a list of tuples with question and correct answer
    questions_and_answers = [(q.question, q.correct_answer) for q in questions]

    return render(request, 'app3_exam/review_exam.html', {
        'questions_and_answers': questions_and_answers,
        'exam_date': exam_date_str,
        'sidebar_content': "Knowledge Assessment",
    })









