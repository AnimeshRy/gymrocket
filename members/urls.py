from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('', views.view_members, name="member-list")
]
