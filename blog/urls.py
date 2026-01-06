from django.urls import path

from .views import post_list, post_detail, AboutPageView, ContactPageView


app_name = 'blog'


urlpatterns = [
    # post views
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]

