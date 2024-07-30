from django.contrib import admin
from django.urls import path, include
from . import views,user_login

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n"))
]

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),

    path("base", views.BASE, name="base"),
    path("404",views.PAGE_NOT_FOUND,name="404"),

    path("",views.HOME,name="home"),
    path("search",views.SEARCH_COURSE,name="search_course"),
    path("course/<slug:slug>",views.COURSE_DETAILS,name="course_details"),
    path("courses",views.SINGLE_COURSE, name="single_course"),
    path("contact", views.CONTACT_US, name="contact_us"),
    path("about", views.ABOUT_US, name="about_us"),
    path("packages", views.PACKAGES, name="packages"),


    path("accounts/register", user_login.REGISTER,name='register'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("doLogin",user_login.DO_LOGIN,name="doLogin"),
    path("logout",user_login.LOGOUT,name="logout"),
    path("accounts/profile",user_login.PROFILE,name="profile"),
    path("accounts/profile/update",user_login.PROFILE_UPDATE,name="profile_update"),
) + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
