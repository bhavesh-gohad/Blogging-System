"""BLOGS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myblog import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('addpost/',views.addpost,name="addpost"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.user_logout,name="logout"),
    path('signup/',views.user_signup,name="signup"),
    path('update/<int:id>/',views.update_post,name="update"),
    path('delete_post/<int:id>/',views.delete_post,name="delete_post"),
    path('show/<int:id>/',views.show_post,name="show"),
    path('contact/',views.contact,name="contact"),
    path('profile/<int:id>/',views.show_profile,name="profile"),
    # path('blog/images/passport.jpg/<int:id>',views.show_profile,name="profile"),
    path('editprofile/<int:id>/',views.edit_profile,name="editprofile"),
    path('delete_user/<int:id>/',views.delete_user,name="delete_user"),
    path('changepassword/',views.change_password,name="changepassword"),

    # password reset urls
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='blog/Passwords/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='blog/Passwords/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='blog/Passwords/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='blog/Passwords/password_reset_complete.html'),name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)