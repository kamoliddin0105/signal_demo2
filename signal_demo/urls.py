from django.urls import path
from .views import CategoryCreateAPIView, ProductCreateAPIView, ProductUpdateAPIView, ProductDeleteAPIView

urlpatterns = [
    path('categories/', CategoryCreateAPIView.as_view(), name='create-category'),
    path('products/', ProductCreateAPIView.as_view(), name='create-product'),
    path('products-update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update-product'),
    path('products/<int:pk>/delete/', ProductDeleteAPIView.as_view(), name='delete-product'),
]
