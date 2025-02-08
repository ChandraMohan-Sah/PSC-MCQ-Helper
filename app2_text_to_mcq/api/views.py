
from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",  # Replace with your API key
)

def generate_mcq(request):
    if request.method == "POST":
        input_text = request.POST.get("text", "")

        if not input_text:
            return JsonResponse({"error": "Text input is required."}, status=400)

        # Prepare API request
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "https://yourwebsite.com",  # Replace with your site URL
                "X-Title": "YourWebsite",  # Replace with your site name
            },
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate 10 multiple-choice questions (MCQ) with 4 options each based on the following text. Also, provide the correct answer for each:\n\n{input_text}",
                }
            ]
        )

        # Extract MCQs from API response
        mcq_data = completion.choices[0].message.content  

        return JsonResponse({"mcqs": mcq_data})
    return render(request, "app2_text_to_mcq/text_to_mcq.html")
 