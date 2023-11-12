"""
URL configuration for website project.

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
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from src.profiles.urls import urlpatterns as profiles_urlpatterns
from src.restaurants.urls import urlpatterns as restaurants_urlpatterns


# urlpatterns = [
#     path('', index, name='index'),
#     path('students/', students, name="students"),
#     path('user/', include('users.urls')),
#     path('bboard/', include('bboard.urls')),
#     path('admin/', admin.site.urls),
#     path('post/<int:post_id>/', posts_detail, name='posts_detail'),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('create/', create, name="create"),
#     path('comments/', comments, name="comments"),
#     path('posts/', posts, name="posts"),
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(profiles_urlpatterns)),
    path("", include(restaurants_urlpatterns)),
    path("grappelli/", include("grappelli.urls")),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
