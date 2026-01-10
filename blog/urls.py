from django.urls import path

from .views import post_list, post_detail, post_share, post_comment, \
    AboutPageView, ContactPageView, PostListView


app_name = 'blog'


urlpatterns = [
    # post views
    # path('', post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    # path('<int:id>/', post_detail, name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', post_detail, name='post_detail'), 
    path('<int:post_id>/share/', post_share, name='post_share'), 
    path('<int:post_id>/comment/', post_comment, name='post_comment'), 
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]

