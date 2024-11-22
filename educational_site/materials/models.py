from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

# Validator function to ensure only PDFs are uploaded
def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError("Only PDF files are allowed.")

class PDF(models.Model):
    
    file = models.FileField(upload_to='pdfs/', validators=[validate_pdf]) 
 
    name = models.CharField(max_length=255, unique=True)


    # Subject and grade fields for categorization
    subject = models.CharField(max_length=100)  
    grade = models.CharField(max_length=50)  

    # Timestamp for when the PDF is uploaded
    uploaded_at = models.DateTimeField(auto_now_add=True)  
    
    def save(self, *args, **kwargs):
        # Automatically set a meaningful name if it is empty or invalid
        if not self.name or self.name.isdigit():
            self.name = f"{self.subject} {self.grade}"  # Example: "Math Grade 10"
        super().save(*args, **kwargs)

    def __str__(self):
        # String representation to include the PDF name, subject, and grade
        return f"{self.name} - {self.subject} - {self.grade}"
