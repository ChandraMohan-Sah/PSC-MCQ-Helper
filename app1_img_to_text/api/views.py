
import requests
from django.shortcuts import render
import os
import imghdr

OCR_API_URL = "https://api.ocr.space/parse/image"  
OCR_API_KEY = "K88802554388957"  


def ocr_view(request):
    extracted_text = ""
    if request.method == 'POST' and request.FILES.get('image_file'):
        image_file = request.FILES['image_file']

        # Check if the image size is less than 950 KB
        if image_file.size > 950 * 1024:
            return render(request, 'app1_img_to_text/ocr_template.html', {
                'extracted_text': "",
                "error_message": "Only images with a size less than 950 KB are acceptable.",
                "sidebar_content": "Knowledge Assessment"
            })

        # Check if the uploaded file is an image (not a PDF or other format)
        image_type = imghdr.what(image_file)
        if image_type is None:
            return render(request, 'app1_img_to_text/ocr_template.html', {
                'extracted_text': "",
                "error_message": "Only image files are allowed, no PDF or other formats.",
                "sidebar_content": "Knowledge Assessment"
            })

        # Send request to OCR API
        response = requests.post(
            OCR_API_URL,
            files={"file": image_file},
            data={"apikey": OCR_API_KEY, "language": "eng"}
        )

        # Extract text from response
        ocr_result = response.json()
        if ocr_result.get("ParsedResults"):
            extracted_text = ocr_result["ParsedResults"][0]["ParsedText"]
    
    context = {
        'extracted_text': extracted_text,
        "sidebar_content": "Knowledge Assessment"
    }
    return render(request, 'app1_img_to_text/ocr_template.html', context)



from django.http import HttpResponse

def download_txt(request):
    if request.method == 'POST':
        extracted_text = request.POST.get('extracted_text')

        # Create the response to download the text file
        response = HttpResponse(
            extracted_text,
            content_type='text/plain'
        )
        response['Content-Disposition'] = 'attachment; filename="extracted_text.txt"'
        return response
    return render(request, 'app1_img_to_text/ocr_template.html')
