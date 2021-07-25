from django.urls import path

from .views import add_user_order, order_list

urlpatterns = [
    path('add-user-order', add_user_order),
    path('orders', order_list),
]
