from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="base"),
    path('memberchart/', views.member_chart, name="member-chart"),
    path('paymentchart/', views.payment_chart, name="payment-chart")
]
