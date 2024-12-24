from django.core.paginator import Paginator
from django.shortcuts import render
from .models import BlogPost


def blog_list(request):
    items_per_page = int(request.GET.get('items_per_page', 5))
    posts = BlogPost.objects.all()

    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog_list.html', {
        'page_obj': page_obj,
        'items_per_page': items_per_page,
    })
