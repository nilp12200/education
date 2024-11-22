from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# materials/views.py
from django.shortcuts import render, redirect, get_object_or_404



def home(request):
    return render(request,'home.html')


def teacher_dashboard(request):
    return render(request,'teacher.html')




def student_dashboard(request):
    return render(request,'student.html')

def upload_pdf(request):
    # Logic for uploading PDFs
    return render(request, 'upload.html')

def download_pdfs(request):
    # Logic for uploading PDFs
    return render(request, 'download.html')

def manage_pdfs(request):
    pdfs = PDF.objects.all()
    # Logic for managing PDFs
    return render(request, 'manage.html', {'pdfs':pdfs})

def browse_pdfs(request):
    # Logic for browsing PDFs
    return render(request, 'browse.html')





from django.shortcuts import render, get_object_or_404, redirect
from .models import PDF



from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadPDFForm
from .models import PDF
from django.shortcuts import render, get_object_or_404, redirect
from .models import PDF

def upload_pdf(request):
    if request.method == 'POST' and request.FILES['pdf_file']:
        pdf_file = request.FILES['pdf_file']
        name = request.POST['name']
        subject = request.POST['subject']
        grade = request.POST['grade']
        
        # Save the uploaded PDF to the database
        new_pdf = PDF(file=pdf_file, subject=subject, grade=grade,name=name)
        new_pdf.save()
        return redirect('manage_pdfs')
        
        return HttpResponse('PDF uploaded successfully!')
    
    return render(request, 'upload.html')

def manage_pdfs(request):
    pdfs = PDF.objects.all()
    return render(request, 'manage.html', {'pdfs': pdfs})

def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, pk=pdf_id)
    pdf.delete()
    return redirect('manage_pdfs')

# def delete_pdf(request, pdf_id):
#     pdf = get_object_or_404(PDF, pk=pdf_id)
#     pdf.delete()
#     return redirect('manage_pdfs')




def edit_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES, instance=pdf)
        if form.is_valid():
            form.save()
            return redirect('manage_pdfs')  # Redirect to the manage page
    else:
        form = UploadPDFForm(instance=pdf)
    
    return render(request, 'edit_pdf.html', {'form': form, 'pdf': pdf})


from django.shortcuts import render, get_object_or_404
from .models import PDF

def browse_pdfs(request):
    pdfs = PDF.objects.all()
    return render(request, 'browse.html', {'pdfs': pdfs})



from django.shortcuts import render

from django.shortcuts import render
from .models import PDF

# def grade_8_pdfs(request):
#     # Filter PDFs with grade value 8
#     grade_8_pdfs = PDF.objects.filter(grade='Grade 8')
#     # print(grade_8_pdfs) 
#     return render(request, 'grade_8_pdfs.html', {'pdfs': grade_8_pdfs})
from django.shortcuts import render, get_object_or_404
from .models import PDF


def grade_8_pdfs(request):
    # Filter PDFs with grade value 8
    grade_8_pdfs = PDF.objects.filter(grade='Grade 8')
    # print(grade_8_pdfs) 
    return render(request, 'grade_8_pdfs.html', {'pdfs': grade_8_pdfs})

def grade_9_pdfs(request):
    # Filter PDFs with grade value 8
    grade_9_pdfs = PDF.objects.filter(grade='Grade 9')
    # print(grade_8_pdfs) 
    return render(request, 'grade_9_pdfs.html', {'pdfs': grade_9_pdfs})
def grade_10_pdfs(request):
    # Filter PDFs with grade value 8
    grade_10_pdfs = PDF.objects.filter(grade='Grade 10')
    # print(grade_8_pdfs) 
    return render(request, 'grade_10_pdfs.html', {'pdfs': grade_10_pdfs})

# from django.http import FileResponse
# from django.shortcuts import get_object_or_404
# from .models import PDF

# def view_pdf(request, pdf_id):
#     """
#     Serve a PDF file for inline viewing in the browser.
#     """
#     pdf = get_object_or_404(PDF, id=pdf_id)
#     file_path = pdf.file.path  # Get the path of the PDF file
#     response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     response['Content-Disposition'] = f'inline; filename="{pdf.subject}.pdf"'
#     return response
from django.shortcuts import get_object_or_404
from django.http import FileResponse, HttpResponse
from .models import PDF

def view_pdf(request, pdf_id):
    pdf = get_object_or_404(PDF, id=pdf_id)
    if pdf.file.name.endswith('.pdf'):
        return FileResponse(open(pdf.file.path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponse("This file is not a valid PDF.", status=400)




def grade_8_pdfsd(request):
    # Filter PDFs with grade value 8
    grade_8_pdfs = PDF.objects.filter(grade='Grade 8')
    # print(grade_8_pdfs) 
    return render(request, 'downloadgrade_8_pdfs.html', {'pdfs': grade_8_pdfs})

from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from .models import PDF  # Replace with your actual model

def download_pdf(request, pdf_id):
    # Fetch the PDF object using the ID
    pdf = get_object_or_404(PDF, id=pdf_id)
    try:
        # Serve the file as an attachment
        response = FileResponse(open(pdf.file.path, 'rb'), as_attachment=True)
        return response
    except FileNotFoundError:
        raise Http404("PDF not found")

def grade_9_pdfsd(request):
    # Filter PDFs with grade value 8
    grade_9_pdfs = PDF.objects.filter(grade='Grade 9')
    # print(grade_8_pdfs) 
    return render(request, 'downloadgrade_9_pdfs.html', {'pdfs': grade_9_pdfs})

def grade_10_pdfsd(request):
    # Filter PDFs with grade value 8
    grade_10_pdfs = PDF.objects.filter(grade='Grade 10')
    # print(grade_8_pdfs) 
    return render(request, 'downloadgrade_10_pdfs.html', {'pdfs': grade_10_pdfs})
