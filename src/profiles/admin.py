from django.contrib import admin

from src.profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "is_banned")


admin.site.register(Profile, ProfileAdmin)
