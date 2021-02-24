from django.urls import path

from .views import MenuListAPIView, MenuDetailAPIView, OrderView

app_namem = 'menuitems'

urlpatterns = [
    path('<int:pk>/', MenuDetailAPIView.as_view(), name = 'menu_detail'),
    path('', MenuListAPIView.as_view(), name = 'menu_list'),
    path('order/', OrderView.as_view(), name = 'order_view')
]
