from django import forms
from .models import PDF

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['file', 'subject', 'grade']
        widgets = {
            'subject': forms.Select(attrs={
                'class': 'w-full p-3 border rounded',
            }),
            'grade': forms.Select(attrs={
                'class': 'w-full p-3 border rounded',
            }),
        }
        labels = {
            'file': 'PDF File',
            'subject': 'Subject',
            'grade': 'Grade',
        }
