from django.urls import path

from src.restaurants.views import (
    main,
    restaurants_detail_view,
    reviews_view,
    about_view,
)

urlpatterns = [
    path("", main, name="main"),
    path(
        "restaurants/<int:restaurant_id>/",
        restaurants_detail_view,
        name="restaurants-detail",
    ),
    path("reviews/", reviews_view, name="reviews"),
    path("about/", about_view, name="about"),
]
