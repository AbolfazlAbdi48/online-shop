from django.urls import path

from .views import ProductList, product_detail, SearchList

urlpatterns = [
    path('products', ProductList.as_view()),
    path('products/<productId>/<title>', product_detail),
    path('products/search', SearchList.as_view()),
]
