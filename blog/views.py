from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView

from .models import Post


def post_list(request):
    posts = Post.published.all()

    return render(
        request, 'home.html', {'posts': posts}
    )


def post_detail(request, id):
    # 
    post = get_object_or_404(
        Post,
        id=id,
        status=Post.Status.PUBLISHED
    )

    return render(
        request,
        'post.html',
        {'post': post}
    )


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
