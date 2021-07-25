from django.urls import path

from .views import blog, article, search

urlpatterns = [
    path('blog', blog),
    path('blog/article/<articleId>', article),
    path('blog/search', search),
]
