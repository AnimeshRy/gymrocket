from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path('all/', views.MemberListView.as_view(), name='member-list'),
    path('add/', views.AddMemberView.as_view(), name='add-member'),
    path('<int:pk>/detail/', views.MemberDetailView.as_view(),
         name='detail-member'),
    path('<int:pk>/update/', views.UpdateMemberView.as_view(), name='update-member'),
    path('<int:pk>/del/', views.DeleteMemberView.as_view(), name='delete-member')
]
