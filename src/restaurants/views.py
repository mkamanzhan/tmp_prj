from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from src.restaurants.models import Restaurant, Review
from src.restaurants.utils import divide_chunks


def main(request):
    if request.method == "GET":
        template = loader.get_template("pages/main.html")
        restaurants = Restaurant.objects.order_by("-rating")
        paginator = Paginator(restaurants, 20)
        page_number = request.GET.get("page", 1)
        page_restaurants = paginator.get_page(page_number)
        restaurants_chunks = divide_chunks(page_restaurants, size=4)
        context = {
            "restaurants_chunks": restaurants_chunks,
        }
        return HttpResponse(template.render(context, request))
    return redirect("main")


# def main(request):
#     template = loader.get_template("index.html")
#     pub = Post.objects.order_by("published")
#     context = {"pub": pub}
#     return HttpResponse(template.render(context, request))


# def students(request):
#     template = loader.get_template("main/students.html")
#     context = {}
#     return HttpResponse(template.render(context, request))


# def posts_create(request):
#     if request.method == "GET":
#         template = loader.get_template("main/create.html")
#         return HttpResponse(template.render({}, request))
#     if request.method == "POST":
#         user_id = request.user.id
#         title = request.POST.get("title")
#         text = request.POST.get("text")
#         post = Post(user_id=user_id, title=title, text=text)
#         post.save()
#         return redirect("index")
#     return redirect("index")


# def comments_create(request):
#     if request.method == "POST":
#         user_id = request.user.id
#         post_id = request.POST.get("post_id")
#         text = request.POST.get("text")
#         comment = Comment(user_id=user_id, post_id=post_id, text=text)
#         comment.save()
#         return redirect("posts_detail", post_id=post_id)
#     return redirect("index")


# def main_(request):
#     template = loader.get_template("main/index.html")
#     usr = Post.objects.order_by("user")
#     context = {"usr": usr}
#     return HttpResponse(template.render(context, request))


# def posts_detail(request, post_id):
#     if request.method == "GET":
#         template = loader.get_template("main/posts.html")
#         post = get_object_or_404(Post, id=post_id)
#         comments = Comment.objects.filter(post_id=post_id).order_by("-id")
#         form = CommentForm()
#         form_post = PostForm()
#         context = {
#             "post": post,
#             "comments": comments,
#             "form": form,
#             "form_post": form_post,
#         }
#         return HttpResponse(template.render(context, request))
#     return redirect("index")
