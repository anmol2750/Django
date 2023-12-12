from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cartitems/', CartItemViews.as_view()),
    path('cartitems/<int:id>', CartItemViews.as_view())
]