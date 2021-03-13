from django.urls import path
from . import views
import calendar

app_name = 'reports'

urlpatterns = [
    path('', views.reports, name='gen-reports'),
    path('export/', views.export_all, name='export'),
    path('export/<int:pk>/member/', views.export_single, name='export-single'),
]
