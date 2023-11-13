from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404


from src.profiles.models import Profile


def login_view(request):
    if request.method == "GET":
        template = loader.get_template("pages/login.html")
        return HttpResponse(template.render({}, request))
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in")
            return redirect("main")
        else:
            messages.error(request, "Login error")
            return redirect("login")
    return redirect("main")


def register_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        User.objects.create_user(username=email, email=email, password=password)
        messages.success(request, "You have successfully registered")
        return redirect("login")
    return redirect("main")


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("main")


def profile_view(request):
    if request.method == "GET":
        template = loader.get_template("pages/profile.html")
        user_id = request.user.id
        profile = get_object_or_404(Profile, user_id=user_id)
        context = {"profile": profile}
        return HttpResponse(template.render(context, request))
    if request.method == "POST":
        user = request.user
        profile = Profile.objects.get(user_id=user.id)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        image = request.FILES.get("image")
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile.phone = phone
        profile.image = image
        profile.save()
        messages.success(request, "You have successfully updated your profile")
        return redirect("profile")
    return redirect("main")
