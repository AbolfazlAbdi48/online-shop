from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name="login"),
    path('register', views.register_user, name="register"),
    path('logout', views.log_out, name="logout"),
    path('account', views.user_page, name="account"),
    path('account/edit', views.user_edit, name="editProfile"),
    path('account/paid-order',views. user_paid_orders, name="paidOrders"),
    path('account/paid-order/<orderId>', views.user_paid_order_detail, name="paidOrderDetail"),
    path('account/address', views.user_address, name="addresses"),
    path('account/address/add', views.user_add_address, name="newAddress"),
    path('account/address/edit/<addressId>', views.user_edit_address, name="editAddress"),
    path('account/address/delete/<addressId>', views.user_delete_address, name="deleteAddress"),
]
