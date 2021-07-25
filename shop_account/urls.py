from django.urls import path

from .views import login_user, register_user, user_page, user_edit, user_address, user_add_address, user_edit_address, \
    user_delete_address, user_paid_orders, user_paid_order_detail, log_out

urlpatterns = [
    path('login', login_user),
    path('register', register_user),
    path('log-out', log_out),
    path('account', user_page),
    path('account/edit', user_edit),
    path('account/paid-order', user_paid_orders),
    path('account/paid-order/<orderId>', user_paid_order_detail),
    path('account/address', user_address),
    path('account/address/add', user_add_address),
    path('account/address/edit/<addressId>', user_edit_address),
    path('account/address/delete/<addressId>', user_delete_address),
]
