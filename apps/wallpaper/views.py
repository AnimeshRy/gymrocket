from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Wallpaper, WallpaperForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


@login_required
def set_wallpaper(request):
  # Wallpaper Change Route in Base URL
    if request.method == 'POST':
        form = WallpaperForm(request.POST, request.FILES)
        if form.is_valid():
            if Wallpaper.objects.filter()[:1].exists():
                object = Wallpaper.objects.filter()[:1].get()
                # for updating photo
                if 'photo' in request.FILES:
                    myfile = request.FILES['photo']
                    fs = FileSystemStorage(
                        base_url=settings.WALLPAPER_URL, location=settings.WALLPAPER_FILES)
                    photo = fs.save(myfile.name, myfile)
                    object.photo = fs.url(photo)
                object.save()
            else:
                form.save()
        return render(request, 'wallpaper/set_wallpaper.html', {'form': WallpaperForm(), 'success': 'Successfully Changed the Wallpaper!'})
    else:
        return render(request, 'wallpaper/set_wallpaper.html', {'form': WallpaperForm()})
