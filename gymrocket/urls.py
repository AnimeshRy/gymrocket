from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.members.views import LandingPage
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),

    # App routes
    path('members/', include("apps.members.urls", namespace="members")),
    path('wallpaper/', include("apps.wallpaper.urls", namespace="wallpaper")),
    path('reports/', include("apps.reports.urls", namespace="reports")),
    path('dashboard/', include("apps.dashboard.urls", namespace="dashboard")),

    # Landing Page route
    path('', LandingPage.as_view(), name="landing-page"),

    # password change routes
    path('password_change/', PasswordChangeView.as_view(), name='password-change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # auth routes
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

# for handling profile photos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Handling Static files in Debug mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
