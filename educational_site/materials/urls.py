# # materials/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('upload/', views.upload_material, name='upload_material'),
#     path('delete/<int:pk>/', views.delete_material, name='delete_material'),
#     path('rename/<int:pk>/', views.rename_material, name='rename_material'),
# ]
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('manage/', views.manage_pdfs, name='manage_pdfs'),
    path('browse/', views.browse_pdfs, name='browse_pdfs'),
    # path('download/', views.download_pdfs, name='download_pdfs'),
    path('upload/', views.upload_pdf, name='upload_pdf'),
    path('manage/', views.manage_pdfs, name='manage_pdfs'),
    path('delete/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),
    path('edit/<int:pdf_id>/', views.edit_pdf, name='edit_pdf'),
    path('grade_8/', views.grade_8_pdfs, name='grade_8_pdfs'),
    path('grade-8-pdfs/', views.grade_8_pdfs, name='grade_8_pdfs'),
    path('grade_9/', views.grade_9_pdfs, name='grade_9_pdfs'),
    path('grade_10/', views.grade_10_pdfs, name='grade_10_pdfs'),
    path('materials/download/<int:pdf_id>/', views.download_pdfs, name='download_pdfs'),
    # path('grade/<str:grade>/', views.view_pdfs_by_grade, name='grade_pdfs'),
    path('grade-8-pdfs/', views.grade_8_pdfs, name='grade_pdfs'),
    path('grade-10-pdfs/', views.grade_10_pdfs, name='grade_pdfs'),
    # path('pdfs/<str:grade>/', views.view_pdfs_by_grade, name='grade_pdfs'),
    # path('serve-pdf/<int:pdf_id>/', views.serve_pdf, name='serve_pdf'),
    path('view-pdf/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
    path('download/', views.download_pdfs, name='view_pdf'),
    path('grade_8_pdfsd', views.grade_8_pdfsd, name='grade_8_pdfsd'),
    path('grade_9_pdfsd', views.grade_9_pdfsd, name='grade_9_pdfsd'),
    path('grade_10_pdfsd', views.grade_10_pdfsd, name='grade_10_pdfsd'),
    path('download/<int:pdf_id>/', views.download_pdf, name='download_pdf'),
    

    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
