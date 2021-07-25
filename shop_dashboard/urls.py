from django.urls import path

from .views import dashboard, dashboard_orders, dashboard_orders_un_send, dashboard_orders_send, dashboard_order_derail

urlpatterns = [
    path('dashboard', dashboard),
    path('dashboard/orders', dashboard_orders),
    path('dashboard/orders/send', dashboard_orders_send),
    path('dashboard/orders/unsend', dashboard_orders_un_send),
    path('dashboard/orders/<orderId>', dashboard_order_derail),
]
