from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import TemplateView, ListView

from .models import Post


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'home.html'


def post_list(request):
    pos_list = Post.published.all()
    paginator = Paginator(pos_list, 5)
    page_number = request.GET.get('page', 1)
    try: 
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    return render(
        request, 'home.html', {'posts': posts}
    )


def post_detail(request, year, month, day, post):
    # 
    post = get_object_or_404(
        Post, 
        status=Post.Status.PUBLISHED, 
        slug=post, 
        publish__year=year, 
        publish__month=month, 
        publish__day=day
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
