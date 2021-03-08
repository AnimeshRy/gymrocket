from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from members.views import LandingPage
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include("members.urls", namespace="members")),
    path('', LandingPage.as_view(), name="landing-page"),

    path('password_change/', PasswordChangeView.as_view(), name='password-change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    # auth routes
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

# for handling profile photos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
