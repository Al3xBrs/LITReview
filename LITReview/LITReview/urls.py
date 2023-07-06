"""
URL configuration for LITReview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import articles.views
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeDoneView, PasswordChangeView
from users.views import signup_page, profil_page
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name ="users/login.html", redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('home/', articles.views.home, name="home"),
    path('change-password/', PasswordChangeView.as_view(template_name = 'users/change_password.html'), name="password_change"),
    path('password-change-done/', PasswordChangeDoneView.as_view(template_name = 'users/change_password_success.html'), name="password_change_done"),
    path('signup/', signup_page, name='signup'),
    path("ticket/upload/", articles.views.ticket_upload, name="ticket_upload"),
    path("review/upload/<int:ticket_id>/", articles.views.review_upload, name="review_upload"),
    path("ticket/<int:ticket_id>/", articles.views.ticket_detail, name="ticket_detail"),
    path("ticket-delete/<int:ticket_id>/", articles.views.ticket_delete, name="ticket_delete"),
    path("ticket-delete-view/<int:ticket_id>/", articles.views.ticket_delete_view, name="ticket_delete_view"),
    path("profil/<int:user_id>/", profil_page, name="profil_page"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
