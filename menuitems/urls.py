from django.urls import path

from .views import MenuListAPIView, MenuDetailAPIView

app_namem = 'menuitems'

urlpatterns = [
    path('<int:pk>/', MenuDetailAPIView.as_view(), name = 'menu_detail'),
    path('', MenuListAPIView.as_view(), name = 'menu_list'),
]
