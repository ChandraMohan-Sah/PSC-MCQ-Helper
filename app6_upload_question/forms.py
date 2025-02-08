# from django import forms

# class FileUploadForm(forms.Form):
#     file = forms.FileField()


from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField(required=False, label="Upload JSON/CSV File")
    json_text = forms.CharField(widget=forms.Textarea, required=False, label="Paste JSON Here")
