from django.urls import path

from src.restaurants.views import (
    main,
    restaurants_detail_view,
    reviews_view,
)

urlpatterns = [
    path("", main, name="main"),
    path("restaurants/<int:restaurant_id>/", restaurants_detail_view, name="restaurants-detail"),
    path("reviews/", reviews_view, name="reviews"),
#     path("students/", students, name="students"),
#     path("posts/<int:post_id>/", posts_detail, name="posts-detail"),
#     path("posts/create/", posts_create, name="posts-create"),
#     path("comments/create/", comments_create, name="comments-create"),
]
