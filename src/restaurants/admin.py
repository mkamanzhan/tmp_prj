from django.contrib import admin

from src.restaurants.models import Restaurant, Review


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "is_active", "rating")


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("restaurant", "user", "text", "rating")


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Review, ReviewAdmin)
