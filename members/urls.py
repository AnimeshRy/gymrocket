from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('all/', views.view_members, name='member-list'),
    path('add/', views.AddMemberView.as_view(), name='add-member'),
]
