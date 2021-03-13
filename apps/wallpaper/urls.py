from django.urls import path
from . import views

app_name = "wallpaper"

urlpatterns = [
    path('change/', views.set_wallpaper, name='change')
]
