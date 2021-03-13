from django.urls import path
from . import views
import calendar

app_name = 'reports'

urlpatterns = [
    path('', views.reports, name='gen-reports'),
]
