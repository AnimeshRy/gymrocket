from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('', views.test_page, name="test")
]
