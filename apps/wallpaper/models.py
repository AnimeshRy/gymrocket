from django.db import models
from django.forms import ModelForm

# Wallpaper Model and Form


class Wallpaper(models.Model):
    photo = models.FileField(upload_to='wallpaper/')


class WallpaperForm(ModelForm):
    class Meta:
        model = Wallpaper
        fields = '__all__'  # File Upload Field
