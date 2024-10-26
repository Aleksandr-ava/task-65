from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
# Create your views here.
"""Первая задача"""


# def post_list(request):
#     posts = Post.objects.all()
#     paginator = Paginator(posts, 3)  # Показываем 3 поста на странице
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, 'blog/post_list.html', context)


"""Вторая задача"""


def post_list(request):
    posts = Post.objects.all()
    per_page = request.GET.get('per_page', 5)  # По умолчанию 3 поста на странице
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'per_page': per_page,
    }
    return render(request, 'blog/post_list2.html', context)
