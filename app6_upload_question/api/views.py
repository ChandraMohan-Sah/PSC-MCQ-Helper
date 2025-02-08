import json
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from app6_upload_question.models import MCQ
from app6_upload_question.forms import FileUploadForm

def upload_mcq(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES.get('file')
            json_text = form.cleaned_data['json_text']

            if file:
                file_ext = file.name.split('.')[-1]
                if file_ext == 'json':
                    handle_json_upload(file)
                elif file_ext == 'csv':
                    handle_csv_upload(file)
                else:
                    messages.error(request, "Invalid file format! Upload JSON or CSV.")
                    return redirect('upload_mcq')

            elif json_text:
                try:
                    data = json.loads(json_text)
                    handle_json_data(data)
                except json.JSONDecodeError:
                    messages.error(request, "Invalid JSON format! Please check your input.")
                    return redirect('upload_mcq')

            else:
                messages.error(request, "Please provide a JSON file or paste JSON text.")
                return redirect('upload_mcq')

            messages.success(request, "MCQs uploaded successfully!")
            return redirect('upload_mcq')

    else:
        form = FileUploadForm()

    return render(request, 'app6_upload_question/upload.html', {'form': form, "sidebar_content": "Knowledge Assessment"})

def handle_json_upload(file):
    """Handles JSON file upload."""
    data = json.load(file)
    handle_json_data(data)

def handle_json_data(data):
    """Processes JSON data and saves it to the database."""
    mcq_objects = [
        MCQ(
            question=item["question"],
            option1=item["option1"],
            option2=item["option2"],
            option3=item["option3"],
            option4=item["option4"],
            correct_answer=item["correct_answer"]
        ) for item in data
    ]
    MCQ.objects.bulk_create(mcq_objects)

def handle_csv_upload(file):
    """Handles CSV file upload."""
    df = pd.read_csv(file)
    mcq_objects = [
        MCQ(
            question=row["question"],
            option1=row["option1"],
            option2=row["option2"],
            option3=row["option3"],
            option4=row["option4"],
            correct_answer=row["correct_answer"]
        ) for _, row in df.iterrows()
    ]
    MCQ.objects.bulk_create(mcq_objects)
