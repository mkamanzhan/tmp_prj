from django.urls import path

from src.restaurants.views import (
    main,
)

urlpatterns = [
    path("", main, name="main"),
#     path("students/", students, name="students"),
#     path("posts/<int:post_id>/", posts_detail, name="posts-detail"),
#     path("posts/create/", posts_create, name="posts-create"),
#     path("comments/create/", comments_create, name="comments-create"),
]
