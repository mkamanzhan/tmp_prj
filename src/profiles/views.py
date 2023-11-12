from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import redirect
from django.contrib import messages

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


# def login_view(request):
#     if request.POST:
#         username = request.POST["username"]
#         password = request.POST["password"]

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect("index")
#         else:
#             return HttpResponse("Login error")
#     else:
#         return render(request, "users/login.html", {})


# def auth_view(request):
#     if request.POST:
#         username = request.POST["username"]
#         password = request.POST["password"]

#         try:
#             user = User.objects.get(username=username)
#             if user is not None:
#                 return HttpResponse("Такой пользователь существует!")
#         except User.DoesNotExist:
#             User.objects.create_user(username, password=password)
#             return render(request, "users/login.html", {})

#     else:
#         return render(request, "users/auth.html", {})


# def logout_view(request):
#     logout(request)
#     return redirect("index")


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"


# class ProfileSerializer(serializers.ModelSerializer):
#     user = UserSerializer()

#     class Meta:
#         model = Profile
#         fields = "__all__"


# class ActiveProfilesList(APIView):
#     def get(self, request, format=None):
#         profiles = Profile.objects.filter(is_banned=False)
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)


# def profile(request):
#     user_id = request.user.id
#     template = loader.get_template("main/index.html")
#     profile = Profile.objects.get(user_id=user_id)
#     context = {"profile": profile}
#     return HttpResponse(template.render(context, request))
