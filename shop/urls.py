from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('store/', views.ShopView.as_view(), name='store'),
    path('detail/<slug:pk>', views.ShopDetailView.as_view(), name='cloth_detail'),
]
